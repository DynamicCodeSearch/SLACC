package edu.ncsu.visitors.adapters;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.ReferenceType;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.common.collect.Sets;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import edu.ncsu.config.Settings;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.JavaFormatter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.StatementHelper;

import edu.ncsu.visitors.blocks.*;
import edu.ncsu.visitors.helpers.VisitorHelper;
import org.apache.commons.lang3.StringUtils;

import java.io.*;
import java.util.*;
import java.util.logging.Logger;

public class MethodAndVariableAdapter extends VoidVisitorAdapter{

    private static final Logger LOGGER = Logger.getLogger(MethodAndVariableAdapter.class.getName());

    private static final Gson GSON = new GsonBuilder().create();

    private String dataset;

    private CompilationUnit compilationUnit;

    private String fileName;

    private CommentAdapter commentAdapter;

    private List<ClassBlock> classBlocks;

    private Set<Integer> linesCovered;

    private List<ClassBlock> getClassBlocks() {
        return classBlocks;
    }

    private MethodAndVariableAdapter(String dataset, String javaFile){
        this.dataset = dataset;
        this.linesCovered = new HashSet<>();
        this.fileName = javaFile;
        this.compilationUnit = VisitorHelper.loadCompilationUnit(fileName);
        this.commentAdapter = new CommentAdapter(fileName, compilationUnit);
        List<TypeDeclaration> types = compilationUnit.getTypes();
        String fileSource = compilationUnit.toString();
        this.classBlocks = new ArrayList<>();
        for (TypeDeclaration type: types) {
            classBlocks.add(parseTypeDeclaration(type, fileSource));
        }
    }

