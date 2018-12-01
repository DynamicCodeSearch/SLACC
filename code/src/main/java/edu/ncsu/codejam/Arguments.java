package edu.ncsu.codejam;

import edu.ncsu.arguments.ArgumentExtractor;
import edu.ncsu.config.Settings;

import java.util.*;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());

    public static void extractAndStorePrimitiveArguments() {
        LOGGER.info("Extracting primitive arguments from generated classes ... ");
        ArgumentExtractor extractor = new ArgumentExtractor(CodejamUtils.DATASET);
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        extractor.extractAndStorePrimitiveArguments(javaFiles);
    }

    public static void storeFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        ArgumentExtractor extractor = new ArgumentExtractor(CodejamUtils.DATASET);
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        extractor.storeFuzzedArguments(javaFiles, Settings.FUZZ_ARGUMENT_SIZE);
    }

    public static void storeTestFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        ArgumentExtractor extractor = new ArgumentExtractor(CodejamUtils.DATASET, true);
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        extractor.storeFuzzedArguments(javaFiles, Settings.TEST_FUZZ_ARGUMENT_SIZE);
    }

    public static void main(String[] args) {
//        extractAndStorePrimitiveArguments();
//        storeRandomArgs();
//        ArgumentStore.generateForJavaFile("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Egor/generated_class_mini.java");
        storeTestFuzzedArguments();
    }
}
