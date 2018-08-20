package edu.ncsu.config;

import edu.ncsu.utils.Utils;

public class Properties {

    public static String HOME = System.getenv("HOME");

    public static String ROOT_PATH = Utils.pathJoin(HOME, "Raise", "ProgramRepair");

    public static String PROJECT_HOME = Utils.pathJoin(ROOT_PATH, "CodeSeer");

    public static String CODE_HOME = Utils.pathJoin(PROJECT_HOME, "code");

    public static String CODEJAM_JAVA_FOLDER = Utils.pathJoin(PROJECT_HOME, "projects", "src", "main", "java");

    public static String META_STORE = Utils.pathJoin(CODE_HOME, "metastore");

    public static String CODEJAM_OBJECT_STORE = Utils.pathJoin(META_STORE, "codejam", "classes.json");

    public static int MIN_STATEMENT_SIZE = 2;

}
