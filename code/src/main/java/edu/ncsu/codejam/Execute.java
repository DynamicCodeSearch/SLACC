package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.executors.MethodExecutor;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.utils.Utils;

import java.util.logging.Logger;

public class Execute {
    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

    public static void execute() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            executeProblem(problem);
        }
    }

    public static void executeOnce() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            executeProblemOnce(problem);
        }
    }


    public static void executeProblem(String problem) {
        LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
        String problemPath = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        for(String javaFile: CodejamUtils.listGeneratedFiles(problemPath)) {
            MethodExecutor executor = new MethodExecutor(javaFile, store);
            executor.process(false);
        }
    }

    public static void executeProblemOnce(String problem) {
        LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
        String problemPath = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        for(String javaFile: CodejamUtils.listGeneratedFiles(problemPath)) {
            MethodExecutor executor = new MethodExecutor(javaFile, store);
            executor.process(true);
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            LOGGER.info(String.format("Running for %s" , args[0]));
            executeProblem(args[0]);
        } else {
            LOGGER.info("Running for all");
            execute();
        }
    }

}
