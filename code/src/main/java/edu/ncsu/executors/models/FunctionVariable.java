package edu.ncsu.executors.models;

import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.PrimitiveType;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.executors.helpers.FileHandler;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import edu.ncsu.visitors.blocks.Imports;
import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Array;
import java.lang.reflect.InvocationTargetException;
import java.util.*;
import java.util.logging.Logger;

public class FunctionVariable {

    private static final Logger LOGGER = Logger.getLogger(FunctionVariable.class.getName());

    private String dataset;

    private String name;

    private Primitive primitive;

    private String dataType;

    private String packageName;

    private int arrayDimensions = 0;

    private boolean isFuzzable = true;

    private boolean isBuiltInType = false;


    public static FunctionVariable getFunctionVariable(String dataset, Type type, String packageName) {
        if (type instanceof PrimitiveType) {
            return new FunctionVariable(dataset, (PrimitiveType) type);
        } else if (type instanceof ClassOrInterfaceType) {
            return new FunctionVariable(dataset, (ClassOrInterfaceType) type, packageName);
        } else if (type instanceof ReferenceType) {
            return new FunctionVariable(dataset, (ReferenceType) type, packageName);
        }
        throw new RuntimeException("Invalid type " + type.getClass().getName());
    }

    static FunctionVariable fromJSON(String dataset, JsonObject variableJSON) {
        FunctionVariable functionVariable = new FunctionVariable();
        functionVariable.dataset = dataset;
        String dataType = variableJSON.get("type").getAsString();
        String packageName = null;
        if (variableJSON.has("packageName"))
            packageName = variableJSON.get("packageName").getAsString();
        functionVariable.setType(dataType, packageName);
        if (variableJSON.has("name"))
            functionVariable.name = variableJSON.get("name").getAsString();
        if (variableJSON.has("arrayDimensions"))
            functionVariable.arrayDimensions = variableJSON.get("arrayDimensions").getAsInt();
        return functionVariable;
    }

    private FunctionVariable(){}

    private FunctionVariable(String dataset, PrimitiveType type) {
        this.dataset = dataset;
        this.primitive = Primitive.getPrimitive(type.toStringWithoutComments());
    }

    private void copy(FunctionVariable functionVariable) {
        this.dataset = functionVariable.dataset;
        this.name = functionVariable.name;
        this.primitive = functionVariable.primitive;
        this.dataType = functionVariable.dataType;
        this.packageName = functionVariable.packageName;
        this.arrayDimensions = functionVariable.arrayDimensions;
        this.isFuzzable = functionVariable.isFuzzable;
        this.isBuiltInType = functionVariable.isBuiltInType;
    }

    public static FunctionVariable clone(FunctionVariable functionVariable) {
        FunctionVariable newFunctionVariable = new FunctionVariable();
        newFunctionVariable.copy(functionVariable);
        return newFunctionVariable;
    }

    private FunctionVariable(String dataset, ClassOrInterfaceType type, String packageName) {
        this.dataset = dataset;
        setType(type.toString(), packageName);
    }

    private FunctionVariable(String dataset, ReferenceType type, String packageName) {
        if (type.getType() instanceof PrimitiveType) {
            copy(new FunctionVariable(dataset, (PrimitiveType) type.getType()));
        } else if (type.getType() instanceof ClassOrInterfaceType) {
            copy(new FunctionVariable(dataset, (ClassOrInterfaceType) type.getType(), packageName));
        }
        this.arrayDimensions = type.getArrayCount();
    }

    private void setType(String type, String packageName) {
        UserDefinedObjects udo = UserDefinedObjects.getUserDefinedObjects(this.dataset);
        if (packageName != null && udo.canBeFuzzed(udo.getClassObject(packageName, type))) {
            this.dataType = type;
            this.packageName = packageName;
            return;
        }
        if (Primitive.isValidType(type)) {
            this.primitive = Primitive.getPrimitive(type);
            if (Primitive.isBoxed(type)) {
                this.dataType = type;
            }
            return;
        }
        // TODO: Uncomment lines below to support List, Set etc.
        String systemPackage = getSystemPackage(type);
        if (systemPackage != null && isSupportedSystemClass(getFullName(systemPackage, type))) {
            this.dataType = type;
            this.packageName = systemPackage;
            this.isBuiltInType = true;
            return;
        }
        this.dataType = type;
        this.isFuzzable = false;
    }

    private static String getSystemPackage(String className) {
        for (String packageName: Imports.getDefaultImportPackages()) {
            try {
                PackageManager.findClass(packageName, className);
                return packageName;
            } catch (RuntimeException e) {
//                LOGGER.warning(String.format("System package not found: %s", packageName));
            }
        }
        return null;
    }

