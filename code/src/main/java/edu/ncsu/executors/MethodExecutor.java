package edu.ncsu.executors;

import com.google.common.util.concurrent.SimpleTimeLimiter;
import com.google.common.util.concurrent.TimeLimiter;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.store.ArgumentStore;

import java.lang.reflect.Method;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

public class MethodExecutor {

    private static final Logger LOGGER = Logger.getLogger(MethodExecutor.class.getName());

    private ExecutorService executor;

    private TimeLimiter timeLimiter;

    private Class clazz;

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

    public MethodExecutor(String sourcePath, Class clazz, ArgumentStore store) {
        this.clazz = clazz;
        this.store = store;
        this.classMethods = new ClassMethods(sourcePath);
        initialize();
    }


    public void process() {
        Method[] methods = clazz.getMethods();
        for (Method method: classMethods.getMethods()) {
            // TODO: Get arguments for method.
            // TODO: Profile method.
        }
    }
}
