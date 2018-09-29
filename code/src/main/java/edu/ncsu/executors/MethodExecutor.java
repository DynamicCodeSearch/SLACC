package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import com.google.common.util.concurrent.UncheckedTimeoutException;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.store.StoreUtils;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.*;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private static final String METHOD_EXECUTED = "COMPLETED";

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


    public void process() {
        String writeFolder = Utils.pathJoin(Properties.META_RESULTS, classMethods.getPackageName().replaceAll("\\.", File.separator));
        String writeFile = Utils.pathJoin(writeFolder, String.format("%s.json", classMethods.getClassName()));
        LOGGER.info(String.format("Processing %s.%s ...", classMethods.getPackageName(), classMethods.getClassName()));
        JsonObject results;
        JsonArray failedFunctions;
        if (Utils.fileExists(writeFile)) {
            results = StoreUtils.getJsonObject(writeFile).getAsJsonObject();
        } else {
            results = new JsonObject();
        }
        if (results.has("errors")) {
            failedFunctions = results.get("errors").getAsJsonArray();
        } else {
            failedFunctions = new JsonArray();
        }
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        int totalFunctions = 0;
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            if (function.isFuzzable() && function.makeArgumentsKey() != null) {
                if (!results.has(function.getName()) && !errorContainsFunction(failedFunctions, function.getName())) {
                    functionTasks.add(makeFunctionTask(function));
                }
                ++totalFunctions;
            }
        }
        LOGGER.info(String.format("Number of functions to process = %d / %d", functionTasks.size(), totalFunctions));
        if (functionTasks.isEmpty()) {
            LOGGER.info(String.format("%s.%s already processed. Moving On!", classMethods.getPackageName(), classMethods.getClassName()));
            shutdown();
            return;
        }
        try {
            int toRun = functionTasks.size();
            List<Future<Map<String, String>>> functionResults = taskExecutor.invokeAll(functionTasks);
            for (Future<Map<String, String>> functionResult: functionResults) {
                assert functionResult.isDone();
                Map<String, String> executionResult = functionResult.get();
                if (!executionResult.get("status").equals(METHOD_EXECUTED)) {
                    Utils.mkdir(writeFolder);
                    LOGGER.severe(String.format("Exception occured while processing function: %s", executionResult.get("name")));
                    JsonObject failedFunction = new JsonObject();
                    failedFunction.addProperty("name", executionResult.get("name"));
                    failedFunction.addProperty("errorTrace", executionResult.get("status"));
                    updateError(writeFile, failedFunction);
                }
                LOGGER.info(String.format("Functions remaining: %d/%d", toRun, totalFunctions));
                --toRun;

            }
        } catch (Exception e) {
            LOGGER.severe(String.format("Exception while invoking all function tasks in class: %s.%s",
                    classMethods.getPackageName(), classMethods.getClassName()));
            e.printStackTrace();
        }
        shutdown();
    }


    public static void process(String filePath, String functionName, boolean onlySingle) {
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        MethodExecutor executor =  new MethodExecutor(filePath, store);
        ClassMethods classMethods = executor.classMethods;
        Function function = null;
        for (Method method: classMethods.getMethods()) {
            Function tempFunction = classMethods.getFunction(method);
            if (tempFunction.getName().equals(functionName)) {
                function = tempFunction;
                break;
            }
        }
        if (function == null) {
            LOGGER.info("No function found. Terminating");
            executor.shutdown();
        }
        executor.storeFunction(function, onlySingle);
        executor.shutdown();
    }


    private static boolean errorContainsFunction(JsonArray errors, String functionName) {
        for (JsonElement error: errors) {
            if (error.getAsJsonObject().get("name").getAsString().equals(functionName))
                return true;
        }
        return false;
    }

    private synchronized static void updateResult(String fileName, JsonObject result) {
        JsonObject results;
        if (Utils.fileExists(fileName)) {
            results = StoreUtils.getJsonObject(fileName).getAsJsonObject();
        } else {
            results = new JsonObject();
        }
        results.add(result.get("name").getAsString(), result);
        StoreUtils.saveJsonObject(results, fileName, true);
    }

    private synchronized static void updateError(String fileName, JsonObject error) {
        JsonObject results;
        if (Utils.fileExists(fileName)) {
            results = StoreUtils.getJsonObject(fileName).getAsJsonObject();
        } else {
            results = new JsonObject();
        }
        JsonArray failedFunctions;
        if (results.has("errors")) {
            failedFunctions = results.get("errors").getAsJsonArray();
        } else {
            failedFunctions = new JsonArray();
        }
        if (!errorContainsFunction(failedFunctions, error.get("name").getAsString())) {
            failedFunctions.add(error);
            results.add("error", failedFunctions);
            StoreUtils.saveJsonObject(results, fileName, true);
        }
    }

    private Callable<Map<String, String>> makeFunctionTask(final Function function) {

        return new Callable<Map<String, String>>() {
            @Override
            public Map<String, String> call() {
                Map<String, String> retMap = new HashMap<>();
                retMap.put("name", function.getName());
                try {
                    executeAsBash(function.getName());
                    retMap.put("status", METHOD_EXECUTED);
                } catch (Exception e) {
                    retMap.put("status", e.getMessage());
                }
                return retMap;
            }
        };
    }

    private void executeAsBash(String functionName) {
        try {
            String command = String.format("sh scripts/codejam/execute_single_function.sh %s %s",
                    classMethods.getSourcePath(), functionName);
            Process process = Runtime.getRuntime().exec(command, Utils.getEnvs(), new File(Properties.CODE_HOME));
            process.waitFor();
            LOGGER.info(String.format("Output: %s", Utils.getOutput(process)));
            LOGGER.info(String.format("Error : %s", Utils.getOutput(process)));
            process.destroy();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void storeFunction(Function function, boolean onlySingle) {
        String writeFolder = Utils.pathJoin(Properties.META_RESULTS, classMethods.getPackageName().replaceAll("\\.", File.separator));
        String writeFile = Utils.pathJoin(writeFolder, String.format("%s.json", classMethods.getClassName()));
        JsonObject executionResult = executeFunction(function, onlySingle);
        if (executionResult.has("output")) {
            JsonObject outputResult = executionResult.get("output").getAsJsonObject();
            Utils.mkdir(writeFolder);
            updateResult(writeFile, outputResult);
        } else if (executionResult.has("error")) {
            JsonObject error = executionResult.get("error").getAsJsonObject();
            Utils.mkdir(writeFolder);
            updateError(writeFile, error);
        }
    }

    private JsonObject executeFunction(Function function, boolean onlySingle) {
        JsonObject returnVal = new JsonObject();
        try {
            if (onlySingle) {
                returnVal.add("output", processFunctionOnce(function));
            } else {
                returnVal.add("output", processFunction(function));
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


    private JsonObject processFunction(Function function) {
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


    private JsonObject processFunctionOnce(Function function) {
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


    private synchronized JsonObject profileMethod(final Function function, final Object... executionArguments) {
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


    private List<Object[]> fetchFunctionExecutionArgs(Function function) {
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
        methodExecutor.process();
    }
}
