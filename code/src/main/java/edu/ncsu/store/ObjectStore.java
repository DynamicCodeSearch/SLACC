package edu.ncsu.store;

import com.google.gson.*;

import java.io.*;
import java.util.logging.Logger;

public class ObjectStore {

    private final static Logger LOGGER = Logger.getLogger(ObjectStore.class.getName());

    private String store_path;

    /**
     * Create instance of object store
     * @param store_path - Path of json object store
     */
    public ObjectStore(String store_path) {
        this.store_path = store_path;
        File storeFile = new File(store_path);
        if (!storeFile.getParentFile().exists())
            storeFile.getParentFile().mkdirs();
    }

    /**
     * @return - JSONObject of the store file.
     */
    public synchronized JsonObject getStore() {
        JsonParser parser = new JsonParser();
        File storeFile = new File(store_path);
        JsonObject jsonObject;
        try {
            if (storeFile.exists()) {
                jsonObject = (JsonObject) parser.parse(new FileReader(storeFile));
            } else {
                jsonObject = new JsonObject();
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        return jsonObject;
    }

    /**
     * Update json store file with contents of JSON object
     * @param jsonObject - JSONObject to update file.
     */
    public synchronized void saveStore(JsonObject jsonObject) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        try(FileWriter writer = new FileWriter(store_path)) {
            writer.write(gson.toJson(jsonObject));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    /**
     * Delete JSON file.
     * @return - Status of delete
     */
    public synchronized boolean deleteStore() {
        File storeFile = new File(store_path);
        return storeFile.delete();
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
