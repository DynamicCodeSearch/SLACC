package edu.ncsu.visitors.adapters;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.common.collect.Sets;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Properties;
import edu.ncsu.utils.JavaFormatter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.StatementHelper;

import edu.ncsu.visitors.blocks.*;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class MethodAndVariableAdapter extends VoidVisitorAdapter{

    private static final Logger LOGGER = Logger.getLogger(MethodAndVariableAdapter.class.getName());

    private static final Gson GSON = new GsonBuilder().create();

    private CompilationUnit compilationUnit;

    private String fileName;

    private CommentAdapter commentAdapter;

    private List<ClassBlock> classBlocks;

    private Set<Integer> linesCovered;

    private List<ClassBlock> getClassBlocks() {
        return classBlocks;
    }

    private MethodAndVariableAdapter(String javaFile){
        this.linesCovered = new HashSet<>();
        this.fileName = javaFile;
        compilationUnit = VisitorHelper.loadCompilationUnit(fileName);
        commentAdapter = new CommentAdapter(fileName, compilationUnit);
        List<TypeDeclaration> types = compilationUnit.getTypes();
        String fileSource = compilationUnit.toString();
        this.classBlocks = new ArrayList<>();
        for (TypeDeclaration type: types) {
            String className = type.getName();
            Map<String, Variable> fieldVariablesMap = new HashMap<>();
            List<BodyDeclaration> members = type.getMembers();
            List<MethodBlock> methodBlocks = new ArrayList<>();
            for (BodyDeclaration  member: members) {
                if (member instanceof FieldDeclaration) {
                    FieldDeclaration field = (FieldDeclaration) member;
                    Type fieldType = field.getType();
                    for (VariableDeclarator fieldVariable : field.getVariables()) {
                        String variableName = fieldVariable.getId().getName();
                        fieldVariablesMap.put(variableName,
                                new Variable(variableName, fieldType,
                                        fieldVariable.getBeginLine(), field.getBeginColumn(), fieldVariable.getInit(),
                                        type));
                    }
                } else if (member instanceof MethodDeclaration) {
                    MethodDeclaration method = (MethodDeclaration) member;
                    MethodBlock methodBlock = new MethodBlock(method, fileSource, className);
                    methodBlocks.add(methodBlock);
                }
            }
            ClassBlock classBlock = new ClassBlock(type, compilationUnit, fileName, fieldVariablesMap, methodBlocks);
            classBlocks.add(classBlock);
        }
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(MethodDeclaration methodDeclaration, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        if (methodDeclaration.getBody() == null){
            return;
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        List<Parameter> methodParameters = methodDeclaration.getParameters();
        for (Parameter methodParameter: methodParameters) {
            Variable parameter = new Variable(methodParameter.getId().getName(),
                    methodParameter.getType(),
                    methodParameter.getBeginLine(), methodParameter.getBeginColumn(),
                    null, methodBlock.getMethodNode());
            if (methodParameter.isVarArgs())
                parameter.setArrayDimensions(parameter.getArrayDimensions() + 1);
            methodBlock.insertVariableDeclare(parameter);
        }
        visitorArg.put("method", methodBlock);
        visit(methodDeclaration.getBody(), visitorArg);
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(VariableDeclarationExpr variableDeclaratorExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        Type type = variableDeclaratorExpr.getType();
        for (VariableDeclarator variableDeclarator: variableDeclaratorExpr.getVars()) {
            Variable variable = new Variable(variableDeclarator.getId().getName(),
                    type, variableDeclarator.getBeginLine(), variableDeclarator.getBeginColumn(),
                    variableDeclarator.getInit(), getParentNode(variableDeclarator));
            methodBlock.insertVariableDeclare(variable);
            methodBlock.insertVariableUsage(variable.getName(), variable.getStartPosition());
            variable.insertAssignPosition(variable.getStartPosition());
            if (variableDeclarator.getInit() != null) {
                visit(variableDeclarator, arg);
            }
        }
    }

    @SuppressWarnings("unchecked")
    @Override
    public void visit(MethodCallExpr methodCallExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        VisitorHelper.visit(this, methodCallExpr.getScope(), visitorArg);
        if (methodCallExpr.getArgs() != null) {
            for (Expression param: methodCallExpr.getArgs())
                VisitorHelper.visit(this, param, arg);
        }
    }

    private Node getParentNode(VariableDeclarator variableDeclarator) {
        Node parentNode = variableDeclarator.getParentNode();
        while (parentNode != null  && ! StatementHelper.BLOCK_NODE_NAMES.contains(parentNode.getClass().getName())) {
            parentNode = parentNode.getParentNode();
        }
        return parentNode;

    }


    @SuppressWarnings("unchecked")
    @Override
    public void visit(AssignExpr assignExpr, Object arg) {
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        visitorArg.put("method", methodBlock);
        visitorArg.put("class", classBlock);
        if (assignExpr.getTarget() instanceof NameExpr) {
            NameExpr n = (NameExpr) assignExpr.getTarget();
            VariablePosition position = new VariablePosition(n.getBeginLine(), n.getBeginColumn());
            VisitorHelper.updateVariableUsage(n.getName(), position, methodBlock, classBlock, true);
        }
        VisitorHelper.visit(this, assignExpr.getTarget(), visitorArg);
        VisitorHelper.visit(this, assignExpr.getValue(), visitorArg);
    }


    @SuppressWarnings("unchecked")
    @Override
    public void visit(NameExpr n, Object arg) {
//        super.visit(n, arg);
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        VariablePosition position = new VariablePosition(n.getBeginLine(), n.getBeginColumn());
        VisitorHelper.updateVariableUsage(n.getName(), position, methodBlock, classBlock, false);
    }

    private DummyMethod makeFunction(List<StatementBlock> statementBlocks, ClassBlock classBlock, MethodBlock methodBlock) {
        Map<String, Collection<Variable>> methodVariables = StatementHelper.getUndeclaredVariables(statementBlocks, classBlock, methodBlock);
        return new DummyMethod(classBlock, methodBlock, statementBlocks, methodVariables.get("undeclared"), methodVariables.get("declared"));
    }

    private Set<Integer> getLinesCovered(DummyMethod method) {
        Set<Integer> methodLineNumbers = method.getLineNumbers();
        return Sets.intersection(methodLineNumbers, commentAdapter.getSourceCodeLines());
    }

    private String getMainClassName() {
        for (TypeDeclaration type: compilationUnit.getTypes()) {
            if (Variable.getModifier(type.getModifiers()).equals(Variable.PUBLIC))
                return type.getName();
        }
        return null;
    }

    private void saveMetaData(int numFunctions) {
        String packageName = compilationUnit.getPackage().getPackageName();
        String metaFolder = Utils.pathJoin(Properties.META_RESULTS, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(metaFolder);
        File file = new File(Utils.pathJoin(metaFolder, "sloc.json"));
        Set<Integer> sloc = commentAdapter.getSourceCodeLines();
        Map<String, Map<String, Object>> slocMap;
        if (file.exists()) {
            try {
                Reader reader = new FileReader(file);
                slocMap = GSON.fromJson(reader, new TypeToken<Map<String, Map<String, Object>>>(){}.getType());
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
        } else {
            slocMap = new HashMap<>();
        }
        Map<String, Object> stats = new HashMap<>();
        stats.put("sloc", sloc);
        stats.put("linesCovered", linesCovered);
        stats.put("numFunctions", numFunctions);
        slocMap.put(fileName, stats);
        try(Writer writer = new FileWriter(file)) {
            Gson gson = new GsonBuilder().create();
            gson.toJson(slocMap, writer);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private List<String> generateMethods() {
        LOGGER.info(String.format("PROCESSING FOR %s", this.fileName));
        List<String> functions = new ArrayList<>();
        for (ClassBlock classBlock: this.getClassBlocks()) {
            for (MethodBlock methodBlock: classBlock.getMethodBlocks()) {
//                LOGGER.info(String.format("*** %s.%s ***", classBlock.getName(), methodBlock.getName()));
                Map<String, Object> visitorArg = new HashMap<>();
                visitorArg.put("class", classBlock);
                visitorArg.put("method", methodBlock);
                this.visit(methodBlock.getMethodNode(), visitorArg);
                for (List<StatementBlock> statementBlocks: methodBlock.getStatementGroups()) {
//                    System.out.println("\n**** Combination **** ");
//                    for (StatementBlock statementBlock: statementBlocks) {
//                        System.out.println(statementBlock.getStatementAST());
//                    }
//                    System.out.println("***********************\n\n");
                    DummyMethod method = this.makeFunction(statementBlocks, classBlock, methodBlock);
                    List<String> thisFunctions = method.makeFunctions(true);
                    if (thisFunctions != null && thisFunctions.size() > 0) {
                        linesCovered.addAll(getLinesCovered(method));
                        functions.addAll(thisFunctions);
                    }
                }
            }
        }
        LOGGER.info(String.format("Done. # Functions = %d", functions.size()));
        return functions;
    }

    private String saveMethods(List<String> functions) {
        String className = Properties.GENERATED_CLASS_PREFIX + Utils.randomString();
        String packageName = VisitorHelper.getPackage(compilationUnit);
        String writePath = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writePath);
        StringBuilder javaContent = new StringBuilder();
        javaContent.append("package ").append(packageName).append(";\n\n").
                append(Imports.defaultImports()).
                append("public class ").append(className).append(" {\n");
        for (String function: functions) {
            javaContent.append(function).append("\n");
        }
        javaContent.append("}");
        String fileName = Utils.pathJoin(writePath, className + ".java");
        File writeFile = new File(fileName);
        try (PrintWriter out = new PrintWriter(writeFile)) {
            out.println(javaContent.toString());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        JavaFormatter.formatAndSave(fileName);
        return fileName;
    }

    public static void generateMethodsForJavaFile(String javaFile) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(javaFile);
        List<String> functions = adapter.generateMethods();
        String saveFile = adapter.saveMethods(functions);
        String packageName = adapter.compilationUnit.getPackage().getPackageName();
        String mainClassName = adapter.getMainClassName();
        adapter.saveMetaData(functions.size());
        LOGGER.info(String.format("Saved %s.%s to '%s'", packageName, mainClassName, saveFile));
    }

    private static void testGenerateMethods() {
        String fName = String.format("%s/Y11R5P1/Egor1/Main0.java", Properties.CODEJAM_JAVA_FOLDER);
        generateMethodsForJavaFile(fName);
    }

    public static void main(String[] args) {
        testGenerateMethods();
    }

}
