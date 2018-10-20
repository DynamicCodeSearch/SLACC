package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.executors.ArgumentGenerator;
import edu.ncsu.executors.MethodExecutor;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.store.StoreUtils;
import edu.ncsu.visitors.adapters.ConstantAdapter;

import java.lang.reflect.Method;
import java.util.*;
import java.util.logging.Logger;

public class Arguments {

    private static final Logger LOGGER = Logger.getLogger(Arguments.class.getName());

    public static void extractAndStorePrimitiveArguments() {
        LOGGER.info("Extracting primitive arguments from generated classes ... ");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        ArgumentStore.extractAndStorePrimitiveArguments(javaFiles, CodejamUtils.DATASET);
    }

    public static void storeFuzzedArguments() {
        LOGGER.info("Extracting fuzzed arguments from generated classes ... ");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        ArgumentStore.storeFuzzedArguments(javaFiles, CodejamUtils.DATASET);
        ArgumentStore.loadArgumentStore(CodejamUtils.DATASET).deleteFuzzedArguments();
    }

    public static void main(String[] args) {
//        extractAndStorePrimitiveArguments();
//        storeRandomArgs();
        ArgumentStore.generateForJavaFile("codejam", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Egor/generated_class_mini.java");
    }
}
