package edu.ncsu.introclass;

import edu.ncsu.store.ArgumentStore;

import java.util.List;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());

    public static void extractAndStorePrimitiveArguments() {
        LOGGER.info("Extracting primitive arguments from generated classes ... ");
        List<String> javaFiles = IntroClassUtils.listGeneratedFiles();
        ArgumentStore.extractAndStorePrimitiveArguments(javaFiles, IntroClassUtils.DATASET);
    }

    public static void storeFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        List<String> javaFiles = IntroClassUtils.listGeneratedFiles();
        ArgumentStore.storeFuzzedArguments(javaFiles, IntroClassUtils.DATASET);
    }

}
