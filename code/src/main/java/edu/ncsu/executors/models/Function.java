package edu.ncsu.executors.models;

import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.comments.Comment;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Array;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.*;

public class Function {

    private String dataset;

    private String filePath;

    private String baseFilePath;

    private Method method;

    private MethodDeclaration ast;

    private List<Integer> linesTouched;

    private List<Integer> span;

    private List<FunctionVariable> arguments;

    private FunctionVariable returnVariable;

    private boolean isFuzzable = true;

    private String argsKey;

    private List<String> allArgsKeys;

    private Map<String, String> argComboKeyMap = null;

    public String getPackageName() {
        return method.getDeclaringClass().getPackage().getName();
    }

    public String getClassName() {
        return method.getDeclaringClass().getSimpleName();
    }

    public String getName() {
        return method.getName();
    }

    public String getFunctionBody() {
        return ast.getBody().toStringWithoutComments();
    }

    public Method getMethod() {
        return method;
    }

    public MethodDeclaration getAst() {
        return ast;
    }


    public List<FunctionVariable> getArguments() {
        return arguments;
    }

    public FunctionVariable getReturnVariable() {
        return returnVariable;
    }

    public boolean isFuzzable() {
        return isFuzzable;
    }

    public List<Integer> getLinesTouched() {
        return linesTouched;
    }

    public List<Integer> getSpan() {
        return span;
    }

    public boolean isValidArgs() {
        for (FunctionVariable variable: arguments) {
            if (!variable.isFuzzable())
                return false;
        }
        return true;
    }


    public boolean shouldBeSkipped() {
        return arguments.size() > Settings.MAX_NUM_ARGS;
    }

//    public List<String> getExpandedArgs() {
//        List<String> expandedArgs = new ArrayList<>();
//        for (FunctionVariable argument: arguments)
//            expandedArgs.addAll(argument.expandArgs());
//        return expandedArgs;
//    }

    public Function(String dataset, Method method, MethodDeclaration ast, String filePath) {
        this.dataset = dataset;
        this.method = method;
        this.method.setAccessible(true);
        this.ast = ast;
        this.filePath = filePath;
        arguments = new ArrayList<>();
        for (Parameter parameter: ast.getParameters()) {
            FunctionVariable variable = FunctionVariable.getFunctionVariable(
                    this.dataset, parameter.getType(), getPackageName());
            variable.setName(parameter.getId().getName());
            if (!variable.isFuzzable())
                this.isFuzzable = false;
            arguments.add(variable);
        }
        try {
            returnVariable = FunctionVariable.getFunctionVariable(this.dataset, ast.getType(), getPackageName());
            if (!returnVariable.isFuzzable()
                    || FileHandler.isInputClass(returnVariable.getFullName())
                    || hasMultipleWriteArguments())
                this.isFuzzable = false;
        } catch (RuntimeException e) {
            returnVariable = null;
            this.isFuzzable = false;
        }
        processComments();
    }

    private boolean hasMultipleWriteArguments() {
        int n_write_args = 0;
        for (FunctionVariable arg: arguments) {
            if (FileHandler.isOutputClass(arg.getFullName()))
                n_write_args += 1;
        }
        return n_write_args > 1;
    }

    public int getUUID() {
        return System.identityHashCode(this);
    }

    private void processComments() {
        List<Comment> comments = ast.getAllContainedComments();
        if (comments == null || comments.size() == 0)
            return;
        String comment = comments.get(0).getContent();
        comment = comment.replaceAll("\\s", "").replace("*", "");
        for (String m : comment.split(";")) {
            String[] mSplits = m.split(":");
            switch (mSplits[0]) {
                case "source":
                    this.baseFilePath = mSplits[1];
                    break;
                case "lines":
                    this.linesTouched = new ArrayList<>();
                    for (String lineStr : mSplits[1].split(","))
                        this.linesTouched.add(Integer.parseInt(lineStr));
                    Collections.sort(this.linesTouched);
                    break;
                case "start_end":
                    this.span = new ArrayList<>();
                    for (String lineStr : mSplits[1].split(","))
                        this.span.add(Integer.parseInt(lineStr));
                    Collections.sort(this.span);
                    break;
            }
        }
    }

