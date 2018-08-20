package edu.ncsu.visitors.adapters;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.NameExpr;
import com.github.javaparser.ast.expr.VariableDeclarationExpr;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.visitors.helpers.Constants;
import edu.ncsu.visitors.helpers.StatementHelper;

import edu.ncsu.visitors.blocks.*;

import java.io.*;
import java.util.*;

public class MethodAndVariableAdapter extends VoidVisitorAdapter{

    private String projectName = "default0";

    private String javaFile;

    private List<ClassBlock> classBlocks;

    private Set<Integer> linesCovered;

    public String getJavaFile() {
        return javaFile;
    }

    public List<ClassBlock> getClassBlocks() {
        return classBlocks;
    }

    public MethodAndVariableAdapter(String projectName, String javaFile) {
        this(javaFile);
        this.projectName = projectName;
    }

    public MethodAndVariableAdapter(String javaFile){
        this.javaFile = javaFile;
        this.linesCovered = new HashSet<>();
        File srcFile = new File(javaFile);
        CompilationUnit compilationUnit;
        try {
            compilationUnit = JavaParser.parse(srcFile, null, true);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
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
            ClassBlock classBlock = new ClassBlock(type, compilationUnit, fileSource, fieldVariablesMap, methodBlocks);
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
            methodBlock.insertVariableDeclare(
                    new Variable(methodParameter.getId().getName(),
                            methodParameter.getType(),
                            methodParameter.getBeginLine(), methodParameter.getBeginColumn(),
                            null, methodBlock.getMethodNode()));
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
            methodBlock.insertVariableDeclare(
                    new Variable(variableDeclarator.getId().getName(),
                            type, variableDeclarator.getBeginLine(), variableDeclarator.getBeginColumn(),
                            variableDeclarator.getInit(), getParentNode(variableDeclarator)));
            if (variableDeclarator.getInit() != null) {
                visit(variableDeclarator, arg);
            }
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
    public void visit(NameExpr n, Object arg) {
//        super.visit(n, arg);
        if (!(arg instanceof Map)){
            throw new RuntimeException("arg is not instance of Map");
        }
        Map<String, Object> visitorArg = (Map<String, Object>) arg;
        MethodBlock methodBlock = (MethodBlock) visitorArg.get("method");
        ClassBlock classBlock = (ClassBlock) visitorArg.get("class");
        Map<String, Variable> fieldVariableMap = classBlock.getFieldVariables();
        VariablePosition position = new VariablePosition(n.getBeginLine(), n.getBeginColumn());
        if (methodBlock.getVariableDeclareMap() != null && methodBlock.getVariableDeclareMap().containsKey(n.getName())){
            if (methodBlock.insertVariableUsage(n.getName(), position))
                return;
        }
        if (fieldVariableMap.containsKey(n.getName())) {
            classBlock.insertVariableUsage(n.getName(), position);
        } else if (!Constants.IGNORES.contains(n.getName())){
//            throw new RuntimeException(String.format("Is %s on line %d variable not defined?", n.getName(), n.getBeginLine()));
        }
    }

    public static void main(String[] args) {

    }

}
