package edu.ncsu.executors.models;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.executors.helpers.UserDefinedObjects;
import edu.ncsu.visitors.blocks.Variable;
import org.apache.commons.lang3.StringUtils;

import java.util.ArrayList;
import java.util.List;

public class Constructor {

    private String packageName;

    private String className;

    private String scope;

    private List<FunctionVariable> parameters = new ArrayList<>();

    public String getPackageName() {
        return packageName;
    }

    public String getClassName() {
        return className;
    }

    public String getScope() {
        return scope;
    }

    public List<FunctionVariable> getParameters() {
        return parameters;
    }

    private Constructor(String packageName, String className) {
        this.packageName = packageName;
        this.className = className;
    }

    public static Constructor getConstructor(String dataset, String packageName, String className) {
        UserDefinedObjects udo = UserDefinedObjects.getUserDefinedObjects(dataset);
        JsonObject classObject = udo.getClassObject(packageName, className);
        if (udo.canBeFuzzed(classObject)) {
            Constructor constructor = new Constructor(packageName, className);
            for (JsonElement constructorJSON: classObject.getAsJsonArray("constructors")) {
                JsonObject constructorObj = constructorJSON.getAsJsonObject();
                constructor.scope = constructorObj.get("scope").getAsString();
                if (constructorObj.get("isValid").getAsBoolean()
                        && constructorObj.getAsJsonArray("parameters").size() > constructor.parameters.size()) {
                    constructor.parameters = new ArrayList<>();
                    for (JsonElement parameter: constructorObj.getAsJsonArray("parameters")) {
                        constructor.parameters.add(FunctionVariable.fromJSON(dataset, parameter.getAsJsonObject()));
                    }
                }
            }
            return constructor;
        }
        return null;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        if (!scope.equals(Variable.DEFAULT)) {
            sb.append(scope).append(" ");
        }
        if (packageName != null) {
            sb.append(packageName).append(".");
        }
        sb.append(className).append("(");
        if (parameters.size() > 0) {
            sb.append(StringUtils.join(parameters, ", "));
        }
        sb.append(")");
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println(getConstructor(CodejamUtils.DATASET, "CodeJam.Y11R5P1.Egor", "Point"));
    }
}
