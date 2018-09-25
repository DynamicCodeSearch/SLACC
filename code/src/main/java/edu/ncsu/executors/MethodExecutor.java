package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import com.google.common.util.concurrent.UncheckedTimeoutException;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.store.StoreUtils;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.*;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private ExecutorService taskExecutor;

    private ExecutorService timeExecutor;

    private TimeLimiter timeLimiter;

    private ClassMethods classMethods;

    private ArgumentStore store;


    private void initialize() {
        if (timeExecutor == null || timeExecutor.isShutdown())
            timeExecutor = Executors.newFixedThreadPool(Properties.NUM_THREADS);
        if (timeLimiter == null)
            timeLimiter = new SimpleTimeLimiter(timeExecutor);
        if (taskExecutor == null || taskExecutor.isShutdown())
            taskExecutor = Executors.newFixedThreadPool(Properties.NUM_THREADS);
    }

    private static void shutdownExecutor(ExecutorService executorService) {
        if (executorService != null && !executorService.isShutdown()) {
            executorService.shutdown();
            try {
                executorService.awaitTermination(Properties.METHOD_EXECUTION_WAIT_TIME, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            executorService.shutdownNow();
        }
    }

    private void shutdown() {
        shutdownExecutor(timeExecutor);
        timeLimiter = null;
        shutdownExecutor(taskExecutor);
    }

    public MethodExecutor(String sourcePath, ArgumentStore store) {
        this.store = store;
        this.classMethods = new ClassMethods(sourcePath);
        initialize();
    }


    public void process(boolean onlySingle) {
        JsonObject results = new JsonObject();
        JsonArray failedFunctions = new JsonArray();
        String writeFolder = Utils.pathJoin(Properties.META_RESULTS, classMethods.getPackageName().replaceAll("\\.", File.separator));
        String writeFile = Utils.pathJoin(writeFolder, String.format("%s.json", classMethods.getClassName()));
        if (Utils.fileExists(writeFile)){
            LOGGER.info(String.format("%s.%s already processed. Moving On!", classMethods.getPackageName(), classMethods.getClassName()));
            return;
        }
        LOGGER.info(String.format("Processing %s.%s ...", classMethods.getPackageName(), classMethods.getClassName()));
        List<Callable<JsonObject>> functionTasks = new ArrayList<>();
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            if (function.isFuzzable() && function.makeArgumentsKey() != null) {
                functionTasks.add(makeFunctionTask(function, onlySingle));
            }
        }
        try {
            List<Future<JsonObject>> functionResults = taskExecutor.invokeAll(functionTasks);
            for (Future<JsonObject> functionResult: functionResults) {
                assert functionResult.isDone();
                JsonObject executionResult = functionResult.get();
                if (executionResult.has("output")) {
                    JsonObject outputResult = executionResult.get("output").getAsJsonObject();
                    results.add(outputResult.get("name").getAsString(), outputResult);
                } else if (executionResult.has("error")) {
                    JsonObject error = executionResult.get("error").getAsJsonObject();
                    failedFunctions.add(error);
                }
            }
        } catch (Exception e) {
            LOGGER.severe(String.format("Exception while invoking all function tasks in class: %s.%s",
                    classMethods.getPackageName(), classMethods.getClassName()));
            e.printStackTrace();
        }
        results.add("errors", failedFunctions);
        Utils.mkdir(writeFolder);
        if (results.size() == 0) {
            LOGGER.info("None of the functions logged from " + classMethods.getClassName());
        } else {
            LOGGER.info("Results logged to: " + writeFile);
            StoreUtils.saveJsonObject(results, writeFile, true);
        }
        shutdown();
    }

    public Callable<JsonObject> makeFunctionTask(final Function function, final boolean onlySingle) {

        Callable<JsonObject> functionTask = new Callable<JsonObject>() {
            @Override
            public JsonObject call() throws Exception {
                JsonObject returnVal = new JsonObject();
                try {
                    if (onlySingle) {
                        returnVal.add("output", processFunctionOnce(function));;
                    } else {
                        returnVal.add("output", processFunction(function));;
                    }
                } catch (Exception e) {
                    LOGGER.severe(String.format("Exception in function: %s", function.getName()));
                    JsonObject failedFunction = new JsonObject();
                    StringWriter sw = new StringWriter();
                    e.printStackTrace(new PrintWriter(sw));
                    failedFunction.addProperty("name", function.getName());
                    failedFunction.addProperty("errorTrace", sw.toString());
                    returnVal.add("error", failedFunction);
                }
                return returnVal;
            }
        };
        return functionTask;
    }


    public JsonObject processFunction(Function function) {
        System.out.println(String.format("Function: %s", function.getName()));
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        if (executionArgs == null || executionArgs.size() == 0) {
            LOGGER.info(String.format("Execution args does not exist for args key: %s", function.makeArgumentsKey()));
            return null;
        }
        JsonArray executions = new JsonArray();
        for (Object[] executionArg: executionArgs) {
            executions.add(profileMethod(function, executionArg));
        }
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("inputKey", function.makeArgumentsKey());
        functionData.add("outputs", executions);
        return functionData;
    }


    public JsonObject processFunctionOnce(Function function) {
        System.out.println(String.format("Function: %s", function.getName()));
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        if (executionArgs == null || executionArgs.size() == 0) {
            LOGGER.info(String.format("Execution args does not exist for args key: %s", function.makeArgumentsKey()));
            return null;
        }
        JsonArray executions = new JsonArray();
        executions.add(profileMethod(function, executionArgs.get(0)));
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("inputKey", function.makeArgumentsKey());
        functionData.add("outputs", executions);
        return functionData;
    }


    public synchronized JsonObject profileMethod(final Function function, final Object... executionArguments) {
        Callable<Object> methodCall = new Callable<Object>() {
            @Override
            public Object call() {
                try {
                    return function.getMethod().invoke(null, executionArguments);
                } catch (InvocationTargetException e) {
                    throw new RuntimeException(e.getTargetException());
                } catch (Exception e) {
                    e.printStackTrace();
                    throw new RuntimeException(e);
                }
            }
        };
        Object returnVariable = null;
        String errorMessage = null;
        long duration = Properties.METHOD_EXECUTION_WAIT_TIME * 1000;
        try {
            long startTime = System.currentTimeMillis();
            returnVariable = timeLimiter.callWithTimeout(methodCall, Properties.METHOD_EXECUTION_WAIT_TIME,
                    TimeUnit.SECONDS, true);
            duration = System.currentTimeMillis() - startTime;
        } catch (UncheckedTimeoutException e) {
            errorMessage = String.format("Method timed out after %d seconds", Properties.METHOD_EXECUTION_WAIT_TIME);
        } catch (Exception e) {
            errorMessage = e.getMessage();
        }
        return function.dumpReturnAsJSON(returnVariable, errorMessage, duration);
    }


    public List<Object[]> fetchFunctionExecutionArgs(Function function) {
        JsonArray arguments = store.loadFuzzedArguments(function.makeArgumentsKey());
        List<Object[]> functionArgs = new ArrayList<>();
        for (Object arg: arguments) {
            functionArgs.add(function.convertToFunctionArguments(arg).toArray());
        }
        return functionArgs;
    }


    public static void main(String[] args) {
        String source = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Y11R5P1/Egor/generated_class_mini.java";
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        MethodExecutor methodExecutor = new MethodExecutor(source, store);
        methodExecutor.process(true);
    }
}
