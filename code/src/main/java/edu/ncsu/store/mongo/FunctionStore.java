package edu.ncsu.store.mongo;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.util.JSON;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.IFunctionStore;
import org.bson.Document;

import java.util.Map;

public class FunctionStore implements IFunctionStore {

    private String dataset;

    private static final String SUCCESS_FUNCTIONS_COLLECTION = "functions_executed";

    private static final String FAILED_FUNCTIONS_COLLECTION = "functions_failed";

    public FunctionStore(String dataset) {
        this.dataset = dataset;
    }

    private void updateFunction(JsonObject result, String collectionName) {
        String functionName = result.get("name").getAsString();
        Document document = MongoDriver.parseAsDocument(result);
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, collectionName);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "name");
        if (MongoDriver.containsDocument(collection, "name", functionName))
            MongoDriver.deleteDocument(collection, "name", functionName);
        collection.insertOne(document);
    }

    private Document getFunction(String functionName, String collectionName) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, collectionName);
        if (!MongoDriver.collectionExists(collection))
            return null;
        return MongoDriver.getDocument(collection, "name", functionName);
    }

    @Override
    public void updateFunctionResult(JsonObject result) {
        updateFunction(result, SUCCESS_FUNCTIONS_COLLECTION);
    }

    @Override
    public void updateFunctionError(JsonObject result) {
        updateFunction(result, FAILED_FUNCTIONS_COLLECTION);
    }

    private boolean isResult(Function function, Document document) {
        return document != null
                && document.get("name").toString().equals(function.getName())
                && document.get("class").toString().equals(function.getClassName())
                && document.get("package").toString().equals(function.getPackageName());
    }

    @Override
    public boolean isStored(Function function) {
        Document successFunction = getFunction(function.getName(), SUCCESS_FUNCTIONS_COLLECTION);
        if (isResult(function, successFunction))
            return true;
        Document failedFunction = getFunction(function.getName(), FAILED_FUNCTIONS_COLLECTION);
        return isResult(function, failedFunction);
    }

    public static void main(String[] args) {
        String jsonString = "{\"name\": Infinity}".replaceAll("(-)?Infinity", "NaN");
        Document document = new Document((Map<String, Object>) JSON.parse(jsonString));
        System.out.println(document.toJson());
    }
}
