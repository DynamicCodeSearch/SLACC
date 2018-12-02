package edu.ncsu.store;

import com.google.gson.JsonObject;
import edu.ncsu.executors.models.ClassMethods;

public interface IMetadataStore {

    public void saveClassFunctionsMetadata(JsonObject metadata, ClassMethods classMethods);

    public String getSourceFile(String dataset, String functionName);

}
