package edu.ncsu.config;

import edu.ncsu.utils.Utils;

public class Properties {

    // File Paths

    /**
     * Home path
     */
    public static String HOME = System.getenv("HOME");

    /**
     * Parent folder of the main project source code
     */
    public static String ROOT_PATH = Utils.pathJoin(HOME, "Raise", "ProgramRepair");

    /**
     * Project main folder. Includes source code(code), codejam projects(projects) etc.
     */
    public static String CODESEER_HOME = Utils.pathJoin(ROOT_PATH, "CodeSeer");

    /**
     * Source code folder
     */
    public static String CODE_HOME = Utils.pathJoin(CODESEER_HOME, "code");

    /**
     * Projects folder
     */
    public static String PROJECTS_HOME = Utils.pathJoin(CODESEER_HOME, "projects");

    /**
     * Codejam projects folder
     */
    public static String CODEJAM_JAVA_FOLDER = Utils.pathJoin(PROJECTS_HOME, "src", "main", "java");

    /**
     * Meta-store folder
     */
    public static String META_STORE = Utils.pathJoin(CODE_HOME, "meta_store");

    /***
     * Codejam meta-store folder.
     */
    public static String CODEJAM_META_STORE = Utils.pathJoin(META_STORE, "codejam");

    /**
     * Codejam arguments folder
     */
    public static String CODEJAM_ARGUMENTS_FOLDER = Utils.pathJoin(CODEJAM_META_STORE, "arguments");

    /**
     *
     */
    public static String CODEJAM_FUNCTIONS_META_FOLDER = Utils.pathJoin(CODEJAM_META_STORE, "functions");

    /**
     * Codejam arguments index
     */
    public static String CODEJAM_ARGUMENTS_INDEX = Utils.pathJoin(CODEJAM_ARGUMENTS_FOLDER, "index.json");

    /**
     * Class objects folder
     */
    public static String CODEJAM_OBJECT_STORE = Utils.pathJoin(CODEJAM_META_STORE, "classes.json");

    /**
     * Meta-results folder
     */
    public static String META_RESULTS = Utils.pathJoin(CODE_HOME, "meta_results");

    /**
     * Meta-results folder
     */
    public static String CODEJAM_META_RESULTS = Utils.pathJoin(META_RESULTS, "codejam");


    // ************************************************************************************** //


    // Constants

    /**
     * Minimum statement size to consider
     */
    public static int MIN_STATEMENT_SIZE = 2;

    /**
     * Maximum array size
     */
    public static int MAX_ARRAY_SIZE = 100;
//    public static int MAX_ARRAY_SIZE = 5;

    /***
     * Number of arguments to generate while fuzzing
     */
    public static int FUZZ_ARGUMENT_SIZE = 256;
//    public static int FUZZ_ARGUMENT_SIZE = 3;

    /***
     * Three seconds
     */
    public static int THREE_SECS = 3 * 1000;

    /**
     * Generated class prefix
     */
    public static String GENERATED_CLASS_PREFIX = "generated_class_";

    /**
     * Generated function prefix
     */
    public static String GENERATED_FUNCTION_PREFIX = "func_";

    /**
     * Temporary class prefix
     */
    public static String TEMPORARY_CLASS_PREFIX = "temp_class_";

    /**
     * Number of threads for execution
     */
    public static int NUM_THREADS = 4;

    /**
     * Maximum wait time for execution
     */
    public final static int METHOD_EXECUTION_WAIT_TIME = 1;

    /**
     * Maximum wait time for all executions
     */
    public final static int ALL_METHOD_EXECUTIONS_WAIT_TIME = 5;

}
