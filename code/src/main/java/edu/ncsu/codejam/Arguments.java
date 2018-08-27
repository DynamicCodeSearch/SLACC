package edu.ncsu.codejam;

import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.ArgumentStore;
import edu.ncsu.visitors.adapters.ConstantAdapter;

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
        ArgumentStore.savePrimitiveArgumetns(constantsMap);
        constantsMap = ArgumentStore.loadPrimitiveArguments();
        LOGGER.info("====================");
        LOGGER.info("POST SAVING !!!!");
        for (Primitive primitive: constantsMap.keySet()) {
            System.out.println(primitive + " : " + constantsMap.get(primitive).size());
        }
    }

    public static void main(String[] args) {
        extractAndStorePrimitiveArguments();
    }
}
