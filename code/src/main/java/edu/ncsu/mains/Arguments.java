package edu.ncsu.mains;

import edu.ncsu.arguments.ArgumentExtractor;
import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;

import java.util.List;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());


    private static String getDataset(String... args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        return args[0];
    }

    private static  List<String> listGeneratedFiles(String dataset) {
        String datasetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        return Utils.listGeneratedFiles(datasetPath);
    }

    private static List<String> listPermutatedFiles(String dataset) {
        String datasetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        return Utils.listPermutatedFiles(datasetPath);
    }

    public static void extractAndStorePrimitiveArguments(String... args) {
        String dataset = getDataset(args);
        List<String> javaFiles = listGeneratedFiles(dataset);
        ArgumentExtractor extractor = new ArgumentExtractor(dataset);
        extractor.extractAndStorePrimitiveArguments(javaFiles);
    }

    public static void storeFuzzedArguments(String... args) {
        String dataset = getDataset(args);
        boolean deleteOld = false;
        if (args.length > 1) {
            deleteOld = Boolean.parseBoolean(args[1].toLowerCase().trim());
        }
        List<String> javaFiles = listPermutatedFiles(dataset);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = listGeneratedFiles(dataset);
        }
        ArgumentExtractor extractor = new ArgumentExtractor(dataset);
        extractor.storeFuzzedArguments(javaFiles, Settings.FUZZ_ARGUMENT_SIZE, deleteOld);
    }

    public static void storeTestFuzzedArguments(String... args) {
        String dataset = getDataset(args);
        List<String> javaFiles = listGeneratedFiles(dataset);
        ArgumentExtractor extractor = new ArgumentExtractor(dataset, true);
        extractor.storeFuzzedArguments(javaFiles, Settings.TEST_FUZZ_ARGUMENT_SIZE, true);
    }

}
