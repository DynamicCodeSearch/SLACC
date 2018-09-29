package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.executors.MethodExecutor;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.util.logging.Logger;

public class Execute {
    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

    private static final boolean EXECUTE_ONLY_ONCE = false;

    static {
        System.setOut(new PrintStream(new OutputStream() {

            @Override
            public void write(int b) throws IOException {}

        }));
    }

    public static void execute() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            executeProblem(problem, false);
        }
    }

    public static void executeOnce() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            executeProblem(problem, true);
        }
    }

    public static void executeProblem(String problem, Boolean onlySingle) {
        LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
        String problemPath = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        for(String javaFile: CodejamUtils.listGeneratedFiles(problemPath)) {
            MethodExecutor executor = new MethodExecutor(javaFile, store);
            executor.process();
        }
    }

    public static void executeFunction(String filePath, String functionName) {
        MethodExecutor.process(filePath, functionName, EXECUTE_ONLY_ONCE);
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            LOGGER.info(String.format("Running for %s" , args[0]));
            executeProblem(args[0], EXECUTE_ONLY_ONCE);
        } else {
            LOGGER.info("Running for all");
            execute();
        }
    }

}
