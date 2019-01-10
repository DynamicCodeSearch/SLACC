package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.ImportDeclaration;
import com.github.javaparser.ast.body.TypeDeclaration;
import java.util.*;

import edu.ncsu.visitors.blocks.*;

public class ClassBlock {

    /***
     * CompilationUnit of the parsed file
     */
    private CompilationUnit compilationUnit;

    private Set<Integer> commonLinenumbers;

    /***
     * Path of file in class
     */
    private String fileSource;

    /***
     * Name of the package.
     */
    private String packageName;

    /***
     * Name of the class
     */
    private String name;

    /**
     * Map of field member variables
     */
    private Map<String, Variable> fieldVariablesMap;

    /**
     * Set of variables used on a particular line number.
     */
    private Map<Integer, Set<Variable>> lineNumVariableUsageMap;


    /***
     * List of methods in class.
     */
    private List<MethodBlock> methodBlocks;

    /***
     * List of inner classes
     */
    private List<ClassBlock> innerClasses;

    /***
     * Class AST
     */
    private TypeDeclaration classDeclaration;


    /***
     * @return Get filePath
     */
    public String getFileSource() {
        return fileSource;
    }


    /***
     * @return Get name of class
     */
    public String getName() {
        return name;
    }

    /***
     * @param name Set name of class
     */
    public void setName(String name) {
        this.name = name;
    }

    /***
     * @return Get field variables
     */
    public Map<String, Variable> getFieldVariables() {
        return fieldVariablesMap;
    }

    /***
     * @param fieldVariablesMap  Set field variables
     */
    public void setFieldVariables(Map<String, Variable> fieldVariablesMap) {
        this.fieldVariablesMap = fieldVariablesMap;
    }

    /***
     * @return Get method blocks in class
     */
    public List<MethodBlock> getMethodBlocks() {
        return methodBlocks;
    }


    /**
     * @return The name of the package
     */
    public String getPackageName() {
        return packageName;
    }

    /***
     * @return Get class AST Node
     */
    public TypeDeclaration getClassDeclaration() {
        return classDeclaration;
    }

    /***
     * @return Get Variables used on each line
     */
    public Map<Integer, Set<Variable>> getLineNumVariableUsageMap() {
        return lineNumVariableUsageMap;
    }

    /**
     * @return Get instance of parsed CompilationUnit
     */
    public CompilationUnit getCompilationUnit() {
        return compilationUnit;
    }

    public Set<Integer> getCommonLinenumbers() {
        if (commonLinenumbers != null)
            return commonLinenumbers;
        commonLinenumbers = new HashSet<>();
        if (compilationUnit.getPackage() != null) {
            commonLinenumbers.add(compilationUnit.getPackage().getBeginLine());
            commonLinenumbers.add(compilationUnit.getPackage().getEndLine());
        }
        Set<String> defaultImportKeys = Imports.getDefaultImportKeys();
        for (ImportDeclaration importDeclaration: compilationUnit.getImports()) {
            String importName = importDeclaration.getName().toString();
            for (String defaultImportKey: defaultImportKeys) {
                if (importName.startsWith(defaultImportKey)) {
                    commonLinenumbers.add(importDeclaration.getBeginLine());
                    commonLinenumbers.add(importDeclaration.getEndLine());
                    break;
                }
            }
        }
        commonLinenumbers.add(getClassDeclaration().getBeginLine());
        commonLinenumbers.add(getClassDeclaration().getEndLine());
        return commonLinenumbers;
    }

    /***
     * Insert usage of a variable in memory
     * @param variableName Name of Variable
     * @param position Position of Variable
     */
    public void insertVariableUsage(String variableName, VariablePosition position) {
        Variable variable = fieldVariablesMap.get(variableName);
        variable.insertUsedPosition(position);
        if (lineNumVariableUsageMap == null)
            lineNumVariableUsageMap = new HashMap<>();
        Set<Variable> variables;
        if (lineNumVariableUsageMap.containsKey(position.getLine())) {
            variables = lineNumVariableUsageMap.get(position.getLine());
        } else {
            variables = new HashSet<>();
        }
        variables.add(variable);
        lineNumVariableUsageMap.put(position.getLine(), variables);
    }

    /***
     *
     * @param classDeclaration AST of class node
     * @param compilationUnit Instance of the parsed compilationUnit
     * @param fileSource  Path of class
     * @param fieldVariablesMap Map of member variables
     * @param methodBlocks List of method blocks
     */
    public ClassBlock(TypeDeclaration classDeclaration, CompilationUnit compilationUnit, String fileSource,
                      Map<String, Variable> fieldVariablesMap, List<MethodBlock> methodBlocks,
                      List<ClassBlock> innerClasses) {
        this.classDeclaration = classDeclaration;
        this.compilationUnit = compilationUnit;
        this.fileSource = fileSource;
        this.name = classDeclaration.getName();
        this.fieldVariablesMap = fieldVariablesMap;
        this.methodBlocks = methodBlocks;
        this.innerClasses = innerClasses;
    }

    /***
     * Return true if there is a static method of this name
     * @param methodName
     * @return
     */
    public boolean isStaticMethod(String methodName) {
        // TODO: update this to support method overloading as well.
        for (MethodBlock methodBlock: this.methodBlocks) {
            if (methodBlock.getName().equals(methodName) && methodBlock.isStatic())
                return true;
        }
        return false;
    }

    public boolean containsInnerClass(String name) {
        for (ClassBlock classBlock: this.innerClasses) {
            if (classBlock.getName().equals(name))
                return true;
        }
        return false;
    }

}
