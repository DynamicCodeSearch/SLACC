package edu.ncsu.store.mongo;

public class ExtendedFunctionStore extends FunctionStore {

    protected String dataset;

    public ExtendedFunctionStore(String dataset) {
        super(dataset);
    }

    @Override
    protected String getSuccessFunctionsCollection() {
        return "test_functions_executed";
    }

    @Override
    protected String getFailedFunctionsCollection() {
        return "test_functions_failed";
    }

}
