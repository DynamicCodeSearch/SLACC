package edu.ncsu.mains;

import edu.ncsu.arguments.ClassArgumentsExtractor;

import java.util.Arrays;
import java.util.logging.Logger;

public class ClassStorage {
    private static Logger LOGGER = Logger.getLogger(ClassStorage.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        ClassArgumentsExtractor.store(dataset);
    }
}
