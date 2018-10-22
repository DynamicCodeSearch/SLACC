package edu.ncsu.executors.models;

import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.comments.Comment;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Array;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Function {

    private String dataset;

    private Method method;

    private MethodDeclaration ast;

    private List<Integer> linesTouched;

    private List<Integer> span;

    private List<FunctionVariable> arguments;

    private FunctionVariable returnVariable;

    private boolean isFuzzable = true;

    private String argsKey;

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

    public List<String> getExpandedArgs() {
        List<String> expandedArgs = new ArrayList<>();
        for (FunctionVariable argument: arguments)
            expandedArgs.addAll(argument.expandArgs());
        return expandedArgs;
    }

    public Function(String dataset, Method method, MethodDeclaration ast) {
        this.dataset = dataset;
        this.method = method;
        this.method.setAccessible(true);
        this.ast = ast;
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
            if (!returnVariable.isFuzzable())
                this.isFuzzable = false;
        } catch (RuntimeException e) {
            returnVariable = null;
            this.isFuzzable = false;
        }
        processComments();
    }

    private void processComments() {
        for (Comment comment: ast.getAllContainedComments()) {
            String commentString = comment.toString().trim();
            int colonPos = commentString.indexOf(":");
            if (commentString.startsWith("// lines: ")) {
                this.linesTouched = new ArrayList<>();
                for (String lineStr: commentString.substring(colonPos + 1).trim().split(","))
                    this.linesTouched.add(Integer.parseInt(lineStr));
                Collections.sort(this.linesTouched);
            } else if (commentString.startsWith("// start_end: ")) {
                this.span = new ArrayList<>();
                for (String lineStr: commentString.substring(colonPos + 1).trim().split(","))
                    this.span.add(Integer.parseInt(lineStr));
                Collections.sort(this.span);
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
            List<String> argKeys = new ArrayList<>();
            for (FunctionVariable argument: arguments) {
                String argKey = argument.makeKey();
                if (argKey != null)
                    argKeys.add(argKey);
            }
            if (argKeys.size() == 0)
                return null;
            argsKey = StringUtils.join(argKeys, ",");
        }
        return argsKey;
    }

    public List<Object> convertToFunctionArguments(Object args) {
        JsonArray argsJsonArray = (JsonArray) args;
        List funcArgs = new ArrayList();
        for(int i=0; i<getArguments().size(); i++) {
            FunctionVariable functionVariable = getArguments().get(i);
            funcArgs.add(functionVariable.convertToFunctionArgument(argsJsonArray));
        }
        return funcArgs;
    }

    public JsonObject dumpReturnAsJSON(Object returnVal, String errorMessage, long duration) {
        // TODO: convert to JSON
        JsonObject formatted = new JsonObject();
        formatted.add("return", formatAsJSON(returnVal));
        formatted.addProperty("errorMessage", errorMessage);
        formatted.addProperty("duration", duration);
        return formatted;
    }

    private static JsonElement formatAsJSON(Object object) {
        if (object == null)
            return null;
        if (object.getClass().isArray()) {
            JsonArray array = new JsonArray();
            for (Object obj: (Object []) object) {
                array.add(formatAsJSON(obj));
            }
            return array;
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
                                array.add(formatAsJSON(arrayElement));
                            }
                            jsonObject.add(field.getName(), array);
                        } else {
                            String type = value.getClass().getSimpleName();
                            if (Primitive.isValidType(type)) {
                                Primitive primitive = Primitive.getPrimitive(type);
                                jsonObject.add(field.getName(), Primitive.convertToArgumentJSON(primitive, value.toString()));
                            } else {
                                jsonObject.add(field.getName(), formatAsJSON(value));
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
        JsonArray linesTouched = new JsonArray();
        for (Integer line: this.linesTouched)
            linesTouched.add(line);
        JsonArray span = new JsonArray();
        for (Integer line: this.span)
            span.add(line);
        metadata.add("linesTouched", linesTouched);
        metadata.add("span", span);
        metadata.add("return", returnVariable.getMetadata());
        return metadata;
    }
}

