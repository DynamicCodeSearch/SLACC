package edu.ncsu.store.mongo;

import com.mongodb.client.MongoCollection;
import org.bson.Document;

public class ExtendedArgumentStore extends ArgumentStore {

    private final static String FUZZED_ARGS_COLLECTION = "test_fuzzed_args";

    private ExtendedArgumentStore(String dataset) {
        super(dataset);
    }

    public static ExtendedArgumentStore loadStore(String dataset) {
        return new ExtendedArgumentStore(dataset);
    }

    @Override
    protected MongoCollection<Document> getFuzzedCollection() {
        return MongoDriver.getCollection(this.dataset, FUZZED_ARGS_COLLECTION);
    }

}
