package edu.ncsu.executors.models;

import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.PrimitiveType;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import edu.ncsu.visitors.blocks.Imports;

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
        UserDefinedObjects userDefinedObjects = UserDefinedObjects.getUserDefinedObjects();
        String dataType = type.getName();
        if (userDefinedObjects.canBeFuzzed(userDefinedObjects.getClassObject(packageName, dataType))) {
            this.dataType = dataType;
            this.packageName = packageName;
            return;
        }
        if (Primitive.isValidType(dataType)) {
            this.primitive = Primitive.getPrimitive(dataType);
            return;
        }
        String systemPackage = getSystemPackage(dataType);
        if (systemPackage != null) {
            this.packageName = systemPackage;
            return;
        }
        this.dataType = dataType;
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
}
