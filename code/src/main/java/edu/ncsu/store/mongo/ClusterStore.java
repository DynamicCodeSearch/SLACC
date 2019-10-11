package edu.ncsu.store.mongo;

import com.google.gson.JsonArray;
import com.mongodb.client.MongoCollection;
import edu.ncsu.store.IClusterStore;
import org.bson.Document;

public class ClusterStore implements IClusterStore {

    private String dataset;

    public ClusterStore(String dataset) {
        this.dataset = dataset;
    }

    @Override
    public JsonArray getClusters(String suffix) {
        String collectionName = String.format("clusters_%s", suffix);
        MongoCollection<Document> collection = MongoDriver.getCollection(this.dataset, collectionName);
        JsonArray clusters = new JsonArray();
        for (Document document : collection.find())
            clusters.add(MongoDriver.parseAsJson(document));
        return clusters;
    }


}
