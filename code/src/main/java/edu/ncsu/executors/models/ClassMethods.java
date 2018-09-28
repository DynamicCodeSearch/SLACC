package edu.ncsu.executors.models;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.BodyDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.helpers.PackageManager;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClassMethods {

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
        File srcFile = new File(sourcePath);
        CompilationUnit compilationUnit;
        try {
            compilationUnit = JavaParser.parse(srcFile);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
        TypeDeclaration classObject = compilationUnit.getTypes().get(0);
        for (BodyDeclaration member: classObject.getMembers()) {
            if (member instanceof MethodDeclaration) {
                MethodDeclaration method = (MethodDeclaration) member;
                methodBodies.put(method.getName(), method);
            }
        }
        return methodBodies;
    }

    public ClassMethods(String sourcePath) {
        this.sourcePath = sourcePath;
        packageName = CodejamUtils.getPackageName(sourcePath);
        className = CodejamUtils.getClassName(sourcePath);
        Class clazz = PackageManager.findClass(packageName, className);
        methodBodies = getMethodBodies();
        methods = new ArrayList<>();
        for (Method method: clazz.getDeclaredMethods()) {
            if (method.getName().startsWith(Properties.GENERATED_FUNCTION_PREFIX)
                    && methodBodies.containsKey(method.getName()))
                methods.add(method);
        }
    }

    public MethodDeclaration getMethodBody(String name) {
        return getMethodBodies().get(name);
    }

    public Function getFunction(Method method) {
        MethodDeclaration ast = getMethodBody(method.getName());
        return new Function(method, ast);
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
