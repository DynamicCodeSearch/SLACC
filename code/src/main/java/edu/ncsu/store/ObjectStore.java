package edu.ncsu.store;

import com.google.gson.*;

import java.io.*;
import java.util.logging.Logger;

public class ObjectStore {

    private final static Logger LOGGER = Logger.getLogger(ObjectStore.class.getName());

    private String store_path;

    public ObjectStore(String store_path) {
        this.store_path = store_path;
        File storeFile = new File(store_path);
        if (!storeFile.getParentFile().exists())
            storeFile.getParentFile().mkdirs();
    }

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

    public synchronized void saveStore(JsonObject jsonObject) {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        try(FileWriter writer = new FileWriter(store_path)) {
            writer.write(gson.toJson(jsonObject));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


    public void saveClass(String packageName, String className, JsonArray imports, JsonArray variables, JsonArray parents) {
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
        packageObject.add(className, classObject);
        jsonObject.add(packageName, packageObject);
        saveStore(jsonObject);
    }

}
