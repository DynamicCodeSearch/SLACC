package edu.ncsu.executors.models;

import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonPrimitive;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Array;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Function {

    private Method method;

    private MethodDeclaration ast;

    private List<Integer> lines;

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

    public List<Integer> getLines() {
        return lines;
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

    public Function(Method method, MethodDeclaration ast) {
        this.method = method;
        this.method.setAccessible(true);
        this.ast = ast;
        arguments = new ArrayList<>();
        for (Parameter parameter: ast.getParameters()) {
            FunctionVariable variable = FunctionVariable.getFunctionVariable(
                    parameter.getType(), getPackageName());
            variable.setName(parameter.getId().getName());
            if (!variable.isFuzzable())
                this.isFuzzable = false;
            arguments.add(variable);
        }
        try {
            returnVariable = FunctionVariable.getFunctionVariable(ast.getType(), getPackageName());
            if (!returnVariable.isFuzzable())
                this.isFuzzable = false;
        } catch (RuntimeException e) {
            returnVariable = null;
            this.isFuzzable = false;
        }
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
        List argsList;
        if (getExpandedArgs().size() == 1) {
            argsList = Collections.singletonList(args);
        } else {
            argsList = (List) args;
        }
        List funcArgs = new ArrayList();
        for(int i=0; i<getArguments().size(); i++) {
            FunctionVariable functionVariable = getArguments().get(i);
            funcArgs.add(functionVariable.convertToFunctionArgument(argsList.get(i)));
        }
        return funcArgs;
    }

    public JsonObject dumpReturnAsJSON(Object returnVal, String errorMessage, long duration) {
        // TODO: convert to JSON
        System.out.println(returnVal);
        System.out.println(String.format("Error: %s", errorMessage));
        return new JsonObject();
    }

    private static JsonElement formatAsJSON(Object object) {
        Field[] fields = object.getClass().getDeclaredFields();
        JsonObject jsonObject = new JsonObject();
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
        return jsonObject;
    }

    public static void main(String[] args) {
        Point a = new Point(2, 3);
        Point b = new Point(4, 5);
        Segment segment = new Segment(a, b);
        System.out.println(Function.formatAsJSON(segment));;
    }
}

class Point {
    double x;
    private double y;

    Point(double x, double y) {
        this.x = x;
        this.y = y;
    }
}


class Segment {
    private Point[] points;
    int x = 5;
    Point p1;
    Point p2;

    Segment(Point p1, Point p2) {
        this.p1 = p1;
        this.p2 = p2;
        points = new Point[2];
        points[0] = p1;
        points[1] = p2;
    }
}
