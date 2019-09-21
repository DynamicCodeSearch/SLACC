package edu.ncsu.store.mongo;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.mongodb.MongoClient;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.IndexOptions;
import com.mongodb.client.model.Indexes;
import com.mongodb.util.JSON;
import edu.ncsu.utils.Utils;
import org.bson.Document;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

public class MongoDriver {

    private static final Logger LOGGER = Logger.getLogger(MongoDriver.class.getName());

    private static final Logger mongoLogger = Logger.getLogger( "org.mongodb.driver" );

    private static Gson GSON = new GsonBuilder().serializeSpecialFloatingPointValues().create();

    private static MongoClient client = null;

    private final static JsonParser jsonParser = new JsonParser();

    static {
         mongoLogger.setLevel(Level.OFF);
    }

    private static String getDefaultHostName() {
        try {
            String hostName = InetAddress.getLocalHost().getHostName();
            return hostName;
        } catch (UnknownHostException e) {
            LOGGER.severe(String.format("Failed to fetch host name. Exception: %s", e.getMessage()));
            throw new RuntimeException(e);
        }
    }

    public static String getHostName() {
        String mongoHome = System.getenv("MONGO_HOME");
        if ( mongoHome != null && !mongoHome.isEmpty()) {
            String fileName = Utils.pathJoin(mongoHome, "host_machine.txt");
            String hostName = Utils.getFileContent(fileName);
            if (hostName != null && !hostName.isEmpty()) {
                return hostName;
            }
        }
        return getDefaultHostName();
    }

    public static MongoClient getClient() {
        if (client == null) {
            String hostName = MongoDriver.getHostName();
            client = new MongoClient(hostName);
        }
        try {
            client.getAddress();
        } catch (Exception e) {
            LOGGER.severe("Looks like client is down");
            client.close();
            client = null;
            throw new RuntimeException(e);
        }
        return client;
    }

    public static MongoDatabase getDatasetDB(String dataset) {
        if (dataset == null || dataset.isEmpty()) {
            throw new RuntimeException("Dataset is empty");
        }
        try {
            return getClient().getDatabase(dataset);
        } catch (NullPointerException e) {
            LOGGER.severe(String.format("Dataset '%s' does not exist. Creating this mongo manually " +
                    "and rerun the application. Don't forget to insert a dummy record.", dataset));
            throw e;
        }

    }

    public static MongoCollection<Document> getCollection(String dataset, String collectionName) {
        return getDatasetDB(dataset).getCollection(collectionName);
    }

    public static void createIndexForCollection(MongoCollection collection, String... fields) {
        IndexOptions indexOptions = new IndexOptions().unique(true);
        collection.createIndex(Indexes.ascending(fields), indexOptions);
    }

    public static boolean collectionExists(MongoCollection collection) {
        return collection != null && collection.count() > 0;
    }

    public static void dropCollection(String dataset, String collectionName) {
        getDatasetDB(dataset).getCollection(collectionName).drop();
    }

    public static Document getDocument(MongoCollection collection, String key, Object value) {
        return (Document) collection.find(Filters.eq(key, value)).first();
    }

    public static boolean containsDocument(MongoCollection collection, String key, Object value) {
        return getDocument(collection, key, value) != null;
    }

    public static void deleteDocument(MongoCollection collection, String key, Object value) {
        collection.deleteOne(Filters.eq(key, value));
    }


    public static Document parseAsDocument(JsonObject result) {
        String jsonString = GSON.toJson(result).trim().replaceAll("(-)?Infinity", "NaN");
        return new Document((Map<String, Object>) JSON.parse(jsonString));
    }

    public static JsonObject parseAsJson(Document document) {
        String jsonString = document.toJson();
        return jsonParser.parse(jsonString).getAsJsonObject();
    }

    public static void main(String[] args) {
        LOGGER.info(String.format("HostName of MongoD Server: %s", MongoDriver.getClient().getAddress().getHost()));
    }

}
