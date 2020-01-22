package edu.ncsu.config;

import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.introclass.IntroClassUtils;
import edu.ncsu.utils.Utils;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import java.util.regex.Pattern;

public class Settings {

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
    public static String CODESEER_HOME = Utils.pathJoin(ROOT_PATH, "SLACC");

    /**
     * Source code folder
     */
    public static String CODE_HOME = Utils.pathJoin(CODESEER_HOME, "code");

    /**
     * Projects folder
     */
    public static String PROJECTS_HOME = Utils.pathJoin(CODESEER_HOME, "projects");


    public static String SRC_MAIN_JAVA = Utils.pathJoin("src", "main", "java");

    /**
     * Folder for projects/src/main/java
     */
    public static String PROJECTS_JAVA_FOLDER = Utils.pathJoin(PROJECTS_HOME, SRC_MAIN_JAVA);

    /**
     * Codejam projects folder
     */
    public static String CODEJAM_JAVA_FOLDER = Utils.pathJoin(PROJECTS_JAVA_FOLDER, "CodeJam");

    /**
     * Introclass projects folder
     */
    public static String INTROCLASS_JAVA_FOLDER = Utils.pathJoin(PROJECTS_JAVA_FOLDER, "IntroClassJava");

    /**
     * Meta-store folder
     */
    public static String META_STORE = Utils.pathJoin(CODE_HOME, "meta_store");

    /**
     * Meta-results folder
     */
    public static String META_RESULTS = Utils.pathJoin(CODE_HOME, "meta_results");

    public static String META_RESULTS_SLOC = Utils.pathJoin(META_RESULTS, "sloc");

    /**
     * Resources folder
     */
    public static String CODE_RESOURCES_FOLDER = Utils.pathJoin(CODE_HOME, "src", "main", "resources");

    public static String CONFIG_FILE_PATH = Utils.pathJoin(CODE_HOME, "src", "main", "resources", "config.properties");


    // ************************************************************************************** //


    // Constants

    /**
     * Minimum statement size to consider
     */
    public static int MIN_STATEMENT_SIZE = 2;

    /***
     * Maximum number of arguments per function.
     */
    public static int MAX_NUM_ARGS = 3;

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

    public static int TEST_FUZZ_ARGUMENT_SIZE = FUZZ_ARGUMENT_SIZE * 5;

    /***
     * Three seconds
     */
    public static int THREE_SECS = 3 * 1000;

    /**
     * Generated class prefix
     */
    public static String GENERATED_CLASS_PREFIX = "generated_class_";

    /**
     * Generated class prefix
     */
    public static String PERMUTATED_CLASS_PREFIX = "permutated_class_";

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
    public static int NUM_THREADS = 1;

    /**
     * Maximum wait time for execution
     */
    public final static int METHOD_EXECUTION_WAIT_TIME = 1;

    /**
     * Maximum wait time for all executions
     */
    public final static int ALL_METHOD_EXECUTIONS_WAIT_TIME = 5;

    /**
     * Mongo storage
     */
    public final static String MONGO_STORAGE = "mongo";

    /**
     * Json storage
     */
    public final static String JSON_STORAGE = "json";

    // ************************************************************************************** //

    // Some property based functions

    public static String getObjectStore(String dataset) {
        return Utils.pathJoin(META_STORE, dataset, "classes.json");
    }

    public static String getMetaResultsFunctionsFolder(String dataset) {
        return Utils.pathJoin(META_RESULTS, dataset, "functions");
    }

    public static String getDatasetSourceFolder(String dataset) {
        if (dataset.equals(CodejamUtils.DATASET))
            return CODEJAM_JAVA_FOLDER;
        else if (dataset.equals(IntroClassUtils.DATASET))
            return INTROCLASS_JAVA_FOLDER;
        throw new RuntimeException(String.format("Illegal dataset: %s", dataset));
    }

    public static String getProperty(String property) {
        Properties properties = new Properties();
        InputStream stream;
        try {
            stream = new FileInputStream(CONFIG_FILE_PATH);
            properties.load(stream);
            return properties.getProperty(property);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String getScriptsFolder(String dataset) {
        if (dataset.equals(CodejamUtils.DATASET))
            return Utils.pathJoin("scripts", "codejam", "java");
        else if (dataset.equals(IntroClassUtils.DATASET))
            return Utils.pathJoin("scripts", "introclass");
        throw new RuntimeException(String.format("Illegal dataset: %s", dataset));
    }

    public static int getNumThreads() {
        String storage = getProperty("store");
        if (storage.equals(MONGO_STORAGE)) {
            return 4 * NUM_THREADS;
        } else if (storage.equals(JSON_STORAGE)) {
            return NUM_THREADS;
        }
        throw new RuntimeException(String.format("Unknown store: %s", storage));
    }

}
