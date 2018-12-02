package edu.ncsu.store.json;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.IFunctionStore;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.util.List;

public class FunctionStore implements IFunctionStore {

    private String dataset;

    public FunctionStore(String dataset) {
        this.dataset = dataset;
    }

    private String getStoreFile(String packageName, String className) {
        String writeFolder = Utils.pathJoin(Settings.getMetaResultsFunctionsFolder(this.dataset),
                packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writeFolder);
        return Utils.pathJoin(writeFolder, String.format("%s.json", className));
    }

    private static boolean errorContainsFunction(JsonArray errors, String functionName) {
        for (JsonElement error: errors) {
            if (error.getAsJsonObject().get("name").getAsString().equals(functionName))
                return true;
        }
        return false;
    }

    private static JsonObject getContent(String storeFile) {
        JsonObject results;
        if (Utils.fileExists(storeFile)) {
            results = JSONDriver.getJsonObject(storeFile).getAsJsonObject();
        } else {
            results = new JsonObject();
        }
        return results;
    }

    @Override
    public synchronized void updateFunctionResult(JsonObject result) {
        String packageName = result.get("package").getAsString();
        String className = result.get("class").getAsString();
        String writeFile = getStoreFile(packageName, className);
        JsonObject results = getContent(writeFile);
        results.add(result.get("name").getAsString(), result);
        JSONDriver.saveJsonObject(results, writeFile, true);
    }

    @Override
    public void updateFunctionError(JsonObject result) {
        String packageName = result.get("package").getAsString();
        String className = result.get("class").getAsString();
        String writeFile = getStoreFile(packageName, className);
        JsonObject results = getContent(writeFile);
        JsonArray failedFunctions;
        if (results.has("errors")) {
            failedFunctions = results.get("errors").getAsJsonArray();
        } else {
            failedFunctions = new JsonArray();
        }
        if (!errorContainsFunction(failedFunctions, result.get("name").getAsString())) {
            failedFunctions.add(result);
            results.add("error", failedFunctions);
            JSONDriver.saveJsonObject(results, writeFile, true);
        }
    }

    @Override
    public boolean isStored(Function function) {
        JsonObject results = getContent(getStoreFile(function.getPackageName(), function.getClassName()));
        if (results.has(function.getName()))
            return true;
        if (!results.has("errors"))
            return false;
        return errorContainsFunction(results.getAsJsonArray("errors"), function.getName());
    }

    @Override
    public List<String> getExecutedFunctionNames(String language) {
        throw new RuntimeException("This method is not implemented for JSON. Check out Mongo.");
    }
}
