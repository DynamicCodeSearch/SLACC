package edu.ncsu.visitors.blocks;

import com.google.common.collect.Iterables;
import com.google.common.collect.Sets;

import java.util.Arrays;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;

public class Type {
    private final static Set<String> PRIMITIVES = new HashSet<String>(Arrays.asList(
        "short",
        "int",
        "long",
        "char",
        "float",
        "double",
        "boolean"
    ));

    private final static Set<String> PRIMITIVE_OBJECTS = new HashSet<>(Arrays.asList(
        "Short",
        "Integer",
        "Long",
        "Character",
        "Float",
        "Double",
        "Boolean"
    ));

    public final static Set<String> IMMUTABLES = new HashSet<>(
            Sets.newHashSet(Iterables.concat(PRIMITIVES, PRIMITIVE_OBJECTS, Collections.singletonList("String"))));

    private static boolean isValidUtilClass(String className) {
        try {
            Class.forName(String.format("java.util.%s", className));
        } catch (ClassNotFoundException e) {
            return false;
        }
        return true;
    }

    public static boolean isValidType(String className) {
        return PRIMITIVES.contains(className) || PRIMITIVE_OBJECTS.contains(className) || isValidUtilClass(className);
    }

}
