package edu.ncsu.arguments;

import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IArgumentStore;
import edu.ncsu.visitors.adapters.ConstantAdapter;

import java.lang.reflect.Method;
import java.util.*;
import java.util.logging.Logger;

public class ArgumentExtractor {

    private final static Logger LOGGER = Logger.getLogger(ArgumentExtractor.class.getName());

    private String dataset;

    private IArgumentStore store;

    /***
     * Initialize Argument Extractor
     * @param dataset - Name of the dataset
     */
    public ArgumentExtractor(String dataset) {
        this(dataset, false);
    }


    public ArgumentExtractor(String dataset, Boolean isTest) {
        this.dataset = dataset;
        if (isTest) {
            this.store = BaseStorage.loadTestArgumentStore(dataset);
        } else {
            this.store = BaseStorage.loadArgumentStore(dataset);
        }
    }


    /**
     * Extract and store primitive arguments for a dataset.
     * @param javaFiles - List of paths fo java files.
     */
    public void extractAndStorePrimitiveArguments(List<String> javaFiles) {
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
        this.store.savePrimitiveArguments(constantsMap);
        constantsMap = this.store.loadPrimitiveArguments();
        LOGGER.info("====================");
        LOGGER.info("POST SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
    }

    /**
     * Generate arguments and save for the java file.
     * @param javaFile - Path of the java file.
     */
    public void generateForJavaFile(String javaFile, int numArgs) {
        ClassMethods classMethods = new ClassMethods(this.dataset, javaFile);
        for (Method method: classMethods.getMethods()) {
            Function function = new Function(this.dataset, method, classMethods.getMethodBodies().get(method.getName()), javaFile);
            if (!function.isValidArgs() || function.shouldBeSkipped())
                continue;
            String argKey = function.makeArgumentsKey();
            if (!this.store.fuzzedKeyExists(argKey)) {
                LOGGER.info(String.format("Storing Key: %s", argKey));
                List<Object> arguments = ArgumentGenerator.generateArgumentsForFunction(this.dataset, function, numArgs);
                if (arguments != null) {
                    this.store.saveFuzzedArguments(argKey, arguments);
                }
            }
//            List<String> argKeys = function.makeAllArgumentsKeys();
//            for (String key: argKeys) {
//                if (!this.store.fuzzedKeyExists(key)) {
//                    LOGGER.info(String.format("Storing Key: %s", key));
//                    List<Object> arguments = ArgumentGenerator.generateArgumentsForFunction(this.dataset, function, numArgs);
//                    if (arguments != null) {
//                        this.store.saveFuzzedArguments(key, arguments);
//                    }
//                }
//            }
        }
    }


    /**
     * Store fuzzed arguments for list of java files and dataset
     * @param javaFiles - List of path of java files
     */
    public void storeFuzzedArguments(List<String> javaFiles, int numArgs, boolean deleteOld) {
        LOGGER.info("Generating random args. Here we go ....");
        if (deleteOld) {
            LOGGER.info("Deleting old arguments ... ");
            store.deleteFuzzedArguments();
        } else  {
            LOGGER.info("Retaining old arguments ... ");
        }
        for (String javaFile: javaFiles) {
            LOGGER.info(String.format("Running for %s", javaFile));
            generateForJavaFile(javaFile, numArgs);
        }
    }

    private void testGenerateForJavaFile() {
        String javaFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Example/aditsu/generated_class_f70e39fe0ce54ddca9f8b5e72ebaa350.java";
        generateForJavaFile(javaFile, Settings.FUZZ_ARGUMENT_SIZE);
    }

    public static void main(String[] args) {
        ArgumentExtractor extractor = new ArgumentExtractor(CodejamUtils.DATASET);
        extractor.testGenerateForJavaFile();
    }
}
