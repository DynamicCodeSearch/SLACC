package edu.ncsu.codejam;

import edu.ncsu.arguments.ClassArgumentsExtractor;

import java.util.logging.Logger;

public class ClassStorage {
    private static Logger LOGGER = Logger.getLogger(ClassStorage.class.getName());

    public static void main(String[] args) {
        ClassArgumentsExtractor.store(CodejamUtils.DATASET);
    }
}
