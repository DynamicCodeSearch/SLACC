package edu.ncsu;

import edu.ncsu.mains.*;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length < 2) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 2. Arguments = %s",
                    Arrays.toString(args)));
        } else {
            switch (args[0]) {
                case "crawl":
                    Crawler.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "preprocess":
                    PreProcess.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "snip":
                    Snipper.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "permutate":
                    Permutate.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "dead_code":
                    DeadCode.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "store_objects":
                    ClassStorage.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "extract_primitive_args":
                    Arguments.extractAndStorePrimitiveArguments(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "extract_fuzzed_args":
                    Arguments.storeFuzzedArguments(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "extract_metadata":
                    Metadata.main(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "execute":
                    Execute.execute(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "execute_single":
                    // TODO: Change path of script and MethodExecutor.java to independent of dataset
                    Execute.executeFunction(Arrays.copyOfRange(args, 1, args.length));
                    break;
                // For Validating clusters
                case "test_extract_fuzzed_args":
                    Arguments.storeTestFuzzedArguments(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "test_reexecute_functions":
                    Execute.reExecuteFunctions(Arrays.copyOfRange(args, 1, args.length));
                    break;
                case "test_reexecute_single":
                    Execute.reExecuteFunction(Arrays.copyOfRange(args, 1, args.length));
                    break;
                default:
                    LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal argument '%s'", args[0]));
                    break;
            }
        }
    }

}
