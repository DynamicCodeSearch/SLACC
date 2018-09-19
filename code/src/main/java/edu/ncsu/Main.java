package edu.ncsu;

import edu.ncsu.codejam.*;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 0. Arguments = %s",
                    Arrays.toString(args)));
        } else if (args[0].equals("crawl")) {
            Crawler.main(Arrays.copyOfRange(args, 1, args.length));
        } else if (args[0].equals("store_objects")) {
            ClassStore.main(args);
        } else if (args[0].equals("snip")) {
            Snipper.main(Arrays.copyOfRange(args, 1, args.length));
        } else if (args[0].equals("extract_primitive_args")) {
            Arguments.extractAndStorePrimitiveArguments();
        } else if (args[0].equals("extract_fuzzed_args")) {
            Arguments.storeRandomArgs();
        } else if (args[0].equals("execute")) {
            Execute.main(Arrays.copyOfRange(args, 1, args.length));
        } else {
            LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal first argument '%s'", args[0]));
        }
        System.exit(0);
    }
}