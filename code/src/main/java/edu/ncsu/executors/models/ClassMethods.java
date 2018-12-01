package edu.ncsu.executors.models;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.BodyDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.utils.Utils;

import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClassMethods {

    private String dataset;

    private String sourcePath;

    private String className;

    private String packageName;

    private List<Method> methods;

    private Map<String, MethodDeclaration> methodBodies;

    public List<Method> getMethods() {
        return methods;
    }

    public Map<String, MethodDeclaration> getMethodBodies() {
        if (methodBodies != null)
            return methodBodies;
        methodBodies = new HashMap<>();
        CompilationUnit compilationUnit = Utils.getCompilationUnit(sourcePath);
        TypeDeclaration classObject = compilationUnit.getTypes().get(0);
        for (BodyDeclaration member: classObject.getMembers()) {
            if (member instanceof MethodDeclaration) {
                MethodDeclaration method = (MethodDeclaration) member;
                methodBodies.put(method.getName(), method);
            }
        }
        return methodBodies;
    }

    public ClassMethods(String dataset, String sourcePath) {
        this.dataset = dataset;
        this.sourcePath = sourcePath;
        packageName = Utils.getPackageName(sourcePath);
        className = Utils.getClassName(sourcePath);
        Class clazz = PackageManager.findClass(packageName, className);
        methodBodies = getMethodBodies();
        methods = new ArrayList<>();
        for (Method method: clazz.getDeclaredMethods()) {
            if (method.getName().startsWith(Settings.GENERATED_FUNCTION_PREFIX)
                    && methodBodies.containsKey(method.getName()))
                methods.add(method);
        }
    }

    public MethodDeclaration getMethodBody(String name) {
        return getMethodBodies().get(name);
    }

    public Function getFunction(Method method) {
        MethodDeclaration ast = getMethodBody(method.getName());
        return new Function(this.dataset, method, ast, this.sourcePath);
    }

    public String getDataset() {
        return dataset;
    }

    public String getSourcePath() {
        return sourcePath;
    }

    public String getClassName() {
        return className;
    }

    public String getPackageName() {
        return packageName;
    }
}
