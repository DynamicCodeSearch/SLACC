package edu.ncsu.store;

import com.google.gson.JsonObject;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.visitors.blocks.GeneratedFunction;

import java.util.List;

public interface IMetadataStore {

    public void saveClassFunctionsMetadata(JsonObject metadata, ClassMethods classMethods);

    public void saveClassFunctionsMetadata(String dataset, List<JsonObject> generatedFunctions);

    public JsonObject getFunctionMetadata(String dataset, String functionName);

    public String getSourceFile(String dataset, String functionName);

}
