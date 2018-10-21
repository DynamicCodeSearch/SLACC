package edu.ncsu.store;

import com.google.gson.*;
import edu.ncsu.utils.Utils;

import java.io.*;

public class StoreUtils {

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

        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        return jsonElement;
    }

    public static JsonObject getJsonObject(String filePath) {
        return getJsonElement(filePath).getAsJsonObject();
    }

    public static JsonArray getJsonArray(String filePath) {
        return getJsonElement(filePath).getAsJsonArray();
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
        storeFile.delete();
    }

}
