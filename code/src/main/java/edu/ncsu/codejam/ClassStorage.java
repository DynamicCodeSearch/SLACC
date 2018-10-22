package edu.ncsu.codejam;

import edu.ncsu.store.ClassStore;

import java.util.logging.Logger;

public class ClassStorage {
    private static Logger LOGGER = Logger.getLogger(ClassStorage.class.getName());

    public static void main(String[] args) {
        ClassStore.store(CodejamUtils.DATASET);
    }
}
