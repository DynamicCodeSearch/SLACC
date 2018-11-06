package edu.ncsu.introclass;

import edu.ncsu.arguments.ArgumentExtractor;

import java.util.List;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());

    private static ArgumentExtractor extractor = new ArgumentExtractor(IntroClassUtils.DATASET);

    public static void extractAndStorePrimitiveArguments() {
        LOGGER.info("Extracting primitive arguments from generated classes ... ");
        List<String> javaFiles = IntroClassUtils.listGeneratedFiles();
        extractor.extractAndStorePrimitiveArguments(javaFiles);
    }

    public static void storeFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        List<String> javaFiles = IntroClassUtils.listGeneratedFiles();
        extractor.storeFuzzedArguments(javaFiles);
    }

}
