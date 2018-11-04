package edu.ncsu.executors.models;

import com.google.gson.JsonElement;
import com.google.gson.JsonPrimitive;

import java.util.*;

public enum  Primitive {

    SHORT("short", Family.INT_FAMILY, "short", "Short", "java.lang.Short"),
    INTEGER("integer", Family.INT_FAMILY, "int", "Integer", "java.lang.Integer"),
    LONG("long", Family.INT_FAMILY, "long", "Long", "java.lang.Long"),
    CHARACTER("character", Family.CHAR_FAMILY, "char", "Character", "java.lang.Character"),
    FLOAT("float", Family.FLOAT_FAMILY, "float", "Float", "java.lang.Float"),
    DOUBLE("double", Family.FLOAT_FAMILY, "double", "Double", "java.lang.Double"),
    BOOLEAN("boolean", Family.BOOLEAN_FAMILY, "boolean", "Boolean", "java.lang.Boolean"),
    BYTE("byte", Family.BYTE_FAMILY, "byte", "Byte", "java.lang.Byte"),
    STRING("string", Family.STRING_FAMILY, "String", "java.lang.String");

    public class Family {
        public static final String INT_FAMILY = "int";
        public static final String CHAR_FAMILY = "char";
        public static final String FLOAT_FAMILY = "float";
        public static final String BOOLEAN_FAMILY = "boolean";
        public static final String BYTE_FAMILY = "byte";
        public static final String STRING_FAMILY = "string";
    }

    /**
     * Mapping types to Primitive Enum.
     */
    private final static Map<String, Primitive> typeToPrimitiveMap = new HashMap<>();

    /**
     * Mapping names to Primitive Enum.
     */
    private final static Map<String, Primitive> nameToPrimitiveMap = new HashMap<>();

    /**
     * Name of enum
     */
    private String name;

    /***
     * General family of primitive datatype
     */
    private String family;

    /**
     * List of types corresponding to the primitive.
     */
    private List<String> types;

    static {
        // Populating the maps
        for (Primitive dataType: Primitive.values()) {
            nameToPrimitiveMap.put(dataType.name, dataType);
            for (String className: dataType.getTypes())
                typeToPrimitiveMap.put(className, dataType);
        }
    }

    /**
     * @return - Name of the Primitive.
     */
    public String getName() {
        return name;
    }

    /**
     * @return - Family of the Primitive
     */
    public String getFamily() {
        return family;
    }

    /**
     * @return - Types for Primitive
     */
    public List<String> getTypes() {
        return types;
    }

    /**
     * @param type - Type as string
     * @return - Return Primitive Enum for the type
     */
    public static Primitive getPrimitive(String type) {
        return typeToPrimitiveMap.get(type);
    }

    /**
     * @param type - Type as string
     * @return - Return true if Primitive Enum exists for type
     */
    public static boolean isValidType(String type) {
        return typeToPrimitiveMap.containsKey(type);
    }

    /**
     * @param name - Name of primitive
     * @return - Return Primitive Enum for the name
     */
    public static Primitive getPrimitiveByName(String name) {
        return nameToPrimitiveMap.get(name);
    }

    /**
     * Create an instance of Primitive Enum
     * @param name - Name of the Primitive Enum
     * @param types - variable args of all the types
     */
    Primitive(String name, String family, String... types) {
        this.name = name;
        this.family = family;
        this.types = new ArrayList<>(Arrays.asList(types));
    }

    /**
     *
     * @param primitive - Primitive Enum
     * @param argString - Value of argument
     * @return - Argument converted to
     */
    public static Object convertToArgument(Primitive primitive, String argString) {
        switch (primitive) {
            case SHORT:
                return (short) Double.parseDouble(argString);
            case INTEGER:
                return (int) Double.parseDouble(argString);
            case LONG:
                return (long) Double.parseDouble(argString);
            case CHARACTER:
                return argString.charAt(0);
            case FLOAT:
                return (float) Double.parseDouble(argString);
            case DOUBLE:
                return Double.parseDouble(argString);
            case BOOLEAN:
                return Boolean.parseBoolean(argString);
            case BYTE:
                return Byte.parseByte(argString);
            case STRING:
                return argString;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    public static JsonElement convertToArgumentJSON(Primitive primitive, String argString) {
        switch (primitive) {
            case SHORT:
                return new JsonPrimitive((short) Double.parseDouble(argString));
            case INTEGER:
                return new JsonPrimitive((int) Double.parseDouble(argString));
            case LONG:
                return new JsonPrimitive((long) Double.parseDouble(argString));
            case CHARACTER:
                return new JsonPrimitive(argString.charAt(0));
            case FLOAT:
                return new JsonPrimitive((float) Double.parseDouble(argString));
            case DOUBLE:
                return new JsonPrimitive(Double.parseDouble(argString));
            case BOOLEAN:
                return new JsonPrimitive(Boolean.parseBoolean(argString));
            case BYTE:
                return new JsonPrimitive(Byte.parseByte(argString));
            case STRING:
                return new JsonPrimitive(argString);
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get class of primitive type
     * @param primitive - Enum of primitive
     * @return - Class of primitive type
     */
    public static Class getPrimitiveClass(Primitive primitive) {
        switch (primitive) {
            case SHORT:
                return short.class;
            case INTEGER:
                return int.class;
            case LONG:
                return long.class;
            case CHARACTER:
                return char.class;
            case FLOAT:
                return float.class;
            case DOUBLE:
                return double.class;
            case BOOLEAN:
                return boolean.class;
            case BYTE:
                return byte.class;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get boxed version class of primitive type
     * @param primitive - Enum of primitive
     * @return - Class of boxed primitive type
     */
    public static Class getPrimitiveBoxedClass(Primitive primitive) {
        switch (primitive) {
            case SHORT:
                return Short.class;
            case INTEGER:
                return Integer.class;
            case LONG:
                return Long.class;
            case CHARACTER:
                return Character.class;
            case FLOAT:
                return Float.class;
            case DOUBLE:
                return Double.class;
            case BOOLEAN:
                return Boolean.class;
            case BYTE:
                return Byte.class;
            case STRING:
                return String.class;
            default:
                throw new RuntimeException(String.format(
                        "Currently we do not support the class %s", primitive.getName()));
        }
    }

    /**
     * Get the boxed name of the primitive enum.
     * @param primitive - Type of primitive
     * @return - Boxed class name of the primitive. eg. int -> Integer
     */
    public static String getBoxedName(Primitive primitive) {
        return getPrimitiveBoxedClass(primitive).getSimpleName();
    }

    public static boolean isBoxed(String type) {
        return Character.isUpperCase(type.charAt(0));
    }
}

class Family {

}