package edu.ncsu.store.json;

import com.google.gson.*;
import edu.ncsu.utils.Utils;
import org.apache.commons.io.FileUtils;

import java.io.*;
import java.util.logging.Logger;

public class JSONDriver {

    private static Logger LOGGER = Logger.getLogger(JSONDriver.class.getName());

    public static JsonElement getJsonElement(String filePath) {
        JsonParser parser = new JsonParser();
        File storeFile = new File(filePath);
        JsonElement jsonElement;
        try {
            if (storeFile.exists()) {
                jsonElement = parser.parse(new FileReader(storeFile));
            } else {
                jsonElement = new JsonObject();
            }
        } catch (Exception e) {
            LOGGER.info(String.format("Error accessing: %s", filePath));
            throw new RuntimeException(e);
        }
        return jsonElement;
    }

    public static JsonObject getJsonObject(String filePath) {
        try {
            return getJsonElement(filePath).getAsJsonObject();
        } catch (RuntimeException e) {
            return new JsonObject();
        }
    }

    public static JsonArray getJsonArray(String filePath) {
        try {
            return getJsonElement(filePath).getAsJsonArray();
        } catch (RuntimeException e) {
            return new JsonArray();
        }
    }

    public static void saveJsonObject(JsonElement jsonElement, String filePath, boolean pretty) {
        GsonBuilder builder = new GsonBuilder().serializeSpecialFloatingPointValues();
        if (pretty) {
            builder.setPrettyPrinting();
        }
        Gson gson = builder.create();
        try(Writer writer = new FileWriter(filePath)) {
            writer.write(gson.toJson(jsonElement));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void saveObject(Object object, String filePath) {
        GsonBuilder builder = new GsonBuilder().serializeSpecialFloatingPointValues();
        Gson gson = builder.create();
        Utils.mkdir(Utils.getFolderPath(filePath));
        try(Writer writer = new FileWriter(filePath)) {
            writer.write(gson.toJson(object));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void deleteStore(String storePath) {
        File storeFile = new File(storePath);
        if (!Utils.fileExists(storePath))
            return;
        try {
            FileUtils.forceDelete(storeFile);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

}
