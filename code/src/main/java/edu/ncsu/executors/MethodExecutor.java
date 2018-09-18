package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import com.google.common.util.concurrent.UncheckedTimeoutException;
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.ArgumentStore;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private ExecutorService executor;

    private TimeLimiter timeLimiter;

    private ClassMethods classMethods;

    private ArgumentStore store;


    private void initialize() {
        if (executor == null || executor.isShutdown())
            executor = Executors.newFixedThreadPool(Properties.NUM_THREADS);
        if (timeLimiter == null)
            timeLimiter = new SimpleTimeLimiter(executor);
    }

    private void shutdown() {
        if (executor == null || executor.isShutdown()) {
            timeLimiter = null;
            return;
        }
        executor.shutdown();
        try {
            executor.awaitTermination(Properties.METHOD_EXECUTION_WAIT_TIME, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        executor.shutdownNow();
        timeLimiter = null;
    }

    public MethodExecutor(String sourcePath, ArgumentStore store) {
        this.store = store;
        this.classMethods = new ClassMethods(sourcePath);
        initialize();
    }


    public void process() {
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            processFunction(function);
        }
        shutdown();
    }


    public void processFunction(Function function) {
        System.out.println(String.format("Function: %s", function.getName()));
        List<Object[]> executionArgs = fetchFunctionExecutionArgs(function);
        JsonArray array = new JsonArray();
        for (Object[] executionArg: executionArgs) {
            array.add(profileMethod(function, executionArg));
        }
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
        try {
            returnVariable = timeLimiter.callWithTimeout(methodCall, Properties.METHOD_EXECUTION_WAIT_TIME,
                    TimeUnit.SECONDS, true);
        } catch (UncheckedTimeoutException e) {
            errorMessage = String.format("Method timed out after %d seconds", Properties.METHOD_EXECUTION_WAIT_TIME);
        } catch (Exception e) {
            errorMessage = e.getMessage();
        }
        return function.dumpReturnAsJSON(returnVariable, errorMessage);
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
        methodExecutor.process();
    }
}
