package edu.ncsu.visitors.blocks;

import java.util.*;

public class Imports {
    /***
     * Individual import headers
     */
    private static Map<String, String> INDIVIDUAL_IMPORT_HEADERS = new HashMap<>();

    /***
     * File import headers
     */
    private static Map<Set<String>, String> FILE_IMPORT_HEADERS = new HashMap<>();

    /***
     * Retrieve imports for list of keys
     * @param keys array of keys to construct imports
     * @return Imports for all keys as a string
     */
    public static String getFileImports(String... keys) {
        Set<String> keySets = new HashSet<>(Arrays.asList(keys));
        if (!FILE_IMPORT_HEADERS.containsKey(keySets)) {
            StringBuilder sb = new StringBuilder();
            for(String key: keySets) {
                sb.append(getImports(key)).append("\n");
            }
            sb.append("\n");
            FILE_IMPORT_HEADERS.put(keySets, sb.toString());
        }
        return FILE_IMPORT_HEADERS.get(keySets);
    }

    /***
     * Get imports for a key
     * @param key Key to construct import
     * @return Imports as string
     */
    private static String getImports(String key) {
        if (!INDIVIDUAL_IMPORT_HEADERS.containsKey(key)) {
            makeImportHeader(key);
        }
        return INDIVIDUAL_IMPORT_HEADERS.get(key);
    }

    /***
     * Construct import header for a certain key. Supports java.lang and java.utl
     * @param key Key to construct import header.
     */
    private static void makeImportHeader(String key) {
        if (key.equals("java.lang.")) {
            INDIVIDUAL_IMPORT_HEADERS.put(key, "import java.lang.*;\n");
        } else if (key.equals("java.util.")) {
            StringBuilder sb = new StringBuilder();
            sb.append("import java.util.AbstractCollection;").append("\n");
            sb.append("import java.util.AbstractList;").append("\n");
            sb.append("import java.util.AbstractMap;").append("\n");
            sb.append("import java.util.AbstractQueue;").append("\n");
            sb.append("import java.util.AbstractSequentialList;").append("\n");
            sb.append("import java.util.AbstractSet;").append("\n");
            sb.append("import java.util.ArrayDeque;").append("\n");
            sb.append("import java.util.ArrayList;").append("\n");
            sb.append("import java.util.Arrays;").append("\n");
            sb.append("import java.util.Collection;").append("\n");
            sb.append("import java.util.Collections;").append("\n");
            sb.append("import java.util.Comparator;").append("\n");
            sb.append("import java.util.Dictionary;").append("\n");
            sb.append("import java.util.HashMap;").append("\n");
            sb.append("import java.util.HashSet;").append("\n");
            sb.append("import java.util.Hashtable;").append("\n");
            sb.append("import java.util.IdentityHashMap;").append("\n");
            sb.append("import java.util.Iterator;").append("\n");
            sb.append("import java.util.HashMap;").append("\n");
            sb.append("import java.util.LinkedHashMap;").append("\n");
            sb.append("import java.util.LinkedHashSet;").append("\n");
            sb.append("import java.util.LinkedList;").append("\n");
            sb.append("import java.util.List;").append("\n");
            sb.append("import java.util.ListIterator;").append("\n");
            sb.append("import java.util.Map;").append("\n");
            sb.append("import java.util.NavigableMap;").append("\n");
            sb.append("import java.util.NavigableSet;").append("\n");
            sb.append("import java.util.Objects;").append("\n");
            sb.append("import java.util.PriorityQueue;").append("\n");
            sb.append("import java.util.Settings;").append("\n");
            sb.append("import java.util.Queue;").append("\n");
            sb.append("import java.util.Random;").append("\n");
            sb.append("import java.util.Set;").append("\n");
            sb.append("import java.util.SortedMap;").append("\n");
            sb.append("import java.util.SortedSet;").append("\n");
            sb.append("import java.util.Stack;").append("\n");
            sb.append("import java.util.StringTokenizer;").append("\n");
            sb.append("import java.util.TreeMap;").append("\n");
            sb.append("import java.util.TreeSet;").append("\n");
            sb.append("import java.util.UUID;").append("\n");
            sb.append("import java.util.Vector;").append("\n");
            sb.append("import java.util.WeakHashMap;").append("\n");
//            INDIVIDUAL_IMPORT_HEADERS.put(key, sb.toString());
            INDIVIDUAL_IMPORT_HEADERS.put(key, "import java.util.*;\n");
        } else {
            INDIVIDUAL_IMPORT_HEADERS.put(key, "import java.io.*;\n");
        }
    }

    public static Set<String> getDefaultImportKeys(){
        Set<String> defaultImportKeys = new HashSet<>();
        defaultImportKeys.add("java.io.");
        defaultImportKeys.add("java.lang.");
        defaultImportKeys.add("java.util.");
        return defaultImportKeys;
    }

    public static List<String> getDefaultImportPackages() {
        List<String> defaultImportPackages = new ArrayList<>();
        defaultImportPackages.add("java.io");
        defaultImportPackages.add("java.lang");
        defaultImportPackages.add("java.util");
        return defaultImportPackages;
    }

    /***
     * Default imports currently being run.
     * @return
     */
    public static String defaultImports() {
        Set<String> importKeys = getDefaultImportKeys();
        return Imports.getFileImports(importKeys.toArray(new String[importKeys.size()]));
    }
}
