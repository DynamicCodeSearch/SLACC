package edu.ncsu.store;

import edu.ncsu.config.Settings;

public class BaseStorage {

    private final static String STORAGE = Settings.getProperty("store");

    public static IArgumentStore loadArgumentStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return edu.ncsu.store.mongo.ArgumentStore.loadStore(dataset);
            case Settings.JSON_STORAGE:
                return edu.ncsu.store.json.ArgumentStore.loadStore(dataset);
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IFunctionStore loadFunctionStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.FunctionStore(dataset);
            case Settings.JSON_STORAGE:
                return new edu.ncsu.store.json.FunctionStore(dataset);
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IMetadataStore loadMetadataStore() {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.MetadataStore();
            case Settings.JSON_STORAGE:
                return new edu.ncsu.store.json.MetadataStore();
            default:
                throw new RuntimeException(String.format("Unknown store: %s", STORAGE));
        }
    }

    public static IArgumentStore loadTestArgumentStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return edu.ncsu.store.mongo.ExtendedArgumentStore.loadStore(dataset);
            default:
                throw new RuntimeException("Test storage supported only for mongo");
        }
    }

    public static IFunctionStore loadTestFunctionStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.ExtendedFunctionStore(dataset);
            default:
                throw new RuntimeException("Test storage supported only for mongo");
        }
    }

    public static IClusterStore loadClusterStore(String dataset) {
        switch (STORAGE) {
            case Settings.MONGO_STORAGE:
                return new edu.ncsu.store.mongo.ClusterStore(dataset);
            default:
                throw new RuntimeException("Test storage supported only for mongo");
        }
    }

}
