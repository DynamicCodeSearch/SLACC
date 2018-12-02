package edu.ncsu.store.mongo;

import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.util.JSON;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.IFunctionStore;
import org.bson.Document;

import java.util.List;
import java.util.Map;

public class FunctionStore implements IFunctionStore {

    protected String dataset;

    protected String getSuccessFunctionsCollection() {
        return "functions_executed";
    }

    protected String getFailedFunctionsCollection() {
        return "functions_failed";
    }

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
        updateFunction(result, getSuccessFunctionsCollection());
    }

    @Override
    public void updateFunctionError(JsonObject result) {
        updateFunction(result, getFailedFunctionsCollection());
    }

    private boolean isResult(Function function, Document document) {
        return document != null
                && document.get("name").toString().equals(function.getName())
                && document.get("class").toString().equals(function.getClassName())
                && document.get("package").toString().equals(function.getPackageName());
    }

    @Override
    public boolean isStored(Function function) {
        Document successFunction = getFunction(function.getName(), getSuccessFunctionsCollection());
        if (isResult(function, successFunction))
            return true;
        Document failedFunction = getFunction(function.getName(), getFailedFunctionsCollection());
        return isResult(function, failedFunction);
    }

    @Override
    public List<String> getExecutedFunctionNames(String language) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, "language_executed_functions");
        Document document = MongoDriver.getDocument(collection, "language", language);
        if (document != null && document.containsKey("names"))
            return (List<String>) document.get("names");
        return null;
    }

    public static void main(String[] args) {
        String jsonString = "{\"name\": Infinity}".replaceAll("(-)?Infinity", "NaN");
        Document document = new Document((Map<String, Object>) JSON.parse(jsonString));
        System.out.println(document.toJson());
//        FunctionStore store = new FunctionStore("codejam");
//        System.out.println(store.getExecutedFunctionNames("java"));
    }
}