    private ClassBlock parseTypeDeclaration(TypeDeclaration typeDeclaration, String fileSource) {
        String className = typeDeclaration.getName();
        Map<String, Variable> fieldVariablesMap = new HashMap<>();
        List<BodyDeclaration> members = typeDeclaration.getMembers();
        List<MethodBlock> methodBlocks = new ArrayList<>();
        List<ClassBlock> innerClasses = new ArrayList<>();
        for (BodyDeclaration  member: members) {
            if (member instanceof FieldDeclaration) {
                FieldDeclaration field = (FieldDeclaration) member;
                Type fieldType = field.getType();
                for (VariableDeclarator fieldVariable : field.getVariables()) {
                    String variableName = fieldVariable.getId().getName();
                    fieldVariablesMap.put(variableName,
                            new Variable(variableName, fieldType,
                                    fieldVariable.getBeginLine(), field.getBeginColumn(), fieldVariable.getInit(),
                                    typeDeclaration, field.getModifiers()));
                }
            } else if (member instanceof MethodDeclaration) {
                MethodDeclaration method = (MethodDeclaration) member;
                MethodBlock methodBlock = new MethodBlock(method, fileSource, className);
                methodBlocks.add(methodBlock);
            } else if (member instanceof ClassOrInterfaceDeclaration) {
                innerClasses.add(parseTypeDeclaration((ClassOrInterfaceDeclaration) member, fileSource));
            }
        }
        return new ClassBlock(typeDeclaration, compilationUnit, fileName, fieldVariablesMap, methodBlocks, innerClasses);
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
            Type paramType = methodParameter.getType();
            if (paramType instanceof ReferenceType && ((ReferenceType) paramType).getType() instanceof ClassOrInterfaceType) {
                visit((ClassOrInterfaceType) ((ReferenceType) paramType).getType(), arg);
            }
            Variable parameter = new Variable(methodParameter.getId().getName(), paramType,
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
        if (type instanceof ReferenceType && ((ReferenceType) type).getType() instanceof ClassOrInterfaceType) {
            visit((ClassOrInterfaceType) ((ReferenceType) type).getType(), arg);
        }
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
        if (methodCallExpr.getScope() == null) {
            Map<String, Object> visitorArg = (Map<String, Object>) arg;
            ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
            if (classBlock.isStaticMethod(methodCallExpr.getName())) {
                methodCallExpr.setName(String.format("%s.%s", classBlock.getName(), methodCallExpr.getName()));
            }
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
            updateStaticVariable(n, methodBlock, classBlock);
            VariablePosition position = new VariablePosition(n.getBeginLine(), n.getBeginColumn());
            VisitorHelper.updateVariableUsage(n.getName(), position, methodBlock, classBlock, true);
        } else if (assignExpr.getTarget() instanceof FieldAccessExpr) {
            FieldAccessExpr t = (FieldAccessExpr) assignExpr.getTarget();
            if (t.getScope() != null && t.getScope() instanceof NameExpr &&
                    ((NameExpr) t.getScope()).getName().equals(classBlock.getName())) {
                VariablePosition position = new VariablePosition(t.getBeginLine(), t.getBeginColumn());
                NameExpr n = t.getFieldExpr();
                if (classBlock.getFieldVariables().containsKey(n.getName())) {
                    Variable fieldVariable = classBlock.getFieldVariables().get(n.getName());
                    fieldVariable.insertAssignPosition(position);
                    fieldVariable.insertUsedPosition(position);
                    classBlock.getFieldVariables().put(n.getName(), fieldVariable);
                }
            }
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
        updateStaticVariable(n, methodBlock, classBlock);
        VariablePosition position = new VariablePosition(n.getBeginLine(), n.getBeginColumn());
        VisitorHelper.updateVariableUsage(n.getName(), position, methodBlock, classBlock, false);
    }

    @Override
    public void visit(ClassOrInterfaceType type, Object arg) {
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        if (type.getScope() == null && classBlock.containsInnerClass(type.getName())) {
            type.setName(String.format("%s.%s", classBlock.getName(), type.getName()));
        }
    }

    public void visit(ObjectCreationExpr objectCreationExpr, Object arg) {
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        ClassOrInterfaceType type = objectCreationExpr.getType();
        if (type.getScope() == null && classBlock.containsInnerClass(type.getName())) {
            type.setName(String.format("%s.%s", classBlock.getName(), type.getName()));
        }
        if (objectCreationExpr.getArgs() != null) {
            for (Expression expression: objectCreationExpr.getArgs()) {
                VisitorHelper.visit(this, expression, arg);
            }
        }
    }

    private void updateStaticVariable(NameExpr n, MethodBlock methodBlock, ClassBlock classBlock) {
        String variableName = n.getName();
        if (methodBlock.getVariableDeclareMap() == null || methodBlock.getVariableDeclareMap().containsKey(variableName))
            return;
        if (classBlock.getFieldVariables().containsKey(variableName)) {
            Variable variable = classBlock.getFieldVariables().get(variableName);
            if (variable.isStatic() && !(n.getParentNode() instanceof FieldAccessExpr)) {
                n.setName(String.format("%s.%s", classBlock.getName(), n.getName()));
            }
        }
    }


    private DummyMethod makeFunction(List<StatementBlock> statementBlocks, ClassBlock classBlock, MethodBlock methodBlock) {
        Map<String, Collection<Variable>> methodVariables = StatementHelper.getUndeclaredVariables(statementBlocks, classBlock, methodBlock);
        return new DummyMethod(dataset, classBlock, methodBlock, statementBlocks, methodVariables.get("undeclared"), methodVariables.get("declared"));
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

    private void saveMetaData(List<GeneratedFunction> generatedFunctions) {
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore();
        List<JsonObject> genFuncsAsJson = new ArrayList<>();
        for (GeneratedFunction generatedFunction: generatedFunctions)
            genFuncsAsJson.add(generatedFunction.toJson());
        metadataStore.saveClassFunctionsMetadata(dataset, genFuncsAsJson);

        String packageName = compilationUnit.getPackage().getPackageName();
        String metaFolder = Utils.pathJoin(Settings.META_RESULTS_SLOC, packageName.replaceAll("\\.", File.separator));
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
        stats.put("numFunctions", generatedFunctions.size());
        slocMap.put(fileName, stats);
        try(Writer writer = new FileWriter(file)) {
            Gson gson = new GsonBuilder().create();
            gson.toJson(slocMap, writer);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    private List<GeneratedFunction> generateMethods() {
        // TODO: Make this return a bunch of functions;
        LOGGER.info(String.format("PROCESSING FOR %s", this.fileName));
        List<GeneratedFunction> functions = new ArrayList<>();
        Set<String> existingFunctions  = new HashSet<>();
        for (ClassBlock classBlock: this.getClassBlocks()) {
            for (MethodBlock methodBlock: classBlock.getMethodBlocks()) {
//                LOGGER.info(String.format("*** %s.%s ***", classBlock.getName(), methodBlock.getName()));
                Map<String, Object> visitorArg = new HashMap<>();
                visitorArg.put("class", classBlock);
                visitorArg.put("method", methodBlock);
                this.visit(methodBlock.getMethodNode(), visitorArg);
                for (List<StatementBlock> statementBlocks: methodBlock.getStatementGroups()) {
                    DummyMethod method = this.makeFunction(statementBlocks, classBlock, methodBlock);
                    List<GeneratedFunction> thisFunctions = method.makeFunctions(true, existingFunctions);
//                    System.out.println("\n**** Combination **** ");
//                    for (StatementBlock statementBlock: statementBlocks) {
//                        System.out.println(statementBlock.getStatementAST());
//                    }
//                    System.out.println(thisFunctions.size());
//                    System.out.println("***********************\n\n");
                    if (thisFunctions.size() > 0) {
                        linesCovered.addAll(getLinesCovered(method));
                        functions.addAll(thisFunctions);
                    }
                }
            }
        }
        LOGGER.info(String.format("Done. # Functions = %d", functions.size()));
        return functions;
    }

    private String saveMethods(List<GeneratedFunction> functions) {
        // TODO: Accept list of functions or a new object. Save metadata as well
        String className = Settings.GENERATED_CLASS_PREFIX + Utils.randomString();
        String packageName = VisitorHelper.getPackage(compilationUnit);
        String writePath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writePath);
        String writeFilePath = Utils.pathJoin(writePath, className + ".java");
        StringBuilder javaContent = new StringBuilder();
        javaContent.append("package ").append(packageName).append(";\n\n").
                append(Imports.defaultImports()).
                append("public class ").append(className).append(" {\n");
        for (GeneratedFunction function: functions) {
            function.setSourceFile(fileName);
            function.setGeneratedFile(writeFilePath);
            javaContent.append(function.getBody()).append("\n");
        }
        javaContent.append("}");
        File writeFile = new File(writeFilePath);
        try (PrintWriter out = new PrintWriter(writeFile)) {
            out.println(javaContent.toString());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        JavaFormatter.formatAndSave(writeFilePath);
        return writeFilePath;
    }

    public static void generateMethodsForJavaFile(String dataset, String javaFile) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(dataset, javaFile);
        List<GeneratedFunction> functions = adapter.generateMethods();
        String saveFile = adapter.saveMethods(functions);
        String packageName = adapter.compilationUnit.getPackage().getPackageName();
        String mainClassName = adapter.getMainClassName();
        adapter.saveMetaData(functions);
        LOGGER.info(String.format("Saved %s.%s to '%s'", packageName, mainClassName, saveFile));
    }

    public static List<Map<String, String>> extractMethodProps(String dataset, String javaFile, boolean skipMain) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(dataset, javaFile);
        List<Map<String, String>> methodNames = new ArrayList<>();
        for (ClassBlock classBlock: adapter.getClassBlocks()) {
            for (MethodBlock methodBlock: classBlock.getMethodBlocks()) {
                Map<String, String> props = new HashMap<>();
                if (skipMain && methodBlock.getName().equals("main"))
                    continue;
                props.put("Class", classBlock.getName());
                props.put("Package", classBlock.getCompilationUnit().getPackage().getName().toString());
                props.put("Method", methodBlock.getName());
                List<String> params = new ArrayList<String>();
                if (methodBlock.getMethodNode().getParameters() != null) {
                    for (Parameter param: methodBlock.getMethodNode().getParameters()) {
                        params.add(param.getType().toString() + " " + param.getId().getName());
                    }
                }
                props.put("Args", String.format("\"%s\"", StringUtils.join(params, ";")));
                props.put("Return", methodBlock.getReturnType());
                methodNames.add(props);
            }
        }
        return methodNames;
    }


    private static void testGenerateMethods() {
//        String fName = String.format("%s/CodeJam/Y11R5P1/aditsu/Example.java", Settings.getDatasetSourceFolder(CodejamUtils.DATASET));
//        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Dummy/subtract/Dummy.java";
        String fName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/IntroClassJava/digits/digits_65e02c1a_015/digits_65e02c1a_015.java";
        generateMethodsForJavaFile("IntroClassJava", fName);
    }

    public static void main(String[] args) {
        testGenerateMethods();
    }

}
