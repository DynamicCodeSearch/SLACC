package edu.ncsu.visitors.blocks;

import java.util.*;

import com.github.javaparser.ast.stmt.ReturnStmt;
import com.google.common.base.Joiner;
import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.utils.InMemoryJavaCompiler;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;
import org.apache.commons.lang3.StringUtils;


public class DummyMethod {

    private String dataset;

    private List<StatementBlock> statementBlocks;

    private Collection<Variable> arguments;

    private Collection<Variable> returns;

    private Set<Integer> lineNumbers;

    private String packageName;

    private MethodBlock parentMethodBlock;

    private ClassBlock parentClassBlock;

    public DummyMethod(String dataset, ClassBlock parentClassBlock, MethodBlock parentMethodBlock, List<StatementBlock> statementBlocks,
                       Collection<Variable> arguments, Collection<Variable> returns) {
        this.dataset = dataset;
        this.parentClassBlock = parentClassBlock;
        this.parentMethodBlock = parentMethodBlock;
        this.statementBlocks = statementBlocks;
        this.arguments = arguments;
        this.packageName = VisitorHelper.getPackage(parentClassBlock.getCompilationUnit());
        getLineNumbers();
        setReturns(returns);

    }

    private void setReturns(Collection<Variable> returns) {
        Map<String, VariablePosition> startEnd = getStartEnd();
        VariablePosition start = startEnd.get("start");
        VariablePosition end = startEnd.get("end");
        this.returns = new HashSet<>();
        for (Variable returnVariable: returns) {
            if (returnVariable.isAssignedInRange(start, end))
                this.returns.add(returnVariable);
        }
    }

    public Set<Integer> getLineNumbers() {
        if (lineNumbers != null)
            return lineNumbers;
        lineNumbers = new HashSet<>();
        for (StatementBlock block: statementBlocks) {
            for (Variable variable: arguments)
                lineNumbers.add(variable.getStartPosition().getLine());
            for(int lineNum = block.getStartLine(); lineNum <= block.getEndLine(); lineNum++)
                lineNumbers.add(lineNum);
            StatementBlock parentBlock = block.getParentStatement();
            while (parentBlock != null) {
                lineNumbers.add(parentBlock.getStartLine());
                lineNumbers.add(parentBlock.getEndLine());
                parentBlock = parentBlock.getParentStatement();
            }
        }
        lineNumbers.add(parentMethodBlock.getStartLine());
        lineNumbers.add(parentMethodBlock.getEndLine());
        lineNumbers.addAll(parentClassBlock.getCommonLinenumbers());
        return lineNumbers;
    }

    /***
     * Get range of start and end number for all statements in function
     * @return Set of line numbers between start and end of each statement.
     */
    private Set<Integer> getStatementSpan() {
        Set<Integer> lineNumbers = new HashSet<>();
        for (StatementBlock block: statementBlocks) {
            for(int i=block.getStartLine(); i<=block.getEndLine(); i++) {
                lineNumbers.add(i);
            }
        }
        return lineNumbers;
    }

    private Map<String, VariablePosition> getStartEnd() {
        VariablePosition start = null, end = null;
        for (StatementBlock block: statementBlocks) {
            VariablePosition thisStart = new VariablePosition(block.getStartLine(), block.getStartColumn());
            VariablePosition thisEnd = new VariablePosition(block.getEndLine(), block.getEndColumn());
            if (start == null || thisStart.isBefore(start)) start = thisStart;
            if (end == null || thisEnd.isAfter(end)) end = thisEnd;
        }
        Map<String, VariablePosition> positionMap = new HashMap<>();
        positionMap.put("start", start);
        positionMap.put("end", end);
        return positionMap;
    }

    /**
     * Make comments storing metadata of the function
     * @return Comments metadata as a string
     */
    private String makeMetaComments() {
        return String.format("/**\n source:%s; lines:%s; start_end:%s\n*/",
                this.parentClassBlock.getFileSource(),
                Joiner.on(",").join(lineNumbers),
                Joiner.on(",").join(getStatementSpan()));
//
//
//        return "// " + "source: " + this.parentClassBlock.getFileSource() +
//                "\n// " + "lines: " + Joiner.on(",").join(lineNumbers) +
//                "\n// " + "start_end: " + Joiner.on(",").join(getStatementSpan()) +
//                "\n";
    }

    /***
     * Make the function body of the dummy method
     * @return Function body as string.
     */
    private String makeFunctionBody() {
        StringBuilder builder = new StringBuilder();
        for (StatementBlock block: statementBlocks) {
            builder.append(block.getStatementAST().toStringWithoutComments()).append("\n");
        }
        return builder.toString();
    }

    /***
     * Make the function arguments as string
     * @return Arguments as string
     */
    private String makeArguments() {
        StringBuilder builder = new StringBuilder();
        for (Variable argument: arguments) {
            String format = builder.length() == 0 ? "%s" : ", %s";
            builder.append(String.format(format, argument.toFunctionParameter()));
        }
        return builder.toString();
    }

