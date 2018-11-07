package edu.ncsu.store.json;

import com.google.gson.*;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.store.IArgumentStore;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class ArgumentStore implements IArgumentStore {

    private static final Logger LOGGER = Logger.getLogger(ArgumentStore.class.getName());

    private String dataset;

    private static volatile Map<String, ArgumentStore> storeMap = new HashMap<>();

    private ArgumentStore(String dataset) {
        this.dataset = dataset;
    }

    public static ArgumentStore loadStore(String dataset) {
        if (!storeMap.containsKey(dataset)) {
            storeMap.put(dataset, new ArgumentStore(dataset));
        }
        return storeMap.get(dataset);
    }

    /**
     * Get path where primitive arguments are stored.
     * @return - File path
     */
    private String getPrimitiveArgStorePath() {
        return Utils.pathJoin(Settings.META_STORE, dataset, "primitive_arguments.json");
    }

    /**
     * Get path of folder containing the fuzzed arguments
     * @return - Folder path
     */
    private String getArgumentsFolder() {
        return Utils.pathJoin(Settings.META_STORE, dataset, "arguments");
    }


    /***
     * Get path of the index file of the fuzzed arguments
     * @return - Index Path
     */
    private String getArgumentsIndexPath() {
        return Utils.pathJoin(getArgumentsFolder(), "index.json");
    }


    // PRIMITIVE ARGUMENTS
    // ****************************************

    /**
     * Load Primitive Arguments
     * @return - Map of Primitive and Set of the arguments.
     */
    public synchronized Map<Primitive, Set<Object>> loadPrimitiveArguments() {
        LOGGER.info("Loading primitive arguments ... ");
        Map<Primitive, Set<Object>> primitiveArguments = new HashMap<>();
        try (Reader reader = new FileReader(getPrimitiveArgStorePath())) {
            Gson gson = new GsonBuilder().serializeSpecialFloatingPointValues().create();
            Map<String, Set<String>> gsonData = gson.fromJson(reader, new TypeToken<HashMap<String, Set<String>>>(){}.getType());
            for (String key: gsonData.keySet()) {
                Set<String> argStrings = gsonData.get(key);
                Set<Object> args = new HashSet<>();
                Primitive primitive = Primitive.getPrimitiveByName(key);
                for (String argString: argStrings)
                    args.add(Primitive.convertToArgument(primitive, argString));
                primitiveArguments.put(primitive, args);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return primitiveArguments;
    }

    /**
     * Save primitive arguments
     * @param primitiveArguments - Map of Primitive and Set of arguments.
     */
    public synchronized void savePrimitiveArguments(Map<Primitive, Set<Object>> primitiveArguments) {
        LOGGER.info("Saving primitive arguments ... ");
        Map<String, Set<Object>> gsonFriendlyArguments = new HashMap<>();
        for (Primitive primitive: primitiveArguments.keySet())
            gsonFriendlyArguments.put(primitive.getName(), primitiveArguments.get(primitive));
        JSONDriver.saveObject(gsonFriendlyArguments, getPrimitiveArgStorePath());
    }

    // FUZZED ARGUMENTS
    // ****************************************

    /**
     * Check if fuzzed key exists
     * @param key - Key to be checked
     * @return - True if key exists
     */
    public synchronized boolean fuzzedKeyExists(String key) {
        return loadFuzzedArgumentIndices().has(key);
    }

    /**
     * Save fuzzed arguments
     * @param key - Key to be saved to
     * @param arguments - Arguments to save
     */
    public synchronized void saveFuzzedArguments(String key, Object arguments) {
        Utils.mkdir(getArgumentsFolder());
        String indexKey = Utils.randomString();
        saveArgumentIndex(key, indexKey);
        String argsFile = Utils.pathJoin(getArgumentsFolder(), String.format("%s.json", indexKey));
        JSONDriver.saveObject(arguments, argsFile);
    }

    /**
     * Save Argument Index for a key and index
     * @param argKey - Argument key
     * @param indexKey - Index key
     */
    private void saveArgumentIndex(String argKey, String indexKey) {
        JsonObject jsonObject = loadFuzzedArgumentIndices();
        jsonObject.addProperty(argKey, indexKey);
        JSONDriver.saveJsonObject(jsonObject, getArgumentsIndexPath(), true);
    }

    /**
     * Load fuzzed argument indices
     * @return - Get a json object for codejam arguments.
     */
    private JsonObject loadFuzzedArgumentIndices() {
        return JSONDriver.getJsonObject(getArgumentsIndexPath());
    }

    /**
     * Load fuzzed arguments.
     * @param key - Argument key to load
     * @return - Array of fuzzed arguments.
     */
    public JsonArray loadFuzzedArguments(String key) {
        JsonObject index = loadFuzzedArgumentIndices();
        if (!index.has(key))
            return null;
        String indexKey = index.get(key).getAsString();
        String filePath = Utils.pathJoin(getArgumentsFolder(), String.format("%s.json", indexKey));
        return JSONDriver.getJsonArray(filePath);
    }

    /**
     * Delete fuzzed arguments
     */
    public void deleteFuzzedArguments() {
        JSONDriver.deleteStore(getArgumentsFolder());
    }

}
