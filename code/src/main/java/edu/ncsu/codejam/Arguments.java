package edu.ncsu.codejam;

import edu.ncsu.arguments.ArgumentExtractor;

import java.util.*;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());

    private static ArgumentExtractor extractor = new ArgumentExtractor(CodejamUtils.DATASET);

    public static void extractAndStorePrimitiveArguments() {
        LOGGER.info("Extracting primitive arguments from generated classes ... ");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        extractor.extractAndStorePrimitiveArguments(javaFiles);
    }

    public static void storeFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        extractor.storeFuzzedArguments(javaFiles);
    }

    public static void main(String[] args) {
//        extractAndStorePrimitiveArguments();
//        storeRandomArgs();
//        ArgumentStore.generateForJavaFile("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Egor/generated_class_mini.java");
        storeFuzzedArguments();
    }
}
