package edu.ncsu;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length < 2) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 2. Arguments = %s",
                    Arrays.toString(args)));
        } else if (args[0].equals("CodeJam")) {
            switch (args[1]) {
                case "crawl":
                    edu.ncsu.codejam.Crawler.main(Arrays.copyOfRange(args, 2, args.length));
                    break;
                case "store_objects":
                    edu.ncsu.codejam.ClassStorage.main(args);
                    break;
                case "snip":
                    edu.ncsu.codejam.Snipper.main(Arrays.copyOfRange(args, 2, args.length));
                    break;
                case "extract_primitive_args":
                    edu.ncsu.codejam.Arguments.extractAndStorePrimitiveArguments();
                    break;
                case "extract_fuzzed_args":
                    edu.ncsu.codejam.Arguments.storeFuzzedArguments();
                    break;
                case "execute":
                    edu.ncsu.codejam.Execute.main(Arrays.copyOfRange(args, 2, args.length));
                    break;
                case "execute_single":
                    edu.ncsu.codejam.Execute.executeFunction(args[2], args[3]);
                    break;
                case "extract_metadata":
                    edu.ncsu.codejam.Metadata.extractMetadata();
                    break;
                default:
                    LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal second argument '%s'", args[1]));
                    break;
            }
        } else if (args[0].equals("IntroClass")) {
            switch (args[1]) {
                case "crawl":
                    edu.ncsu.introclass.Crawler.process();
                    break;
                case "store_objects":
                    edu.ncsu.introclass.ClassStorage.main(args);
                case "snip":
                    edu.ncsu.introclass.Snipper.main(Arrays.copyOfRange(args, 2, args.length));
                    break;
                case "extract_primitive_args":
                    edu.ncsu.introclass.Arguments.extractAndStorePrimitiveArguments();
                    break;
                case "extract_fuzzed_args":
                    edu.ncsu.introclass.Arguments.storeFuzzedArguments();
                    break;
                case "dead_code":
                    edu.ncsu.introclass.Clean.eliminateDeadCode();
                    break;
                default:
                    LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal second argument '%s'", args[1]));
                    break;
            }
        } else {
            LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal first argument '%s'", args[0]));
        }
        System.exit(0);
    }
}