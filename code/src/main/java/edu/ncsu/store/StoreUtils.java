package edu.ncsu.store;

import com.google.gson.*;

import java.io.*;

public class StoreUtils {

    public static JsonElement getJsonElement(String filePath) {
        JsonParser parser = new JsonParser();
        File storeFile = new File(filePath);
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
        try(Writer writer = new FileWriter(filePath)) {
            writer.write(gson.toJson(object));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}
