package edu.ncsu.visitors.blocks;

public class ImportBlock {
    /***
     * Qualifier for the import. eg. java.util
     */
    private String qualifier;

    /***
     * Name of the import. ef. Queue
     */
    private String name;

    /**
     * Get the qualifier name.
     * @return qualifier
     */
    public String getQualifier() {
        return qualifier;
    }

    /**
     * Get the name of the media.
     * @return name
     */
    public String getName() {
        return name;
    }
}
