package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ModifierSet;
import com.github.javaparser.ast.expr.Expression;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import com.google.gson.JsonObject;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Variable {
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

    /**
     * End scope of variable
     */
    protected Integer endScopeLineNumber;

    /**
     * @return Type of variable
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

    public Variable(String name, Type type, String scope) {
        this.uuid = UUID.randomUUID().toString();
        this.name = name;
        this.scope = scope;
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            this.type = refType.getType().toStringWithoutComments();
            this.arrayDimensions = ((ReferenceType) type).getArrayCount();
        } else {
            this.type = type.toStringWithoutComments();
            this.arrayDimensions = 0;
        }
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
    public Variable(String name, Type type, Integer lineNumber, Integer columnNumber, Expression initValue, Node parentNode) {
        this(name, type.toStringWithoutComments(), lineNumber, columnNumber, initValue, parentNode);
        if (type instanceof ReferenceType) {
            ReferenceType refType = (ReferenceType) type;
            this.type = refType.getType().toStringWithoutComments();
            this.arrayDimensions = ((ReferenceType) type).getArrayCount();
        } else {
            this.arrayDimensions = 0;
        }
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
        jsonObject.addProperty("type", type);
        jsonObject.addProperty("arrayDimensions", arrayDimensions);
        jsonObject.addProperty("scope", scope);
        return jsonObject;
    }

    public static String getModifier(int modifierCode) {
        if (ModifierSet.isPublic(modifierCode)) {
            return "public";
        } else if (ModifierSet.isProtected(modifierCode)) {
            return "protected";
        } else if (ModifierSet.isPrivate(modifierCode)) {
            return "private";
        } else {
            return "default";
        }
    }
}
