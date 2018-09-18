package edu.ncsu.codejam;

import edu.ncsu.executors.MethodExecutor;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.store.ArgumentStore;

import java.util.List;
import java.util.logging.Logger;

public class Execute {
    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

    public static void execute() {
        LOGGER.info("Executing codejam projects. Here we go ....");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        for (String javaFile: javaFiles) {
            MethodExecutor executor = new MethodExecutor(javaFile, store);
            executor.process();
            System.exit(0);
        }

    }

    public static void main(String[] args) {
        execute();
    }

}
