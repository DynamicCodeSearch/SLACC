package edu.ncsu.executors.helpers;

import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.store.json.ClassStore;

import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

public class UserDefinedObjects {

    private static final Logger LOGGER = Logger.getLogger(UserDefinedObjects.class.getName());

    /**
     * Classes as JSONObject
     */
    private JsonObject objectsJSON;

    /**
     * Map of UserDefinedObjects
     */
    private static Map<String, UserDefinedObjects> userDefinedObjectsMap = new HashMap<>();

    /**
     * Initialize UserDefinedObjects
     */
    private UserDefinedObjects(String dataset) {
        this.objectsJSON = new ClassStore(dataset).getStore();
    }

    /**
     * @return - Create singleton instance of UserDefinedObjects
     */
    public static UserDefinedObjects getUserDefinedObjects(String dataset) {
        if (!userDefinedObjectsMap.containsKey(dataset))
            userDefinedObjectsMap.put(dataset, new UserDefinedObjects(dataset));
        return userDefinedObjectsMap.get(dataset);
    }

    /**
     * @return - Classes as JSON Object
     */
    public JsonObject getObjectsJSON() {
        return this.objectsJSON;
    }

    /**
     * Get Class Object from the JSON store
     * @param packageName - Name of the package
     * @param className - Name of the class
     * @return
     */
    public JsonObject getClassObject(String packageName, String className) {
        JsonObject packageObjects = objectsJSON.getAsJsonObject(packageName);
        if (packageObjects != null)
            return packageObjects.getAsJsonObject(className);
        return null;
    }

    /**
     * Check if class can be fuzzed.
     * @param classObject - JSONObject of class
     * @return - True if the classObject can generate arguments that can be fuzzed
     */
    public boolean canBeFuzzed(JsonObject classObject) {
        if (classObject == null)
            return false;
        return !classObject.get("isTemplate").getAsBoolean() && classObject.get("isValid").getAsBoolean();
    }

}
