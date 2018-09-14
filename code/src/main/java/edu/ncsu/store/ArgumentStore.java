package edu.ncsu.store;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Properties;
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

    private volatile Map<String, Object> cache;

    private volatile Map<Primitive, Set<Object>> defaultPrimitiveArgs;

    private static volatile ArgumentStore argumentStore = null;

    private ArgumentStore() {
        cache = loadFromJSONFile();
        defaultPrimitiveArgs = loadPrimitiveArguments();
    }

    public static ArgumentStore loadArgumentStore() {
        if (argumentStore == null) {
            argumentStore = new ArgumentStore();
        }
        return argumentStore;
    }

    public synchronized boolean fuzzedKeyExists(String key) {
        return cache.containsKey(key);
    }

    public synchronized void saveFuzzedArguments(String key, Object arguments) {
        cache.put(key, arguments);
        try(Writer writer = new FileWriter(FUZZED_ARGUMENTS_STORE)) {
            Gson gson = new GsonBuilder().create();
            gson.toJson(cache, writer);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

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
        try (Writer writer = new FileWriter(PRIMITIVE_ARGUMENTS_STORE)) {
            Map<String, Set<Object>> gsonFriendlyArguments = new HashMap<>();
            for (Primitive primitive: primitiveArguments.keySet())
                gsonFriendlyArguments.put(primitive.getName(), primitiveArguments.get(primitive));
            Gson gson = new GsonBuilder().serializeSpecialFloatingPointValues().create();
            gson.toJson(gsonFriendlyArguments, writer);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private static synchronized Map<String, Object> loadFromJSONFile() {
        Map<String, Object> cache = new HashMap<>();
        File jsonFile = new File(FUZZED_ARGUMENTS_STORE);
        if (!jsonFile.exists())
            return cache;
        try (Reader reader = new FileReader(FUZZED_ARGUMENTS_STORE)){
            Gson gson = new GsonBuilder().create();
            Map<String, Object> gsonData = gson.fromJson(reader, new TypeToken<HashMap<String, Object>>(){}.getType());
            cache = gsonData;
            for (String key: gsonData.keySet()) {
                if (StringUtils.isEmpty(key))
                    continue;
//                List<DataType> dataTypes = new ArrayList<>();
//                for (String dataTypeName: Arrays.asList(key.split("\\s*,\\s*")))
//                    dataTypes.add(DataType.getDataTypeByName(dataTypeName));
//                cache.put(key, ArgumentGenerator.convertToArguments(dataTypes, gsonData.get(key)));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return cache;
    }

}
