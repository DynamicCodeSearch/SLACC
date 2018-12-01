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

    protected String dataset;

    private final static String PRIMITIVE_ARGS_COLLECTION = "primitive_args";

    private final static String FUZZED_ARGS_COLLECTION = "fuzzed_args";

    protected ArgumentStore(String dataset) {
        this.dataset = dataset;
    }

    public static ArgumentStore loadStore(String dataset) {
        return new ArgumentStore(dataset);
    }


    protected MongoCollection<Document> getFuzzedCollection() {
        return MongoDriver.getCollection(this.dataset, FUZZED_ARGS_COLLECTION);
    }

    private MongoCollection<Document> getPrimitiveCollection() {
        return MongoDriver.getCollection(this.dataset, PRIMITIVE_ARGS_COLLECTION);
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
        MongoCollection<Document> collection = getPrimitiveCollection();
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "type", "family");
        collection.insertMany(documents);
    }

    @Override
    public Map<Primitive, Set<Object>> loadPrimitiveArguments() {
        LOGGER.info("Loading Primitive Arguments from MongoDB ... ");
        Map<Primitive, Set<Object>> primitiveArguments = new HashMap<>();
        MongoCollection<Document> collection = getPrimitiveCollection();
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
        MongoCollection<Document> collection = getFuzzedCollection();
        if (!MongoDriver.collectionExists(collection))
            MongoDriver.createIndexForCollection(collection, "key");
        collection.insertOne(document);
    }


    private Document getFuzzed(String key) {
        MongoCollection<Document> collection = getFuzzedCollection();
        return collection.find(Filters.eq("key", key)).first();
    }

    @Override
    public boolean fuzzedKeyExists(String key) {
        MongoCollection<Document> collection = getFuzzedCollection();
        return MongoDriver.containsDocument(collection, "key", key);
    }

    @Override
    public JsonArray loadFuzzedArguments(String key) {
        MongoCollection<Document> collection = getFuzzedCollection();
        Document document = MongoDriver.getDocument(collection, "key", key);
        if (document == null)
            return null;
        return new Gson().fromJson(JSON.serialize(document.get("args")), JsonArray.class);
    }

    @Override
    public void deleteFuzzedArguments() {
        getFuzzedCollection().drop();
    }

    public static void main(String[] args) {
        ArgumentStore store = loadStore("codejam");
//        System.out.println(store.loadFuzzedArguments("int,int"));
        System.out.println(store.loadFuzzedArguments("float,(int)@1"));

    }


}
