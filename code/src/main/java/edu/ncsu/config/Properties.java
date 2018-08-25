package edu.ncsu.config;

import edu.ncsu.utils.Utils;

public class Properties {

    public static String HOME = System.getenv("HOME");

    public static String ROOT_PATH = Utils.pathJoin(HOME, "Raise", "ProgramRepair");

    public static String CODESEER_HOME = Utils.pathJoin(ROOT_PATH, "CodeSeer");

    public static String CODE_HOME = Utils.pathJoin(CODESEER_HOME, "code");

    public static String PROJECTS_HOME = Utils.pathJoin(CODESEER_HOME, "projects");

    public static String CODEJAM_JAVA_FOLDER = Utils.pathJoin(PROJECTS_HOME, "src", "main", "java");

    public static String META_STORE = Utils.pathJoin(CODE_HOME, "meta_store");

    public static String CODEJAM_OBJECT_STORE = Utils.pathJoin(META_STORE, "codejam", "classes.json");

    public static String META_RESULTS = Utils.pathJoin(CODE_HOME, "meta_results");

    public static int MIN_STATEMENT_SIZE = 2;

}
