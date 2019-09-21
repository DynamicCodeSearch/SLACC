package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ModifierSet;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import com.google.gson.JsonObject;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.executors.models.Primitive;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import static edu.ncsu.visitors.blocks.Type.*;

public class Variable {

    public final static String PUBLIC = "public";

    public final static String PRIVATE = "private";

    public final static String PROTECTED = "protected";

    public final static String DEFAULT = "default";

    /**
     * Unique ID of Variable
     */
    private String uuid;

    /***
     * Access modifier of the variable
     */
    private String scope="local";

    /**
     * Type of variable
     */
    protected String type;

    /**
     * AST Type of variable
     */
    protected Type astType;

    /**
     * Name of package
     */
    protected String packageName;

    /**
     * Name of variable
     */
    protected String name;

    /**
     * Number of dimensions of array
     */
    protected Integer arrayDimensions;

    /**
     * Initial value of Variable
     */
    protected Expression initValue = null;

    /**
     * Start postiion variable was declared
     */
    protected VariablePosition startPosition;

    /**
     * Positions where variables used
     */
    protected List<VariablePosition> usedPositions;

    /***
     * Positions where variables had their values changed
     */
    protected List<VariablePosition> assignPositions;

    /**
     * End scope of variable
     */
    protected Integer endScopeLineNumber;

    /**
     * Modifier code of the variable
     */
    protected int modifierCode = -1;

    /**
     * @return Type(AST) of variable
     */
    public Type getAstType() {
        return astType;
    }

    /**
     * @return Type(String) of variable
     */
    public String getType() {
        return type;
    }

    /**
     * @return Name of variable
     */
    public String getName() {
        return name;
    }


    public VariablePosition getStartPosition() {
        return startPosition;
    }

    /**
     * @return Line where variable's scope ends
     */
    public Integer getEndScopeLineNumber() {
        return endScopeLineNumber;
    }

    /**
     * @param position Insert position of variable
     */
    public void insertUsedPosition(VariablePosition position) {
        if (usedPositions == null)
            usedPositions = new ArrayList<>();
        usedPositions.add(position);
    }

    public void insertAssignPosition(VariablePosition position) {
        if (assignPositions == null)
            assignPositions = new ArrayList<>();
        assignPositions.add(position);
    }

    /**
     * @return The number of dimensions in the array
     */
    public Integer getArrayDimensions() {
        return arrayDimensions;
    }

    /**
     * Set the arrayDimensions for the variable
     * @param arrayDimensions The dimensions of variable
     */
    public void setArrayDimensions(int arrayDimensions) {
        this.arrayDimensions = arrayDimensions;
    }

    public Variable(String name, Type type, String packageName, String scope) {
        this.uuid = UUID.randomUUID().toString();
        this.name = name;
        this.scope = scope;
        this.astType = type;
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            this.type = refType.getType().toStringWithoutComments();
            this.arrayDimensions = ((ReferenceType) type).getArrayCount();
        } else {
            this.type = type.toStringWithoutComments();
            this.arrayDimensions = 0;
        }
        this.packageName = getPackageName(packageName, this.type);
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber) {
        this.uuid = UUID.randomUUID().toString();
        this.name = name;
        this.type = type;
        this.startPosition = new VariablePosition(lineNumber, columnNumber);
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber, Expression initValue) {
        this(name, type, lineNumber, columnNumber);
        this.initValue = initValue;
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     * @param parentNode AST of block where variable was declared
     */
    public Variable(String name, String type, Integer lineNumber, Integer columnNumber, Expression initValue, Node parentNode) {
        this(name, type, lineNumber, columnNumber, initValue);
        this.endScopeLineNumber = parentNode.getEndLine() - 1;
    }

    /**
     * Create a new variable
     * @param name Name of the variable
     * @param type Type of the variable
     * @param lineNumber Line number where variable was declared.
     * @param columnNumber Column number where variable was declared.
     * @param initValue Initial value of variable
     * @param parentNode AST of block where variable was declared
     */
    public Variable(String name, Type type, Integer lineNumber, Integer columnNumber, Expression initValue,
                    Node parentNode) {
        this(name, type.toStringWithoutComments(), lineNumber, columnNumber, initValue, parentNode);
        this.astType = type;
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            this.type = refType.getType().toStringWithoutComments();
            this.arrayDimensions = ((ReferenceType) type).getArrayCount();
        } else {
            this.arrayDimensions = 0;
        }
    }

    public Variable(String name, Type type, Integer lineNumber, Integer columnNumber, Expression initValue,
                    Node parentNode, int modifierCode) {
        this(name, type, lineNumber, columnNumber, initValue, parentNode);
        this.modifierCode = modifierCode;
    }


    @Override
    public boolean equals(Object obj) {
        if (obj == null || !(obj instanceof Variable))
            return false;
        Variable other = (Variable) obj;
        return this.uuid.equals(other.uuid);
    }

    @Override
    public int hashCode() {
        return this.uuid.hashCode();
    }

    @Override
    public String toString() {
        return this.type + "$$" + this.name + "$$" + this.startPosition;
    }

    public JsonObject toJson() {
        JsonObject jsonObject = new JsonObject();
        jsonObject.addProperty("name", name);
        jsonObject.addProperty("packageName", packageName);
        jsonObject.addProperty("type", type);
        jsonObject.addProperty("arrayDimensions", arrayDimensions);
        jsonObject.addProperty("scope", scope);
        return jsonObject;
    }

    public static String getModifier(int modifierCode) {
        if (ModifierSet.isPublic(modifierCode)) {
            return PUBLIC;
        } else if (ModifierSet.isProtected(modifierCode)) {
            return PROTECTED;
        } else if (ModifierSet.isPrivate(modifierCode)) {
            return PRIVATE;
        } else {
            return DEFAULT;
        }
    }

    public String toTypeString() {
        StringBuilder typeString = new StringBuilder();
        if (Primitive.isValidType(type)) {
            typeString.append(Primitive.getBoxedName(Primitive.getPrimitive(type)));
        } else {
            typeString.append(type);
        }
        for (int i=0; i<this.arrayDimensions; i++)
            typeString.append("[]");
        return typeString.toString();
    }

    public String toFunctionParameter() {
        return String.format("%s %s", toTypeString(), getName());
    }

    public boolean isAssignedInRange(VariablePosition start, VariablePosition end) {
        if (assignPositions == null || assignPositions.size() == 0)
            return false;
        for (VariablePosition assignedPosition: assignPositions) {
            if (assignedPosition.isOnOrAfter(start) && assignedPosition.isOnOrBefore(end))
                return true;
        }
        return false;
    }

    public boolean isMutable() {
        return !(IMMUTABLES.contains(type));
    }

    public boolean isStatic() {
        return this.modifierCode != -1 && ModifierSet.isStatic(this.modifierCode);
    }


    private static String getPackageName(String variablePackage, String type) {
        try {
            PackageManager.findClass(variablePackage, type);
            return variablePackage;
        } catch (RuntimeException e) {}
        if (Primitive.isValidType(type))
            return null;
        for (String packageName: Imports.getDefaultImportPackages()) {
            try {
                PackageManager.findClass(packageName, type);
                return packageName;
            } catch (RuntimeException e) {
            }
        }
        return null;
    }

}
