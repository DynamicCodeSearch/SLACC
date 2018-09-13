package edu.ncsu.executors.helpers;

import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.store.ObjectStore;

import java.util.logging.Logger;

public class UserDefinedObjects {

    private static final Logger LOGGER = Logger.getLogger(UserDefinedObjects.class.getName());

    /**
     * Classes as JSONObject
     */
    private JsonObject objectsJSON;

    /**
     * Singleton instance of UserDefinedObjects
     */
    private static UserDefinedObjects userDefinedObjects;

    /**
     * Initialize UserDefinedObjects
     */
    private UserDefinedObjects() {
        this.objectsJSON = new ObjectStore(Properties.CODEJAM_OBJECT_STORE).getStore();
    }

    /**
     * @return - Create singleton instance of UserDefinedObjects
     */
    public static UserDefinedObjects getUserDefinedObjects() {
        if (userDefinedObjects == null)
            userDefinedObjects = new UserDefinedObjects();
        return userDefinedObjects;
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
