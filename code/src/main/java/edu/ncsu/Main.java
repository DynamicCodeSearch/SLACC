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
            if (args[1].equals("crawl")) {
                edu.ncsu.codejam.Crawler.main(Arrays.copyOfRange(args, 2, args.length));
            } else if (args[1].equals("store_objects")) {
                edu.ncsu.codejam.ClassStore.main(args);
            } else if (args[1].equals("snip")) {
                edu.ncsu.codejam.Snipper.main(Arrays.copyOfRange(args, 2, args.length));
            } else if (args[1].equals("extract_primitive_args")) {
                edu.ncsu.codejam.Arguments.extractAndStorePrimitiveArguments();
            } else if (args[1].equals("extract_fuzzed_args")) {
                edu.ncsu.codejam.Arguments.storeRandomArgs();
            } else if (args[1].equals("execute")) {
                edu.ncsu.codejam.Execute.main(Arrays.copyOfRange(args, 2, args.length));
            } else if (args[1].equals("execute_single")) {
                edu.ncsu.codejam.Execute.executeFunction(args[2], args[3]);
            } else if (args[1].equals("extract_metadata")) {
                edu.ncsu.codejam.Metadata.extractMetadata();
            } else {
                LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal second argument '%s'", args[1]));
            }
        } else if (args[0].equals("IntroClass")) {
            if (args[1].equals("crawl")) {
                edu.ncsu.introclass.Crawler.process();
            } else if (args[1].equals("snip")) {
                edu.ncsu.introclass.Snipper.main(Arrays.copyOfRange(args, 2, args.length));
            } else {
                LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal second argument '%s'", args[1]));
            }
        } else {
            LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal first argument '%s'", args[0]));
        }
        System.exit(0);
    }
}