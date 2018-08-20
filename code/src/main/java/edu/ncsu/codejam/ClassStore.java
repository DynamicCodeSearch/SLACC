package edu.ncsu.codejam;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.store.ObjectStore;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.ObjectStoreAdapter;
import edu.ncsu.visitors.blocks.Type;

import java.util.logging.Logger;

public class ClassStore {

    private static final Logger LOGGER = Logger.getLogger(ClassStore.class.getName());

    private static final ObjectStore objectStore = new ObjectStore(Properties.CODEJAM_OBJECT_STORE);

    private static void storeClasses() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            for (String user: Utils.listDir(problemDir)) {
                String userDir = Utils.pathJoin(problemDir, user);
                for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                    LOGGER.info(String.format("Processing: %s", javaFile));
                    new ObjectStoreAdapter(javaFile).storeClasses(objectStore);
                }
            }
        }
    }

    private static void markClasses() {
        LOGGER.info("Marking the saved JSON as valid/invalid");
        JsonObject store = objectStore.getStore();
        for (String packageName: store.keySet()) {
            JsonObject packageObject = store.getAsJsonObject(packageName);
            for (String className: packageObject.keySet()) {
                getClassJSON(store, packageName, className);
            }
        }
        objectStore.saveStore(store);
    }

    private static JsonObject getClassJSON(JsonObject store, String packageName, String className) {
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
                        if (!variableJSON.get("scope").toString().equals("private")){
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
            JsonObject typeObject = getClassJSON(store,  packageName, type);
            if (typeObject != null) {
                if (!Boolean.parseBoolean(typeObject.get("isValid").toString())) {
                    isValid = false;
                    break;
                }
            } else if (!Type.isValidType(type)) {
                isValid = false;
                break;
            }

        }
        classObject.addProperty("isValid", isValid);
        packageObject.add(className, classObject);
        store.add(packageName, packageObject);
        return classObject;
    }

    public static void main(String[] args) {
        storeClasses();
        markClasses();
    }

}
