package edu.ncsu.visitors.helpers;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.visitors.blocks.ClassBlock;
import edu.ncsu.visitors.blocks.MethodBlock;
import edu.ncsu.visitors.blocks.Variable;
import edu.ncsu.visitors.blocks.VariablePosition;

import java.io.File;
import java.io.IOException;
import java.util.Map;

public class VisitorHelper {

    /***
     * Load the ast compilation unit of the java source file.
     * @param javaFilePath - Path of the java file.
     * @return - Compilation unit of the source file
     */
    public static CompilationUnit loadCompilationUnit(String javaFilePath) {
        File srcFile = new File(javaFilePath);
        try {
            return JavaParser.parse(srcFile, null, true);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    /***
     * Return the name of the package
     * @return
     */
    public static String getPackage(CompilationUnit compilationUnit) {
        return compilationUnit.getPackage().getName().toStringWithoutComments();
    }

    @SuppressWarnings("unchecked")
    public static void visit(VoidVisitorAdapter adapter, Expression expression, Object arg) {
        if (expression instanceof ArrayAccessExpr) {
            adapter.visit((ArrayAccessExpr) expression, arg);
        } else if (expression instanceof ArrayCreationExpr) {
            adapter.visit((ArrayCreationExpr) expression, arg);
        } else if (expression instanceof ArrayInitializerExpr) {
            adapter.visit((ArrayInitializerExpr) expression, arg);
        } else if (expression instanceof AssignExpr) {
            adapter.visit((AssignExpr) expression, arg);
        } else if (expression instanceof BinaryExpr) {
            adapter.visit((BinaryExpr) expression, arg);
        } else if (expression instanceof BooleanLiteralExpr) {
            adapter.visit((BooleanLiteralExpr) expression, arg);
        } else if (expression instanceof CastExpr) {
            adapter.visit((CastExpr) expression, arg);
        } else if (expression instanceof CharLiteralExpr) {
            adapter.visit((CharLiteralExpr) expression, arg);
        } else if (expression instanceof ClassExpr) {
            adapter.visit((ClassExpr) expression, arg);
        } else if (expression instanceof ConditionalExpr) {
            adapter.visit((ConditionalExpr) expression, arg);
        } else if (expression instanceof DoubleLiteralExpr) {
            adapter.visit((DoubleLiteralExpr) expression, arg);
        } else if (expression instanceof EnclosedExpr) {
            adapter.visit((EnclosedExpr) expression, arg);
        } else if (expression instanceof FieldAccessExpr) {
            adapter.visit((FieldAccessExpr) expression, arg);
        } else if (expression instanceof InstanceOfExpr) {
            adapter.visit((InstanceOfExpr) expression, arg);
        } else if (expression instanceof IntegerLiteralMinValueExpr) {
            adapter.visit((IntegerLiteralMinValueExpr) expression, arg);
        } else if (expression instanceof IntegerLiteralExpr) {
            adapter.visit((IntegerLiteralExpr) expression, arg);
        } else if (expression instanceof LambdaExpr) {
            adapter.visit((LambdaExpr) expression, arg);
        } else if (expression instanceof LongLiteralMinValueExpr) {
            adapter.visit((LongLiteralMinValueExpr) expression, arg);
        } else if (expression instanceof LongLiteralExpr) {
            adapter.visit((LongLiteralExpr) expression, arg);
        } else if (expression instanceof MarkerAnnotationExpr) {
            adapter.visit((MarkerAnnotationExpr) expression, arg);
        } else if (expression instanceof MethodCallExpr) {
            adapter.visit((MethodCallExpr) expression, arg);
        } else if (expression instanceof MethodReferenceExpr) {
            adapter.visit((MethodReferenceExpr) expression, arg);
        } else if (expression instanceof QualifiedNameExpr) {
            adapter.visit((QualifiedNameExpr) expression, arg);
        } else if (expression instanceof NameExpr) {
            adapter.visit((NameExpr) expression, arg);
        } else if (expression instanceof NormalAnnotationExpr) {
            adapter.visit((NormalAnnotationExpr) expression, arg);
        } else if (expression instanceof NullLiteralExpr) {
            adapter.visit((NullLiteralExpr) expression, arg);
        } else if (expression instanceof ObjectCreationExpr) {
            adapter.visit((ObjectCreationExpr) expression, arg);
        } else if (expression instanceof SingleMemberAnnotationExpr) {
            adapter.visit((SingleMemberAnnotationExpr) expression, arg);
        } else if (expression instanceof StringLiteralExpr) {
            adapter.visit((StringLiteralExpr) expression, arg);
        } else if (expression instanceof SuperExpr) {
            adapter.visit((SuperExpr) expression, arg);
        } else if (expression instanceof ThisExpr) {
            adapter.visit((ThisExpr) expression, arg);
        } else if (expression instanceof TypeExpr) {
            adapter.visit((TypeExpr) expression, arg);
        } else if (expression instanceof UnaryExpr) {
            adapter.visit((UnaryExpr) expression, arg);
        } else if (expression instanceof VariableDeclarationExpr) {
            adapter.visit((VariableDeclarationExpr) expression, arg);
        }
    }

    public static void updateVariableUsage(String variableName, VariablePosition position,
                                           MethodBlock methodBlock, ClassBlock classBlock, boolean updateAssign) {
        Map<String, Variable> fieldVariableMap = classBlock.getFieldVariables();
        boolean variableFound = false;
        if (methodBlock.getVariableDeclareMap() != null && methodBlock.getVariableDeclareMap().containsKey(variableName)){
            variableFound = methodBlock.updateVariableUsage(variableName, position, updateAssign);
        }
        if (!variableFound && fieldVariableMap.containsKey(variableName)) {
            Variable fieldVariable = fieldVariableMap.get(variableName);
            fieldVariable.insertAssignPosition(position);
            fieldVariable.insertUsedPosition(position);
            fieldVariableMap.put(variableName, fieldVariable);
        }
    }

}