    private boolean isSupportedSystemClass(String className) {
        return FileHandler.isSupportedFileClass(className);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Primitive getPrimitive() {
        return primitive;
    }

    public void setPrimitive(Primitive primitive) {
        this.primitive = primitive;
    }

    public String getDataType() {
        return dataType;
    }

    public String getDataTypeAsString() {
        StringBuilder dt = new StringBuilder();
        dt.append(dataType);
        for (int i=0; i < arrayDimensions; i++)
            dt.append("[]");
        return dt.toString();
    }

    public int getArrayDimensions() {
        return arrayDimensions;
    }

    public void setArrayDimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    boolean isFuzzable() {
        return isFuzzable;
    }

    public boolean isBuiltInType() {
        return isBuiltInType;
    }

    public String getPackageName() {
        return packageName;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (isFuzzable) {
            sb.append("+");
        } else {
            sb.append("-");
        }
        if (primitive != null) {
            sb.append(primitive.getName());
        } else if (dataType != null){
            if (packageName != null) {
                sb.append(getFullName());
            } else {
                sb.append(dataType);
            }

        }
        if (arrayDimensions > 0) {
            for (int i=0; i < arrayDimensions; i++)
                sb.append("[]");
        }
        if (name != null) {
            sb.append(" ").append(name);
        }
        return sb.toString();
    }

    public String getFullName() {
        return String.format("%s.%s", packageName, dataType);
    }

    public String getFullName(String packageName, String dataType) {
        return String.format("%s.%s", packageName, dataType);
    }

    public String toFunctionParameter() {
        StringBuilder sb = new StringBuilder();
        sb.append(dataType);
        if (arrayDimensions > 0) {
            for (int i=0; i < arrayDimensions; i++)
                sb.append("[]");
        }
        sb.append(" ").append(getName());
        return sb.toString();
    }

    public String makeKey() {
        String key;
        if (primitive != null) {
//            key = primitive.getName();
            key = primitive.getFamily();
        } else if (isBuiltInType) {
            key = getFullName();
            if (FileHandler.isInputClass(key)) {
                key = FileHandler.FILE_INPUT_TYPE;
            } else if  (FileHandler.isOutputClass(key)) {
                key = FileHandler.FILE_OUTPUT_TYPE;
            }
        } else {
            Constructor constructor = Constructor.getConstructor(this.dataset, packageName, dataType);
            if (constructor == null || constructor.getParameters() == null)
                return null;
            List<String> paramKeys = new ArrayList<>();
            for (FunctionVariable parameter: constructor.getParameters()) {
                String paramKey = parameter.makeKey();
                if (paramKey != null) {
                    paramKeys.add(paramKey);
                }
            }
            if (paramKeys.size() == 0)
                return null;
            key = StringUtils.join(paramKeys, ",");
        }
        if (arrayDimensions > 0) {
            key = "(" + key + ")@"+arrayDimensions;
        }

        return key;
    }

//    public List<String> expandArgs() {
//        List<String> paramKeys = new ArrayList<>();
//        if (primitive != null) {
//            paramKeys.add(primitive.getName());
//        } else {
//            Constructor constructor = Constructor.getConstructor(this.dataset, packageName, dataType);
//            if (constructor == null || constructor.getParameters() == null)
//                return null;
//            for (FunctionVariable parameter: constructor.getParameters()) {
//                List<String> expandedParams = parameter.expandArgs();
//                if (expandedParams != null) {
//                    paramKeys.addAll(expandedParams);
//                }
//            }
//            if (paramKeys.size() == 0)
//                return null;
//        }
//        if (arrayDimensions > 0) {
//            return Collections.singletonList("(" + StringUtils.join(paramKeys, ",") + ")@"+arrayDimensions);
//        }
//        return paramKeys;
//    }

    public Object convertToFunctionArgument(JsonArray arg, int funcUUID, int argSetIndex) {
        return convertToFunctionArgument(arg, arrayDimensions, funcUUID, argSetIndex);
    }

    private Object convertToFunctionArgument(JsonArray arg, int arraySize, int funcUUID, int argSetIndex) {
        if (arraySize == 0) {
            if (primitive != null) {
                Object argVal = arg.get(0);
                arg.remove(0);
                return Primitive.convertToArgument(primitive, argVal.toString());
            } else if (isBuiltInType) {
                String key = getFullName();
                Object argVal = arg.get(0);
                arg.remove(0);
                if (FileHandler.isInputClass(key)) {
                    return FileHandler.convertFileInput(key, argVal.toString());
                } else if (FileHandler.isOutputClass(key)) {
                    return FileHandler.convertFileOutput(key, funcUUID, argSetIndex);
                }
                throw new RuntimeException(String.format("We do not support %s", key));
            } else {
                Constructor constructor = Constructor.getConstructor(this.dataset, packageName, dataType);
                List<Object> argVals = new ArrayList<>();
                if (constructor != null && constructor.getParameters() != null && constructor.getParameters().size() > 0) {
                    for (int i=0; i<constructor.getParameters().size(); i++) {
                        FunctionVariable parameter = constructor.getParameters().get(i);
                        argVals.add(parameter.convertToFunctionArgument(arg, funcUUID, argSetIndex));
                    }
                }
                java.lang.reflect.Constructor classConstructor = getClassConstructor();
                try {
                    return classConstructor.newInstance(argVals.toArray());
                } catch (InstantiationException e) {
                    throw new RuntimeException(String.format("InstantiationException: %s", e.getMessage()), e);
                } catch (IllegalAccessException e) {
                    throw new RuntimeException(String.format("IllegalAccessException: %s", e.getMessage()), e);
                } catch (InvocationTargetException e) {
                    throw new RuntimeException(String.format("InvocationTargetException: %s", e.getMessage()), e.getTargetException());
                }
            }
        } else {
            JsonElement arrayArg = arg.get(0);
            arg.remove(0);
            List<Object> vals = new ArrayList<>();
            for (JsonElement argVal: arrayArg.getAsJsonArray()) {
                try {
                    if (argVal.isJsonArray()) {
                        vals.add(convertToFunctionArgument(argVal.getAsJsonArray(), arraySize - 1, funcUUID, argSetIndex));
                    } else {
                        JsonArray argValArray = new JsonArray();
                        argValArray.add(argVal);
                        vals.add(convertToFunctionArgument(argValArray, arraySize - 1, funcUUID, argSetIndex));
                    }
                } catch (Exception e) {
                    System.out.println(argVal);
                    throw new RuntimeException(e);
                }

            }
            Class baseClass = getClassInstantiation();
            Class arrayClass = Array.newInstance(baseClass, vals.size()).getClass();
            return Arrays.copyOf(vals.toArray(), vals.size(), arrayClass);
        }
    }

    public Class getClassInstantiation() {
        if (primitive != null) {
            if (dataType != null) {
                return Primitive.getPrimitiveBoxedClass(primitive);
            } else {
                return Primitive.getPrimitiveClass(primitive);
            }
        } else {
            return PackageManager.findClass(packageName, dataType);
        }
    }

    public Class getCompleteClassInstatiation() {
        Class baseClass = getClassInstantiation();
        for (int i=0; i<arrayDimensions; i++) {
            baseClass = Array.newInstance(baseClass, 0).getClass();
        }
        return baseClass;
    }

    public java.lang.reflect.Constructor getClassConstructor() {
        if (primitive != null) {
            throw new RuntimeException(String.format("Constructor cannot be created for primitive type: %s", primitive.getName()));
        }
        Class objClass = getClassInstantiation();
        List<Class> constructorClasses = new ArrayList<>();
        Constructor constructor = Constructor.getConstructor(this.dataset, packageName, dataType);
        assert constructor != null;
        for (FunctionVariable parameter: constructor.getParameters()) {
            constructorClasses.add(parameter.getCompleteClassInstatiation());
        }
        try {
            java.lang.reflect.Constructor classConstructor = objClass.getDeclaredConstructor(constructorClasses.toArray(new Class[0]));
            classConstructor.setAccessible(true);
            return classConstructor;
        } catch (NoSuchMethodException e) {
            throw new RuntimeException(e);
        }
    }

    public JsonObject getMetadata() {
        JsonObject returnObject = new JsonObject();
        returnObject.addProperty("isArray", this.getArrayDimensions() > 0);
        boolean isPrimitive = this.getPrimitive() != null;
        returnObject.addProperty("isPrimitive", isPrimitive);
        if (isPrimitive) {
            returnObject.addProperty("type", this.getPrimitive().getName());
        } else {
            returnObject.addProperty("type", this.getDataType());
            JsonObject classObject = UserDefinedObjects.getUserDefinedObjects(this.dataset).getClassObject(this.getPackageName(), this.getDataType());
            if (classObject != null && classObject.has("variables") && classObject.get("variables").getAsJsonArray().size() > 0) {
                JsonArray variables = new JsonArray();
                for (JsonElement element: classObject.get("variables").getAsJsonArray()) {
                    JsonObject variableObject = element.getAsJsonObject();
                    JsonObject variableMetadata = FunctionVariable.fromJSON(this.dataset, variableObject).getMetadata();
                    if (variableMetadata != null)
                        variables.add(variableMetadata);
                    else
                        return null;
                }
                returnObject.add("variables", variables);
            } else {
                return null;
            }
        }
        return returnObject;
    }

}