    public String makeUniqueFunctionDescriptor(String argStr, String body, String returnStmt) {
        String retStmt = StringUtils.isEmpty(returnStmt) ? "" : returnStmt;
        return String.format("@rg$tr:%s;b0dy:%s%s", argStr, body, retStmt).trim();
    }

    /***
     * Make functions
     * @param isStatic: Is function static?
     * @return Entire function as string
     */
    public List<GeneratedFunction> makeFunctions(boolean isStatic, Set<String> exisitingFunctions) {
        // TODO: return an object that contains method and associated meta data which is stored in comments
        List<GeneratedFunction> functions = new ArrayList<>();
        StringBuilder builder = new StringBuilder();
        String functionBody = makeFunctionBody();
        String argStr = makeArguments();
        String argAndBody = "(" +
                argStr + ") { \n" +
//                makeMetaComments() +
                functionBody;
        Set<Integer> span = getStatementSpan();
        StatementBlock lastStatementBlock = statementBlocks.get(statementBlocks.size() - 1);
        String definitionFormat = isStatic ? "public static %s %s" : "public %s %s";
        boolean isReturnStatement = lastStatementBlock.getStatementAST() instanceof ReturnStmt;
        if (arguments.size() == 0)
            return functions;
        if (isReturnStatement) {
            String functionDescriptor = makeUniqueFunctionDescriptor(argStr, functionBody, null);
            if (exisitingFunctions.contains(functionDescriptor)) {
                return functions;
            }
            exisitingFunctions.add(functionDescriptor);
            String funcName = "func_" + Utils.randomString();
            builder.append(String.format(definitionFormat, parentMethodBlock.getReturnType(), funcName)).
                    append(argAndBody).
                    append("\n}\n\n");
            boolean status = isValidFunction(builder.toString());
            if (status) {
                GeneratedFunction genFunc = new GeneratedFunction();
                genFunc.setName(funcName);
                genFunc.setBody(builder.toString());
                genFunc.setLinesTouched(lineNumbers);
                genFunc.setSpan(span);
                FunctionVariable retVariable = FunctionVariable.getFunctionVariable(dataset, parentMethodBlock.getMethodNode().getType(), packageName);
                genFunc.setReturnMeta(retVariable.getMetadata());
                functions.add(genFunc);
            }
            return functions;
        }
        if (returns.size() == 0)
            return functions;
        String returnFormat = "return %s;";
        for (Variable returnVariable: returns) {
            FunctionVariable retVariable = FunctionVariable.getFunctionVariable(dataset, returnVariable.getAstType(), packageName);
            String returnStatement = String.format(returnFormat, returnVariable.name);
            String functionDescriptor = makeUniqueFunctionDescriptor(argStr, functionBody, returnStatement);
            if (exisitingFunctions.contains(functionDescriptor)) {
                continue;
            }
            exisitingFunctions.add(functionDescriptor);
            String funcName = "func_" + Utils.randomString();
//            System.out.println("####");
//            System.out.println(funcName);
//            System.out.println(functionDescriptor);
//            System.out.println("\n\n");
            builder.append(String.format(definitionFormat, returnVariable.toTypeString(), funcName)).
                    append(argAndBody).
                    append(returnStatement).
                    append("\n}\n\n");
            boolean status = isValidFunction(builder.toString());
            if (status) {
                GeneratedFunction genFunc = new GeneratedFunction();
                genFunc.setName(funcName);
                genFunc.setBody(builder.toString());
                genFunc.setLinesTouched(lineNumbers);
                genFunc.setSpan(span);
                genFunc.setReturnMeta(retVariable.getMetadata());
                functions.add(genFunc);
            }
            builder = new StringBuilder();
        }
        return functions;
    }

    /***
     * Check if the function is valid
     * @return True of function is valid
     */
    private boolean isValid() {
        return arguments.size() > 0 && returns.size() > 0;
    }

    /***
     * Helper function to check if a function body is valid
     * @param functionAsString Function body as string
     * @return True if valid function
     */
    private boolean isValidFunction(String functionAsString) {
        String className = Settings.TEMPORARY_CLASS_PREFIX + Utils.randomString();
        StringBuilder javaContent = new StringBuilder();
        javaContent.append("package ").append(packageName).append(";\n\n").
                append(Imports.defaultImports()).
                append("public class ").append(className).append(" {\n").
                append(functionAsString).append("}");
        try {
            return InMemoryJavaCompiler.compile(className, packageName, Settings.PROJECTS_JAVA_FOLDER,
                    javaContent.toString());
        } catch (Exception | Error e) {
            return false;
        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        String argAndBody = "(" +
                makeArguments() + ") { \n" +
                makeFunctionBody();
        if (returns.size() == 0) {
            builder.append("public void func").append(argAndBody).append("}");
        } else {
            String definitionFormat = "public %s func%d";
            String returnFormat = "return %s;";
            int i = 0;
            for (Variable returnVariable: returns) {
                builder.append(String.format(definitionFormat, returnVariable.type, ++i)).
                        append(argAndBody).
                        append(String.format(returnFormat, returnVariable.name)).
                        append("\n}\n\n");
            }
        }
        return builder.toString();
    }

}
