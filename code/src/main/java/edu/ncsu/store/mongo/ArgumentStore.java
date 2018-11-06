package edu.ncsu.store.mongo;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.util.JSON;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.IArgumentStore;
import org.bson.Document;

import java.util.*;
import java.util.logging.Logger;

public class ArgumentStore implements IArgumentStore {

    private static final Logger LOGGER = Logger.getLogger(ArgumentStore.class.getName());

    private String dataset;

    private final static String PRIMITIVE_ARGS_COLLECTION = "primitive_args";

    private final static String FUZZED_ARGS_COLLECTION = "fuzzed_args";

    private ArgumentStore(String dataset) {
        this.dataset = dataset;
    }

    public static ArgumentStore loadStore(String dataset) {
        return new ArgumentStore(dataset);
    }


    @Override
    public void savePrimitiveArguments(Map<Primitive, Set<Object>> primitiveArguments) {
        LOGGER.info("Saving Primitive Arguments from MongoDB ... ");
        List<Document> documents = new ArrayList<>();
        for (Primitive primitive: primitiveArguments.keySet()) {
            Document document = new Document("type", primitive.getName())
                    .append("family", primitive.getFamily())
                    .append("args", primitiveArguments.get(primitive));
            documents.add(document);
        }
        if (documents.size() == 0)
            return;
        MongoDriver.dropCollection(this.dataset, PRIMITIVE_ARGS_COLLECTION);
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, PRIMITIVE_ARGS_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "type", "family");
        collection.insertMany(documents);
    }

    @Override
    public Map<Primitive, Set<Object>> loadPrimitiveArguments() {
        LOGGER.info("Loading Primitive Arguments from MongoDB ... ");
        Map<Primitive, Set<Object>> primitiveArguments = new HashMap<>();
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, PRIMITIVE_ARGS_COLLECTION);
        for (Document document: collection.find()) {
            Primitive primitive = Primitive.getPrimitiveByName(document.getString("type"));
            Set<Object> args = new HashSet<Object>((List) document.get("args"));
            primitiveArguments.put(primitive, args);
        }
        return primitiveArguments;
    }

    @Override
    public void saveFuzzedArguments(String key, Object arguments) {
        Document document = new Document("key", key)
                .append("args", arguments);
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUZZED_ARGS_COLLECTION);
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key");
        collection.insertOne(document);
    }


    private Document getFuzzed(String key) {
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, FUZZED_ARGS_COLLECTION);
        return collection.find(Filters.eq("key", key)).first();
    }

    @Override
    public boolean fuzzedKeyExists(String key) {
        return getFuzzed(key) != null;
    }

    @Override
    public JsonArray loadFuzzedArguments(String key) {
        Document document = getFuzzed(key);
        if (document == null)
            return null;
        return new Gson().fromJson(JSON.serialize(document.get("args")), JsonArray.class);
    }

    @Override
    public void deleteFuzzedArguments() {
        MongoDriver.dropCollection(this.dataset, FUZZED_ARGS_COLLECTION);
    }

    public static void main(String[] args) {
        ArgumentStore store = loadStore("codejam");
//        System.out.println(store.loadFuzzedArguments("int,int"));
        System.out.println(store.loadFuzzedArguments("float,(int)@1"));

    }


}
