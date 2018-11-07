package edu.ncsu.store.mongo;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import com.mongodb.util.JSON;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.store.IMetadataStore;
import org.bson.Document;

import java.lang.reflect.Method;
import java.util.Map;
import java.util.logging.Logger;

public class MetadataStore implements IMetadataStore {

    private static final Logger LOGGER = Logger.getLogger(MetadataStore.class.getName());

    private static final String FUNCTION_METADATA_COLLECTION = "functions_metadata";

    @Override
    public void saveClassFunctionsMetadata(JsonObject metadata, ClassMethods classMethods) {
        LOGGER.info("Writing metadata in Mongo Database ... ");
        Gson gson = new Gson();
        MongoCollection<Document> collection = MongoDriver.getCollection(classMethods.getDataset(), FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "name");
        for (Method method: classMethods.getMethods()) {
            String functionName = classMethods.getFunction(method).getName();
            JsonObject functionMetadata = metadata.getAsJsonObject(functionName);
            String jsonString = gson.toJson(functionMetadata);
            Document document = new Document((Map<String, Object>) JSON.parse(jsonString));
            if (MongoDriver.containsDocument(collection, "name", functionName))
                MongoDriver.deleteDocument(collection, "name", functionName);
            collection.insertOne(document);
        }
    }
}
