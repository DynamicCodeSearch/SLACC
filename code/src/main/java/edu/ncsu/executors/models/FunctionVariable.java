package edu.ncsu.executors.models;

import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.PrimitiveType;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import com.google.gson.JsonObject;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import edu.ncsu.visitors.blocks.Imports;
import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class FunctionVariable {

    private static final Logger LOGGER = Logger.getLogger(FunctionVariable.class.getName());

    private String name;

    private Primitive primitive;

    private String dataType;

    private String packageName;

    private int arrayDimensions = 0;

    private boolean isFuzzable = true;

    public static FunctionVariable getFunctionVariable(Type type, String packageName) {
        if (type instanceof PrimitiveType) {
            return new FunctionVariable((PrimitiveType) type);
        } else if (type instanceof ClassOrInterfaceType) {
            return new FunctionVariable((ClassOrInterfaceType) type, packageName);
        } else if (type instanceof ReferenceType) {
            return new FunctionVariable((ReferenceType) type, packageName);
        }
        throw new RuntimeException("Invalid type " + type.getClass().getName());
    }

    public static FunctionVariable fromJSON(JsonObject variableJSON) {
        FunctionVariable functionVariable = new FunctionVariable();
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

    public FunctionVariable(PrimitiveType type) {
        this.primitive = Primitive.getPrimitive(type.toStringWithoutComments());
    }

    private void copy(FunctionVariable functionVariable) {
        this.name = functionVariable.name;
        this.primitive = functionVariable.primitive;
        this.dataType = functionVariable.dataType;
        this.packageName = functionVariable.packageName;
        this.arrayDimensions = functionVariable.arrayDimensions;
        this.isFuzzable = functionVariable.isFuzzable;
    }

    public FunctionVariable(ClassOrInterfaceType type, String packageName) {
        setType(type.getName(), packageName);
    }

    public void setType(String type, String packageName) {
        UserDefinedObjects udo = UserDefinedObjects.getUserDefinedObjects();
        if (packageName != null && udo.canBeFuzzed(udo.getClassObject(packageName, type))) {
            this.dataType = type;
            this.packageName = packageName;
            return;
        }
        if (Primitive.isValidType(type)) {
            this.primitive = Primitive.getPrimitive(type);
            return;
        }
        // TODO: Uncomment lines below to support List, Set etc.
//        String systemPackage = getSystemPackage(type);
//        if (systemPackage != null) {
//            this.packageName = systemPackage;
//            return;
//        }
        this.dataType = type;
        this.isFuzzable = false;
    }

    public FunctionVariable(ReferenceType type, String packageName) {
        if (type.getType() instanceof PrimitiveType) {
            copy(new FunctionVariable((PrimitiveType) type.getType()));
        } else if (type.getType() instanceof ClassOrInterfaceType) {
            copy(new FunctionVariable((ClassOrInterfaceType) type.getType(), packageName));
        }
        this.arrayDimensions = type.getArrayCount();
    }

    public static String getSystemPackage(String className) {
        for (String packageName: Imports.getDefaultImportPackages()) {
            try {
                PackageManager.findClass(packageName, className);
                return packageName;
            } catch (RuntimeException e) {
            }
        }
        return null;
    }



    public FunctionVariable(String dataType) {
        this.dataType = dataType;
    }


    public FunctionVariable(Primitive primitive) {
        this.primitive = primitive;
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

    public void setDataType(String dataType) {
        this.dataType = dataType;
    }

    public int getArrayDimensions() {
        return arrayDimensions;
    }

    public void setArrayDimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    public boolean isFuzzable() {
        return isFuzzable;
    }

    public void setValid(boolean valid) {
        isFuzzable = isFuzzable;
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
                sb.append(String.format("%s.%s", packageName, dataType));
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

    public String makeKey() {
        String key;
        if (primitive != null) {
            key = primitive.getName();
        } else {
            Constructor constructor = Constructor.getConstructor(packageName, dataType);
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

}
