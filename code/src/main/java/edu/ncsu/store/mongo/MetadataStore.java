package edu.ncsu.store.mongo;

import com.google.gson.JsonObject;
import com.mongodb.client.MongoCollection;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.store.IMetadataStore;
import org.bson.Document;

import java.lang.reflect.Method;
import java.util.logging.Logger;

public class MetadataStore implements IMetadataStore {

    private static final Logger LOGGER = Logger.getLogger(MetadataStore.class.getName());

    private static final String FUNCTION_METADATA_COLLECTION = "functions_metadata";

    @Override
    public void saveClassFunctionsMetadata(JsonObject metadata, ClassMethods classMethods) {
        LOGGER.info("Writing metadata in Mongo Database ... ");
        MongoCollection<Document> collection = MongoDriver.getCollection(classMethods.getDataset(), FUNCTION_METADATA_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "name");
        for (Method method: classMethods.getMethods()) {
            String functionName = classMethods.getFunction(method).getName();
            Document document = MongoDriver.parseAsDocument(metadata.getAsJsonObject(functionName));
            if (MongoDriver.containsDocument(collection, "name", functionName))
                MongoDriver.deleteDocument(collection, "name", functionName);
            collection.insertOne(document);
        }
    }

    @Override
    public String getSourceFile(String dataset, String functionName) {
        MongoCollection<Document> collection = MongoDriver.getCollection(dataset, FUNCTION_METADATA_COLLECTION);
        Document document = MongoDriver.getDocument(collection, "name", functionName);
        if (document == null)
            return null;
        return document.get("filePath").toString();
    }
}
