package edu.ncsu.mains;

import edu.ncsu.executors.MethodExecutor;

import java.io.OutputStream;
import java.io.PrintStream;
import java.util.logging.Logger;

public class Execute {

    private static final Logger LOGGER = Logger.getLogger(Execute.class.getName());

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

    public static void execute(String... args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        if (args.length > 1) {
            LOGGER.info(String.format("Running for problem: %s", args[1]));
            MethodExecutor.executeProblem(dataset, args[1]);
        } else {
            LOGGER.info("Running for all problems");
            MethodExecutor.executeDataset(dataset);
        }
    }

    public static void executeFunction(String... args) {
        if (args.length < 3) {
            LOGGER.severe("First Argument: Dataset, Second Argument: FilePath, Third Argument: FunctionName");
            System.exit(0);
        }
        String dataset = args[0];
        String filePath = args[1];
        String functionName = args[2];
        MethodExecutor.process(filePath, functionName, dataset, false);
    }

    public static void reExecuteFunctions(String... args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        MethodExecutor.reExecuteDataset(dataset);
    }

    public static void reExecuteFunction(String... args) {
        if (args.length < 3) {
            LOGGER.severe("First Argument: Dataset, Second Argument: FilePath, Third Argument: FunctionName");
            System.exit(0);
        }
        String dataset = args[0];
        String filePath = args[1];
        String functionName = args[2];
        MethodExecutor.process(filePath, functionName, dataset, true);
    }

}
