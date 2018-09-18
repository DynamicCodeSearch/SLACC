package edu.ncsu.store;

import com.google.gson.*;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.StringUtils;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class ArgumentStore {

    public static final String PRIMITIVE_ARGUMENTS_STORE = Utils.pathJoin(Properties.CODEJAM_META_STORE, "primitive_arguments.json");

    public static final String FUZZED_ARGUMENTS_STORE = Utils.pathJoin(Properties.CODEJAM_META_STORE, "fuzzed_arguments.json");

    private static final Logger LOGGER = Logger.getLogger(ArgumentStore.class.getName());


    private volatile Map<Primitive, Set<Object>> defaultPrimitiveArgs;

    private static volatile ArgumentStore argumentStore = null;

    private ArgumentStore() {
        defaultPrimitiveArgs = loadPrimitiveArguments();
    }

    public static ArgumentStore loadArgumentStore() {
        if (argumentStore == null) {
            argumentStore = new ArgumentStore();
        }
        return argumentStore;
    }

    // PRIMITIVE ARGUMENTS
    // ****************************************

    /**
     * Load Primitive Arguments
     * @return - Map of Primitive and Set of the arguments.
     */
    public static synchronized Map<Primitive, Set<Object>> loadPrimitiveArguments() {
        LOGGER.info("Loading primitive arguments ... ");
        Map<Primitive, Set<Object>> primitiveArguments = new HashMap<>();
        try (Reader reader = new FileReader(PRIMITIVE_ARGUMENTS_STORE)) {
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
    public static synchronized void savePrimitiveArguments(Map<Primitive, Set<Object>> primitiveArguments) {
        LOGGER.info("Saving primitive arguments ... ");
        Map<String, Set<Object>> gsonFriendlyArguments = new HashMap<>();
        for (Primitive primitive: primitiveArguments.keySet())
            gsonFriendlyArguments.put(primitive.getName(), primitiveArguments.get(primitive));
        StoreUtils.saveObject(gsonFriendlyArguments, PRIMITIVE_ARGUMENTS_STORE);
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
        Utils.mkdir(Properties.CODEJAM_ARGUMENTS_FOLDER);
        String indexKey = Utils.randomString();
        saveArgumentIndex(key, indexKey);
        String argsFile = Utils.pathJoin(Properties.CODEJAM_ARGUMENTS_FOLDER, String.format("%s.json", indexKey));
        StoreUtils.saveObject(arguments, argsFile);
    }

    /**
     * Save Argument Index for a key and index
     * @param argKey - Argument key
     * @param indexKey - Index key
     */
    private void saveArgumentIndex(String argKey, String indexKey) {
        JsonObject jsonObject = loadFuzzedArgumentIndices();
        jsonObject.addProperty(argKey, indexKey);
        StoreUtils.saveJsonObject(jsonObject, Properties.CODEJAM_ARGUMENTS_INDEX, true);
    }

    /**
     * Load fuzzed argument indices
     * @return - Get a json object for codejam arguments.
     */
    private JsonObject loadFuzzedArgumentIndices() {
        return StoreUtils.getJsonObject(Properties.CODEJAM_ARGUMENTS_INDEX);
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
        String filePath = Utils.pathJoin(Properties.CODEJAM_ARGUMENTS_FOLDER, String.format("%s.json", indexKey));
        return StoreUtils.getJsonArray(filePath);
    }

}
