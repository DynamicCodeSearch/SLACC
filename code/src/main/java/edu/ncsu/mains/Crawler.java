package edu.ncsu.mains;

import java.util.Arrays;
import java.util.logging.Logger;

public class Crawler {

    private static final Logger LOGGER = Logger.getLogger(Crawler.class.getName());

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0].trim().toLowerCase();
        if (dataset.equals("CodeJam".toLowerCase())) {
            LOGGER.info("Processing CodeJam ... ");
            edu.ncsu.codejam.Crawler.crawlMain(Arrays.copyOfRange(args, 1, args.length));
        } else if (dataset.equals("IntroClassJava".toLowerCase())) {
            LOGGER.info("Processing IntroClassJava ... ");
            edu.ncsu.introclass.Crawler.process();
        } else {
            LOGGER.severe(String.format("Crawler not defined for dataset: %s", args[0]));
        }
    }

}