    private JsonObject getReturnMetaData() {
        JsonObject returnObject = new JsonObject();

        returnObject.addProperty("isArray", returnVariable.getArrayDimensions() > 0);
        boolean isPrimitive = returnVariable.getPrimitive() != null;
        returnObject.addProperty("isPrimitive", isPrimitive);
        if (isPrimitive) {
            returnObject.addProperty("type", returnVariable.getPrimitive().getName());
        } else {
            returnObject.addProperty("type", returnVariable.getDataType());
            JsonObject classObject = UserDefinedObjects.getUserDefinedObjects(this.dataset).getClassObject(returnVariable.getPackageName(), returnVariable.getDataType());
            if (classObject != null && classObject.has("variables")) {

                returnObject.add("variables", classObject.get("variables").getAsJsonArray());
            }
        }
        return returnObject;
    }

    public String makeArgumentsKey() {
        if (argsKey == null) {
            argsKey = constructArgumentTypesKey(arguments);
        }
        return argsKey;
    }

    public static String constructArgumentTypesKey(List<FunctionVariable> args) {
        List<String> argKeys = new ArrayList<>();
        for (FunctionVariable argument: args) {
            String argKey = argument.makeKey();
            if (argKey != null)
                argKeys.add(argKey);
        }
        if (argKeys.size() == 0)
            return null;
        return StringUtils.join(argKeys, ",");
    }

    public static String constructArgumentNamesKey(List<FunctionVariable> args) {
        List<String> argNames = new ArrayList<>();
        for (FunctionVariable argument: args) {
            argNames.add(argument.getName());
        }
        if (argNames.size() == 0)
            return null;
        return StringUtils.join(argNames, ",");
    }

    public List<String> makeAllArgumentsKeys() {
        if (allArgsKeys == null) {
            List<Object> argKeys = new ArrayList<>();
            for (FunctionVariable argument: arguments) {
                String argKey = argument.makeKey();
                if (argKey != null)
                    argKeys.add(argKey);
            }
            if (argKeys.size() == 0)
                return null;
            Set<String> keySet = new HashSet<String>();
            for (List<Object> permutated: getPermutations(argKeys)) {
                if (permutated.size() > 0) {
                    keySet.add(StringUtils.join(permutated, ","));
                }
            }
            allArgsKeys = new ArrayList<>(keySet);
        }
        return allArgsKeys;
    }

    /**
     * @return Map of arg names, key
     */
    public Map<String, String> getArgComboKeyMap() {
        // TODO: Implement this by doing the permutation crap!!
        if (argComboKeyMap == null) {
            argComboKeyMap = new HashMap<>();
            if (arguments.size() == 0 || shouldBeSkipped()) {
                return argComboKeyMap;
            }
            List<Object> clonedArgs = new ArrayList<>();
            for (FunctionVariable arg: arguments) {
                clonedArgs.add(FunctionVariable.clone(arg));
            }
            List<List<Object>> permutations = getPermutations(clonedArgs);
            for (List permutated : permutations) {
                String argTypesKey = constructArgumentTypesKey(permutated);
                String argNamesKey = constructArgumentNamesKey(permutated);
                argComboKeyMap.put(argNamesKey, argTypesKey);
            }
        }
        return argComboKeyMap;
    }

    public static List<List<Object>> getPermutations(List<Object> objects) {
        if (objects.size() == 0) {
            List<List<Object>> result = new ArrayList<List<Object>>();
            result.add(new ArrayList<Object>());
            return result;
        }
        Object first = objects.remove(0);
        List<List<Object>> returns = new ArrayList<List<Object>>();
        List<List<Object>> permutations = getPermutations(objects);
        for (List<Object> permutated : permutations) {
            for (int i = 0; i <= permutated.size(); i++) {
                List<Object> cloned = new ArrayList<>(permutated);
                cloned.add(i, first);
                returns.add(cloned);
            }
        }
        return returns;
    }


