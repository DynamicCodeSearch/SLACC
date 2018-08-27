package edu.ncsu.store;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.Primitive;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class ArgumentStore {

    public static final String PRIMITIVE_ARGUMENTS_STORE = Utils.pathJoin(Properties.CODEJAM_META_STORE, "primitive_arguments.json");

    private static final Logger LOGGER = Logger.getLogger(ArgumentStore.class.getName());

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
    public static synchronized void savePrimitiveArgumetns(Map<Primitive, Set<Object>> primitiveArguments) {
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

}
