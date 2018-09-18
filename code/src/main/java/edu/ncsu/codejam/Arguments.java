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
        LOGGER.info(String.format("Number of java files: %d", javaFiles.size()));
        ConstantAdapter adapter;
        Map<Primitive, Set<Object>> constantsMap = new HashMap<>();
        Map<Primitive, Set<Object>> fileConstantsMap;
        for (String javaFile: javaFiles) {
            try {
                adapter = new ConstantAdapter(javaFile);
                fileConstantsMap = adapter.getConstantsMap();
                for(Primitive primitive: fileConstantsMap.keySet()) {
                    Set<Object> values = new HashSet<>();
                    if (constantsMap.containsKey(primitive)) {
                        values = constantsMap.get(primitive);
                    }
                    values.addAll(fileConstantsMap.get(primitive));
                    constantsMap.put(primitive, values);
                }
            } catch (Exception e) {
                LOGGER.severe(String.format("Failed to process : %s", javaFile));
                throw e;
            }
        }
        LOGGER.info("PRIOR TO SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
        ArgumentStore.savePrimitiveArguments(constantsMap);
        constantsMap = ArgumentStore.loadPrimitiveArguments();
        LOGGER.info("====================");
        LOGGER.info("POST SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
    }

    public static void storeRandomArgs() {
        StoreUtils.deleteStore(Properties.CODEJAM_ARGUMENTS_FOLDER);
        LOGGER.info("Generating random args. Here we go ....");
        List<String> javaFiles = CodejamUtils.listGeneratedFiles();
        for (String javaFile: javaFiles) {
            LOGGER.info(String.format("Running for %s", javaFile));
            generateForJavaFile(javaFile);
        }
    }

    private static void generateForJavaFile(String javaFile) {
        ArgumentStore store = ArgumentStore.loadArgumentStore();
        ClassMethods classMethods = new ClassMethods(javaFile);
        for (Method method: classMethods.getMethods()) {
            Function function = new Function(method, classMethods.getMethodBodies().get(method.getName()));
            if (!function.isValidArgs())
                continue;
            String key = function.makeArgumentsKey();
            if (!store.fuzzedKeyExists(key)) {
                LOGGER.info(String.format("Storing Key: %s", key));
                List<Object> arguments = ArgumentGenerator.generateArgumentsForFunction(function);
                store.saveFuzzedArguments(key, arguments);
            }
        }
    }

    public static void main(String[] args) {
//        extractAndStorePrimitiveArguments();
        storeRandomArgs();
//        generateForJavaFile("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Y11R5P1/Egor/generated_class_mini.java");
    }
}