    public List<Object> convertToFunctionArguments(Object args, int argIndex) {
        JsonArray argsJsonArray = (JsonArray) args;
        List<Object> funcArgs = new ArrayList<>();
        int funcUUID = getUUID();
        for(int i=0; i<getArguments().size(); i++) {
            FunctionVariable functionVariable = getArguments().get(i);
            funcArgs.add(functionVariable.convertToFunctionArgument(argsJsonArray, funcUUID, argIndex));
        }
        return funcArgs;
    }

    public JsonObject dumpReturnAsJSON(Object returnVal, String errorMessage, long duration, int argSetIndex) {
        int funcUUID = getUUID();
        JsonObject formatted = new JsonObject();
        formatted.add("return", formatAsJSON(returnVal, funcUUID, argSetIndex));
        formatted.addProperty("errorMessage", errorMessage);
        formatted.addProperty("duration", duration);
        return formatted;
    }

    private static JsonElement formatAsJSON(Object object, int funcUUID, int argSetIndex) {
        if (object == null)
            return null;
        if (object.getClass().isArray()) {
            JsonArray array = new JsonArray();
            for (Object obj: (Object []) object) {
                array.add(formatAsJSON(obj, funcUUID, argSetIndex));
            }
            return array;
        } else if (FileHandler.isOutputClass(object.getClass().getCanonicalName())) {
            return new JsonPrimitive(FileHandler.dumpOutputAsText(funcUUID, argSetIndex));
        } else {
            JsonObject jsonObject = new JsonObject();
            if (Primitive.isValidType(object.getClass().getSimpleName())) {
                Primitive primitive = Primitive.getPrimitive(object.getClass().getSimpleName());
                return Primitive.convertToArgumentJSON(primitive, object.toString());
            } else {
                Field[] fields = object.getClass().getDeclaredFields();
                try {
                    for (Field field: fields) {
                        field.setAccessible(true);
                        Object value = field.get(object);
                        if (field.getType().isArray()) {
                            JsonArray array = new JsonArray();
                            Class arrayClass = Array.newInstance(field.getType().getComponentType(),
                                    Array.getLength(value)).getClass();
                            for (Object arrayElement: Arrays.copyOf((Object[]) value, Array.getLength(value), arrayClass)) {
                                array.add(formatAsJSON(arrayElement, funcUUID, argSetIndex));
                            }
                            jsonObject.add(field.getName(), array);
                        } else {
                            String type = value.getClass().getSimpleName();
                            if (Primitive.isValidType(type)) {
                                Primitive primitive = Primitive.getPrimitive(type);
                                jsonObject.add(field.getName(), Primitive.convertToArgumentJSON(primitive, value.toString()));
                            } else {
                                jsonObject.add(field.getName(), formatAsJSON(value, funcUUID, argSetIndex));
                            }
                        }
                    }
                } catch (IllegalAccessException e) {
                    throw new RuntimeException(e);
                }
            }
            return jsonObject;
        }
    }

    public JsonObject getMetaData() {
        JsonObject metadata = new JsonObject();
        metadata.addProperty("name", this.getName());
        metadata.addProperty("body", this.ast.toStringWithoutComments());
        metadata.addProperty("inputKey", this.makeArgumentsKey());
        metadata.addProperty("filePath", this.filePath);
        metadata.addProperty("baseFilePath", this.baseFilePath);
        if (this.linesTouched != null && this.linesTouched.size() > 0) {
            JsonArray linesTouched = new JsonArray();
            for (Integer line: this.linesTouched)
                linesTouched.add(line);
            metadata.add("linesTouched", linesTouched);
        }
        if (this.span != null) {
            JsonArray span = new JsonArray();
            for (Integer line: this.span)
                span.add(line);
            metadata.add("span", span);
        }
        metadata.add("return", returnVariable.getMetadata());
//        metadata.add("argNamesKeysMap", Utils.toJson(getArgComboKeyMap()));
        return metadata;
    }
}

