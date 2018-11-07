package edu.ncsu.store;

import com.google.gson.JsonObject;
import edu.ncsu.executors.models.Function;

public interface IFunctionStore {

    public void updateFunctionResult(JsonObject result);

    public void updateFunctionError(JsonObject result);

    public boolean isStored(Function function);

}
