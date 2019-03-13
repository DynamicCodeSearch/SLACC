package edu.ncsu.mains;

import edu.ncsu.executors.MetadataExtractor;

import java.util.logging.Logger;

public class Metadata {

    private static final Logger LOGGER = Logger.getLogger(Metadata.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        MetadataExtractor.extractForDataset(dataset);
    }
}
