package edu.ncsu.store.json;

import com.google.gson.*;
import edu.ncsu.config.Settings;
import edu.ncsu.store.StoreUtils;

import java.io.*;
import java.util.logging.Logger;

public class ClassStore {

    private final static Logger LOGGER = Logger.getLogger(ClassStore.class.getName());

    private String storePath;

    /**
     * Create instance of object store
     * @param dataset - Name of the dataset
     */
    public ClassStore(String dataset) {
        this.storePath = Settings.getObjectStore(dataset);
        File storeFile = new File(storePath);
        if (!storeFile.getParentFile().exists())
            storeFile.getParentFile().mkdirs();
    }

    /**
     * @return - JSONObject of the store file.
     */
    public synchronized JsonObject getStore() {
        return StoreUtils.getJsonObject(storePath);
    }

    /**
     * Update json store file with contents of JSON object
     * @param jsonObject - JSONObject to update file.
     */
    public synchronized void saveStore(JsonObject jsonObject) {
        StoreUtils.saveJsonObject(jsonObject, storePath, true);
    }

    /**
     * Delete JSON file.
     * @return - Status of delete
     */
    public synchronized void deleteStore() {
        StoreUtils.deleteStore(storePath);
    }

    /***
     * Update class in the json store
     * @param packageName - Name of the package
     * @param className - Name of the class
     * @param imports - List of imports
     * @param variables - List of variables
     * @param parents - List of parent classes(extends, implements)
     * @param constructors - List of constructors
     * @param isTemplate - True if className is interface or abstract class
     */
    public void saveClass(String packageName, String className, JsonArray imports, JsonArray variables,
                          JsonArray parents, JsonArray constructors, boolean isTemplate) {
        LOGGER.info(String.format("Saving class : %s.%s", packageName, className));
        JsonObject jsonObject = getStore();
        JsonObject packageObject = jsonObject.getAsJsonObject(packageName);
        if (packageObject == null) {
            packageObject = new JsonObject();
        }
        JsonObject classObject = new JsonObject();
        classObject.addProperty("name", className);
        classObject.addProperty("package", packageName);
        classObject.add("imports", imports);
        classObject.add("variables", variables);
        classObject.add("parents", parents);
        classObject.add("constructors", constructors);
        classObject.addProperty("isTemplate", isTemplate);
        packageObject.add(className, classObject);
        jsonObject.add(packageName, packageObject);
        saveStore(jsonObject);
    }

}
