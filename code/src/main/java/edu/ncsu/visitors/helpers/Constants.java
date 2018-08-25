package edu.ncsu.visitors.helpers;

import java.util.HashSet;
import java.util.Set;

public class Constants {

    public final static Set<String> IGNORES = new HashSet<>();

    public final static Set<String> PERMITTED_CLASSES = new HashSet<>();

    static  {
        PERMITTED_CLASSES.add("String");
        PERMITTED_CLASSES.add("Integer");
        PERMITTED_CLASSES.add("Long");
        PERMITTED_CLASSES.add("Float");
        PERMITTED_CLASSES.add("Double");
        PERMITTED_CLASSES.add("Character");
        PERMITTED_CLASSES.add("Boolean");
    }

}
