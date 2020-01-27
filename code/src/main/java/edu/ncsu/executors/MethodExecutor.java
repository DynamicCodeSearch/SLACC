package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import com.google.common.util.concurrent.UncheckedTimeoutException;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IArgumentStore;
import edu.ncsu.store.IFunctionStore;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.*;
import java.util.concurrent.*;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private static final String METHOD_EXECUTED = "COMPLETED";

    private static Boolean ONLY_SINGLE = false;

    private static ExecutorService taskExecutor;

    private String dataset;

    private ExecutorService timeExecutor;

    private TimeLimiter timeLimiter;

    private ClassMethods classMethods;

    private IArgumentStore argumentStore;

    private IFunctionStore functionStore;


    static {
        if (taskExecutor == null || taskExecutor.isShutdown())
            taskExecutor = Executors.newFixedThreadPool(Settings.getNumThreads());

//        System.setOut(new PrintStream(new OutputStream() {
//            @Override
//            public void write(int b) {}
//        }));
    }

    private void initialize() {
        if (timeExecutor == null || timeExecutor.isShutdown())
            timeExecutor = Executors.newFixedThreadPool(Settings.getNumThreads());
        if (timeLimiter == null)
            timeLimiter = new SimpleTimeLimiter(timeExecutor);
    }

    private static void shutdownExecutor(ExecutorService executorService) {
        if (executorService != null && !executorService.isShutdown()) {
            executorService.shutdown();
            try {
                executorService.awaitTermination(Settings.METHOD_EXECUTION_WAIT_TIME, TimeUnit.SECONDS);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
            executorService.shutdownNow();
        }
    }

    private void shutdown() {
        LOGGER.info("Shutting down time executor");
        shutdownExecutor(timeExecutor);
        timeLimiter = null;
        LOGGER.info("Shutting down task executor");
        shutdownExecutor(taskExecutor);
    }

    private MethodExecutor(String dataset, Boolean isTest) {
        this.dataset = dataset;
        if (isTest) {
            this.argumentStore = BaseStorage.loadTestArgumentStore(dataset);
            this.functionStore = BaseStorage.loadTestFunctionStore(dataset);
        } else {
            this.argumentStore = BaseStorage.loadArgumentStore(dataset);
            this.functionStore = BaseStorage.loadFunctionStore(dataset);
        }
    }

    private MethodExecutor(String dataset, String sourcePath) {
        this(dataset, sourcePath, false);
    }

    private MethodExecutor(String dataset, String sourcePath, Boolean isTest) {
        this(dataset, isTest);
        this.classMethods = new ClassMethods(this.dataset, sourcePath);
        initialize();
    }

    /**
     * Retrieve function tasks for the Method Executor
     * @return Function Tasks for the java file
     */
    private List<Callable<Map<String, String>>> getFunctionTasks() {
        LOGGER.info(String.format("Fetching function tasks for %s.%s ...", classMethods.getPackageName(), classMethods.getClassName()));
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        int totalFunctions = 0;
        List<Function> validFunctions = new ArrayList<>();
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            if (function.isFuzzable() && function.makeArgumentsKey() != null) {
                if (!this.functionStore.isStored(function)) {
                    validFunctions.add(function);
                }
                ++totalFunctions;
            }
        }
        LOGGER.info(String.format("Number of functions to process = %d / %d", functionTasks.size(), totalFunctions));
        for (int i=0; i<validFunctions.size(); i++)
            functionTasks.add(makeFunctionTask(this.dataset, classMethods.getSourcePath(),
                    validFunctions.get(i).getName(), i , validFunctions.size(), false));
        return functionTasks;
    }

    /***
     * Execute a list of FunctionTask.
     * @param functionTasks - list of function tasks to execute.
     */
    private static void executeFunctionTasks(List<Callable<Map<String, String>>> functionTasks) {
        if (functionTasks == null || functionTasks.size() == 0)
            return;
        long timeToWait = 2 * functionTasks.size() * Settings.ALL_METHOD_EXECUTIONS_WAIT_TIME * Settings.METHOD_EXECUTION_WAIT_TIME;
        LOGGER.info(String.format("Time to wait = %d", timeToWait));
        try {
            List<Future<Map<String, String>>> functionResults = taskExecutor.invokeAll(functionTasks, timeToWait, TimeUnit.SECONDS);
            LOGGER.info("Invoked All!");
            int toRun = functionResults.size();
            for (Future<Map<String, String>> functionResult: functionResults) {
//                assert functionResult.isDone();
                Map<String, String> executionResult = functionResult.get();
                LOGGER.info("Fetched execution results");
                if (!executionResult.get("status").equals(METHOD_EXECUTED)) {
                    LOGGER.severe(String.format("Exception occurred while processing function: %s", executionResult.get("name")));
                }
                LOGGER.info(String.format("Functions remaining: %d/%d", toRun, functionResults.size()));
                --toRun;
            }
            LOGGER.info("Completed invocation");
        } catch (Exception e) {
            LOGGER.severe("Exception while invoking all function tasks");
            e.printStackTrace();
        }

    }


    public static void process(String filePath, String functionName, String dataset, Boolean isTest) {
        MethodExecutor executor =  new MethodExecutor(dataset, filePath, isTest);
        ClassMethods classMethods = executor.classMethods;
        LOGGER.info(String.format("Processing function %s.%s.%s ... ",
                classMethods.getPackageName(), classMethods.getClassName(), functionName));
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
        } else {
            LOGGER.info(String.format("Storing Function: %s", functionName));
            executor.storeFunction(function);
            LOGGER.info(String.format("Function Stored: %s", functionName));
        }
        LOGGER.info(String.format("Shutting Down Function: %s", functionName));
        executor.shutdown();
    }


    private static Callable<Map<String, String>> makeFunctionTask(final String dataset, final String sourcePath,
                                                                  final String functionName, final int taskNumber,
                                                                  final int totalTasks, final boolean isTest) {
        return new Callable<Map<String, String>>() {
            @Override
            public Map<String, String> call() {
                Map<String, String> retMap = new HashMap<>();
                retMap.put("name", functionName);
                try {
                    executeAsBash(dataset, sourcePath, functionName, taskNumber, totalTasks, isTest);
                    retMap.put("status", METHOD_EXECUTED);
                } catch (Exception e) {
                    retMap.put("status", e.getMessage());
                }
                return retMap;
            }
        };
    }

    private static void executeAsBash(String dataset, String sourcePath, String functionName, int taskNumber, int totalTasks, boolean isTest) {
        try {
            LOGGER.info(String.format("Submitted %s. Doing: %d / %d", functionName, taskNumber + 1, totalTasks));
            String scriptsFolder = Utils.pathJoin("scripts", "java");
            if (isTest)
                scriptsFolder = Utils.pathJoin(scriptsFolder, "test");
            String command = String.format("sh %s %s %s %s",
                    Utils.pathJoin(scriptsFolder, "execute_single_function.sh"),
                    dataset, sourcePath, functionName);
            Process process = Runtime.getRuntime().exec(command, Utils.getEnvs(), new File(Settings.CODE_HOME));
            process.waitFor();
            LOGGER.info(String.format("Output: %s\nError: %s\n", Utils.getOutput(process), Utils.getError(process)));
            process.destroy();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private void storeFunction(Function function) {
        JsonObject executionResult = executeFunction(function);
        if (executionResult.has("output")) {
            JsonObject outputResult = executionResult.get("output").getAsJsonObject();
            functionStore.updateFunctionResult(outputResult);
        } else if (executionResult.has("error")) {
            JsonObject error = executionResult.get("error").getAsJsonObject();
            functionStore.updateFunctionError(error);
        }
    }

    private JsonObject executeFunction(Function function) {
        JsonObject returnVal = new JsonObject();
        try {
            if (ONLY_SINGLE) {
                returnVal.add("output", processFunctionOnce(function));
            } else {
                returnVal.add("output", processFunction(function));
            }
        } catch (Exception e) {
            LOGGER.severe(String.format("Exception in function: %s", function.getName()));
            e.printStackTrace();
            JsonObject failedFunction = new JsonObject();
            StringWriter sw = new StringWriter();
            e.printStackTrace(new PrintWriter(sw));
            failedFunction.addProperty("name", function.getName());
            failedFunction.addProperty("class", function.getClassName());
            failedFunction.addProperty("package", function.getPackageName());
            failedFunction.addProperty("errorTrace", sw.toString());
            returnVal.add("error", failedFunction);
        }
        return returnVal;
    }


    private JsonObject processFunction(Function function) {
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        if (executionArgs == null || executionArgs.size() == 0) {
            LOGGER.info(String.format("Execution args does not exist for args key: %s", function.makeArgumentsKey()));
            return null;
        }
        JsonArray executions = new JsonArray();
        int argCount = 0;
        for (Object[] executionArg: executionArgs) {
            executions.add(profileMethod(function, argCount, executionArg));
            argCount += 1;
        }
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("class", function.getClassName());
        functionData.addProperty("package", function.getPackageName());
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
        executions.add(profileMethod(function, 0, executionArgs.get(0)));
        JsonObject functionData = new JsonObject();
        functionData.addProperty("name", function.getName());
        functionData.addProperty("class", function.getClassName());
        functionData.addProperty("inputKey", function.makeArgumentsKey());
        functionData.add("outputs", executions);
        return functionData;
    }


    private synchronized JsonObject profileMethod(final Function function, final int argSetIndex, final Object... executionArguments) {
        Callable<Object> methodCall = new Callable<Object>() {
            @Override
            public Object call() {
                try {
                    return function.getMethod().invoke(null, executionArguments);
                } catch (InvocationTargetException e) {
                    throw new RuntimeException(e.getTargetException());
                } catch (Exception e) {
                    throw new RuntimeException(e);
                }
            }
        };
        Object returnVariable = null;
        String errorMessage = null;
        long duration = Settings.METHOD_EXECUTION_WAIT_TIME * 1000;
        try {
            long startTime = System.currentTimeMillis();
            returnVariable = timeLimiter.callWithTimeout(methodCall, Settings.METHOD_EXECUTION_WAIT_TIME,
                    TimeUnit.SECONDS, true);
            duration = System.currentTimeMillis() - startTime;
        } catch (UncheckedTimeoutException e) {
            errorMessage = String.format("Method timed out after %d seconds", Settings.METHOD_EXECUTION_WAIT_TIME);
        } catch (Exception e) {
            errorMessage = e.getMessage();
        }
        return function.dumpReturnAsJSON(returnVariable, errorMessage, duration, argSetIndex);
    }


    private List<Object[]> fetchFunctionExecutionArgs(Function function) {
        JsonArray arguments = argumentStore.loadFuzzedArguments(function.makeArgumentsKey());
        List<Object[]> functionArgs = new ArrayList<>();
        int argCount = 0;
        for (Object arg: arguments) {
            functionArgs.add(function.convertToFunctionArguments(arg, argCount).toArray());
            argCount += 1;
        }
        return functionArgs;
    }



    // *******************************************************************************
    // Static executor method that executes dataset, problem, function etc

    /**
     * Execute a dataset
     * @param dataset - Dataset to execute
     */
    public static void executeDataset(String dataset) {
        LOGGER.info(String.format("Executing methods for dataset: %s. Here we go .... ", dataset));
        String datasetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        List<String> javaFiles = Utils.listPermutatedFiles(datasetPath);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = Utils.listGeneratedFiles(datasetPath);
        }
        for (String javaFile: javaFiles) {
            MethodExecutor executor = new MethodExecutor(dataset, javaFile);
            functionTasks.addAll(executor.getFunctionTasks());
        }
        MethodExecutor.executeFunctionTasks(functionTasks);
        System.exit(0);
    }

    public static void executeProblem(String dataset, String problem) {
        LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
        String problemPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset, problem);
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        List<String> javaFiles = Utils.listPermutatedFiles(problemPath);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = Utils.listGeneratedFiles(problemPath);
        }
        for (String javaFile: javaFiles) {
            MethodExecutor executor = new MethodExecutor(dataset, javaFile);
            functionTasks.addAll(executor.getFunctionTasks());
        }
        MethodExecutor.executeFunctionTasks(functionTasks);
    }

    public static void reExecuteDataset(String dataset) {
        LOGGER.info(String.format("Rerunning java functions for dataset: %s", dataset));
        MethodExecutor executor = new MethodExecutor(dataset, true);
        List<String> functionNames = executor.functionStore.getExecutedFunctionNames("java");
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore();
        List<Callable<Map<String, String>>> functionTasks = new ArrayList<>();
        int index = 0;
        int totalFunctions = functionNames.size();
        for (String functionName: functionNames) {
            String sourceFile = metadataStore.getSourceFile(dataset, functionName);
            if (sourceFile == null) {
                throw new RuntimeException("Source File not found for function: " + functionName);
            }
            functionTasks.add(makeFunctionTask(dataset, sourceFile, functionName, index, totalFunctions, true));
            index += 1;
        }
        MethodExecutor.executeFunctionTasks(functionTasks);
    }

    private static void testArgGen() {
        String dataset = CodejamUtils.DATASET;
        String sourceFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Example/aditsu/generated_class_f70e39fe0ce54ddca9f8b5e72ebaa350.java";
        String functionName = "func_ba7a218bebc34cbd843a7e3f59d1c4f3";
        MethodExecutor executor = new MethodExecutor(dataset, sourceFile, false);
        ClassMethods classMethods = executor.classMethods;
        LOGGER.info(String.format("Processing function %s.%s.%s ... ",
                classMethods.getPackageName(), classMethods.getClassName(), functionName));
        Function function = null;
        for (Method method: classMethods.getMethods()) {
            if (method.getName().equals(functionName)) {
                function = classMethods.getFunction(method);
                break;
            }
        }
        if (function != null) {
//            int validArgIndex = 0;
//            JsonArray arguments = executor.argumentStore.loadFuzzedArguments(function.makeArgumentsKey());
//            Object arg = arguments.get(validArgIndex);
//            Object[] converted = function.convertToFunctionArguments(arg, validArgIndex).toArray();
//            JsonObject res = executor.profileMethod(function, validArgIndex, converted);
//            System.out.println(res);
            System.out.println(executor.processFunction(function));
            executor.shutdown();

//            System.out.println(res);

//            for (Object arg: arguments) {
//                System.out.println(arg);
////                Object[] converted = function.convertToFunctionArguments(arg).toArray();
//                i += 1;
//                System.out.print(i);
//                System.out.println("*******");
//                if (i > 10)  {
//                    break;
//                }
//                // TODO: delete reader/writer file on exit
//            }
//            List<Object[]> functionArgs = executor.fetchFunctionExecutionArgs(function);
//            for (Object[] executionArg: functionArgs) {
//                executor.profileMethod(function, executionArg);
//            }

        }


    }

    private static void testExecution() {
        String dataset = CodejamUtils.DATASET;
        String sourceFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Example/aditsu/generated_class_f70e39fe0ce54ddca9f8b5e72ebaa350.java";
        String functionName = "func_ba7a218bebc34cbd843a7e3f59d1c4f3";
        MethodExecutor.process(sourceFile, functionName, dataset, false);
//        MethodExecutor executor = new MethodExecutor(dataset, sourceFile);
//        MethodExecutor.executeFunctionTasks(executor.getFunctionTasks());
    }

    public static void main(String[] args) {
        testArgGen();
//        testExecution();
    }
}
