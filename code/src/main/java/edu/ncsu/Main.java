package edu.ncsu;

import edu.ncsu.crawler.CodeJamCrawler;

import java.util.Arrays;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {

    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) throws Exception{
        if (args.length < 1) {
            LOGGER.log(Level.SEVERE, String.format("Size of arguments is less than 0. Arguments = %s",
                    Arrays.toString(args)));
            System.exit(0);
        } else if (args[0].equals("crawl")) {
            CodeJamCrawler.main(Arrays.copyOfRange(args, 1, args.length));
        } else {
            LOGGER.log(Level.SEVERE, String.format("WTF!! Illegal first argument '%s'", args[0]));
        }

    }
}
