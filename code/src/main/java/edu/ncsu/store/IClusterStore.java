package edu.ncsu.store;

import com.google.gson.JsonArray;

public interface IClusterStore {

    public JsonArray getClusters(String suffix);

}
