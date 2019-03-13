package edu.ncsu.mains;

import java.util.logging.Logger;

public class DeadCode {

    private static Logger LOGGER = Logger.getLogger(DeadCode.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        edu.ncsu.preprocess.DeadCode.clean(dataset);
    }

}
