package edu.ncsu.arguments;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.config.Settings;
import edu.ncsu.store.json.ClassStore;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.ObjectStoreAdapter;
import edu.ncsu.visitors.blocks.Type;
import edu.ncsu.visitors.blocks.Variable;

import java.util.logging.Logger;

public class ClassArgumentsExtractor {

    private static final Logger LOGGER = Logger.getLogger(ClassArgumentsExtractor.class.getName());

    private String dataset;

    private String datasetSourceFolder;

    private ClassStore classStore;

    public ClassArgumentsExtractor(String dataset) {
        this.dataset = dataset;
        this.classStore = new ClassStore(this.dataset);
        this.datasetSourceFolder = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, this.dataset);
    }

    private void storeClasses() {
        for (String problem: Utils.listDir(datasetSourceFolder)) {
            String problemDir = Utils.pathJoin(datasetSourceFolder, problem);
            for (String user: Utils.listDir(problemDir)) {
                String userDir = Utils.pathJoin(problemDir, user);
                for (String javaFile: Utils.listNonGeneratedJavaFiles(userDir)) {
                    LOGGER.info(String.format("Processing: %s", javaFile));
                    new ObjectStoreAdapter(javaFile).storeClasses(this.classStore);
                }
            }
        }
    }

    private void markClasses() {
        LOGGER.info("Marking the saved JSON as valid/invalid");
        JsonObject store = classStore.getStore();
        for (String packageName: store.keySet()) {
            JsonObject packageObject = store.getAsJsonObject(packageName);
            for (String className: packageObject.keySet()) {
                getClassJSON(store, packageName, className);
            }
        }
        classStore.saveStore(store);
    }

    private JsonObject getClassJSON(JsonObject store, String packageName, String className) {
        JsonObject packageObject = store.getAsJsonObject(packageName);
        JsonObject classObject = packageObject.getAsJsonObject(className);
        if (classObject == null) {
            return null;
        }
        if (classObject.has("isValid")) {
            return classObject;
        }
        JsonArray parents = classObject.getAsJsonArray("parents");
        JsonArray variables = classObject.getAsJsonArray("variables");
        JsonArray constructors = classObject.getAsJsonArray("constructors");
        if (parents != null) {
            for (JsonElement parent: parents) {
                JsonObject parentJSON = getClassJSON(store, packageName, parent.toString());
                if (parentJSON == null || !parentJSON.has("isValid") || !Boolean.parseBoolean(parentJSON.get("isValid").toString())) {
                    classObject.addProperty("isValid", false);
                    packageObject.add(className, classObject);
                    store.add(packageName, packageObject);
                    return classObject;
                }
                JsonArray parentVariables = parentJSON.getAsJsonArray("variables");
                if (parentVariables != null && parentVariables.size() > 0) {
                    for (JsonElement variable: parentJSON.getAsJsonArray()) {
                        JsonObject variableJSON = variable.getAsJsonObject();
                        if (!variableJSON.get("scope").toString().equals(Variable.PRIVATE)){
                            variables.add(variableJSON);
                        }
                    }
                }
            }
        }
        classObject.add("variables", variables);
        boolean isValid = true;
        for (JsonElement variable: variables) {
            JsonObject variableJSON = variable.getAsJsonObject();
            String type = variableJSON.get("type").getAsString();
            if (!isValidType(store, packageName, type)) {
                isValid = false;
                break;
            }
        }
        JsonArray updatedConstructors = new JsonArray();
        if (constructors != null && constructors.size() > 0) {
            boolean hasOneValidConstructor = false;
            for (JsonElement constructor: constructors) {
                boolean isValidConstructor = true;
                JsonObject constructorJSON = constructor.getAsJsonObject();
                String scope = constructorJSON.get("scope").getAsString();
                if (scope.equals(Variable.PUBLIC) || scope.equals(Variable.DEFAULT)) {
                    for (JsonElement variable: constructorJSON.getAsJsonArray("parameters")) {
                        JsonObject variableJSON = variable.getAsJsonObject();
                        String type = variableJSON.get("type").getAsString();
                        if (!isValidType(store, packageName, type)) {
                            isValidConstructor = false;
                            break;
                        }
                    }
                } else {
                    isValidConstructor = false;
                }
                if (isValidConstructor)
                    hasOneValidConstructor = true;
                constructorJSON.addProperty("isValid", isValidConstructor);
                updatedConstructors.add(constructorJSON);
            }
            isValid = isValid && hasOneValidConstructor;
        }
        classObject.add("constructors", updatedConstructors);
        classObject.addProperty("isValid", isValid);
        packageObject.add(className, classObject);
        store.add(packageName, packageObject);
        return classObject;
    }

    private boolean isValidType(JsonObject store, String packageName, String type) {
        JsonObject typeObject = getClassJSON(store, packageName, type);
        boolean isValid = true;
        if (typeObject != null) {
            if (!Boolean.parseBoolean(typeObject.get("isValid").toString())) {
                isValid = false;
            }
        }
        // TODO: Check here for List, Set, Map etc.
        else if (!Type.isValidType(type)) {
            isValid = false;
        }
        return isValid;
    }

    public static void testStore(String dataset) {
//        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/aditsu/Cakes.java";
        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/stupid/Dummy.java";
        ClassArgumentsExtractor classArgumentsExtractor = new ClassArgumentsExtractor(dataset);
        classArgumentsExtractor.classStore.deleteStore();
        LOGGER.info(String.format("Processing: '%s'", fileName));
        new ObjectStoreAdapter(fileName).storeClasses(classArgumentsExtractor.classStore);
        classArgumentsExtractor.markClasses();
    }

    public static void store(String dataset) {
        ClassArgumentsExtractor classArgumentsExtractor = new ClassArgumentsExtractor(dataset);
        classArgumentsExtractor.classStore.deleteStore();
        classArgumentsExtractor.storeClasses();
        classArgumentsExtractor.markClasses();
    }

    public static void main(String[] args) {
        store("IntroClassJava");
    }

}
