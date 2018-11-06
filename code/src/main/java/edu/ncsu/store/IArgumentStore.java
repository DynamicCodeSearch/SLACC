package edu.ncsu.store;

import com.google.gson.JsonArray;
import edu.ncsu.executors.models.Primitive;

import java.util.Map;
import java.util.Set;

public interface IArgumentStore {

    public Map<Primitive, Set<Object>> loadPrimitiveArguments();

    public void savePrimitiveArguments(Map<Primitive, Set<Object>> primitiveArguments);

    public boolean fuzzedKeyExists(String key);

    public void saveFuzzedArguments(String key, Object arguments);

    public JsonArray loadFuzzedArguments(String key);

    public void deleteFuzzedArguments();

}
