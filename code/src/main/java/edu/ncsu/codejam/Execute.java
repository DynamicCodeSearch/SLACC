package edu.ncsu.codejam;

import edu.ncsu.executors.MethodExecutor;

import java.io.*;
import java.util.logging.Logger;

public class Execute {
    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

    private static final boolean EXECUTE_ONLY_ONCE = false;

    static {
        System.setOut(new PrintStream(new OutputStream() {
            @Override
            public void write(int b) {}
        }));

//        System.setErr(new PrintStream(new OutputStream() {
//            @Override
//            public void write(int b) {}
//        }));
    }

    public static void executeFunction(String filePath, String functionName) {
        MethodExecutor.process(filePath, functionName, CodejamUtils.DATASET, EXECUTE_ONLY_ONCE);
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            LOGGER.info(String.format("Running for %s" , args[0]));
            MethodExecutor.executeProblem(CodejamUtils.DATASET, args[0]);
        } else {
            LOGGER.info("Running for all");
            MethodExecutor.executeDataset(CodejamUtils.DATASET);
        }
    }

}
