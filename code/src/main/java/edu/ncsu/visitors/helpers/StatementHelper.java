package edu.ncsu.visitors.helpers;

import com.github.javaparser.ast.stmt.*;
import java.util.*;

import edu.ncsu.visitors.blocks.*;

public class StatementHelper {
    public final static Set<String> BLOCK_NODE_NAMES = new HashSet<String>();

    public final static Set<String> CHOICE_BLOCK_NODE_NAMES = new HashSet<String>();

    static {
        BLOCK_NODE_NAMES.add(BlockStmt.class.getName());
//        BLOCK_NODE_NAMES.add(CatchClause.class.getName());
        BLOCK_NODE_NAMES.add(DoStmt.class.getName());
        BLOCK_NODE_NAMES.add(ForeachStmt.class.getName());
        BLOCK_NODE_NAMES.add(ForStmt.class.getName());
        BLOCK_NODE_NAMES.add(IfStmt.class.getName());
        BLOCK_NODE_NAMES.add(LabeledStmt.class.getName());
//        BLOCK_NODE_NAMES.add(LocalClassDeclarationStmt.class.getName());
        BLOCK_NODE_NAMES.add(SwitchStmt.class.getName());
        BLOCK_NODE_NAMES.add(SwitchEntryStmt.class.getName());
//        BLOCK_NODE_NAMES.add(SynchronizedStmt.class.getName());
        BLOCK_NODE_NAMES.add(TryStmt.class.getName());
        BLOCK_NODE_NAMES.add(WhileStmt.class.getName());
    }

    static {
        CHOICE_BLOCK_NODE_NAMES.add(IfStmt.class.getName());
        CHOICE_BLOCK_NODE_NAMES.add(SwitchStmt.class.getName());
    }

    public static StatementBlock parseStatementNode(String fileSource, String parentClass,
                                                    String methodName, Statement statementNode, StatementBlock parentStatment) {
        if (StatementHelper.CHOICE_BLOCK_NODE_NAMES.contains(statementNode.getClass().getName())) {
            return new ChoiceGroupedStatementBlock(fileSource, parentClass, methodName, statementNode, parentStatment);
        } else if (StatementHelper.BLOCK_NODE_NAMES.contains(statementNode.getClass().getName())) {
            return new GroupedStatementBlock(fileSource, parentClass, methodName, statementNode, parentStatment);
        } else {
            return new StatementBlock(fileSource, parentClass, methodName, statementNode, parentStatment);
        }
    }

    public static Map<String, VariablePosition> getStatementRange(List<StatementBlock> statementBlocks) {
        int last = statementBlocks.size() - 1;
        Map<String, VariablePosition> positions = new HashMap<>();
        positions.put("start", new VariablePosition(statementBlocks.get(0).getStartLine(), statementBlocks.get(0).getStartColumn()));
        positions.put("end", new VariablePosition(statementBlocks.get(last).getEndLine(), statementBlocks.get(last).getEndColumn()));
        return positions;
    }

    public static Map<String, Collection<Variable>> getUndeclaredVariables(List<StatementBlock> statementBlocks, ClassBlock classBlock, MethodBlock methodBlock) {
        Map<String, VariablePosition> positions = getStatementRange(statementBlocks);
        VariablePosition start = positions.get("start");
        VariablePosition end = positions.get("end");
        Map<Integer, Set<Variable>> methodLineVariableMap = methodBlock.getLineNumVariableUsageMap();
        Set<Variable> undeclaredVariables = new HashSet<>();
        Set<Variable> declaredVariables = new HashSet<>();
        if (methodLineVariableMap != null) {
            for (Integer lineNum: methodLineVariableMap.keySet()) {
                if (start.getLine() <= lineNum && lineNum <= end.getLine()) {
                    for (Variable variable: methodLineVariableMap.get(lineNum)) {
                        if (variable.getStartPosition().isBefore(start)) {
                            undeclaredVariables.add(variable);
                        } // else {
                        else if (variable.getEndScopeLineNumber() >= end.getLine()){
                            declaredVariables.add(variable);
                        }
                    }
                }
            }
        }
        Map<Integer, Set<Variable>> classLineVariableMap = classBlock.getLineNumVariableUsageMap();
        if (classLineVariableMap != null) {
            for (Integer lineNum: classLineVariableMap.keySet()) {
                if (start.getLine() <= lineNum && lineNum <= end.getLine()) {
                    undeclaredVariables.addAll(classLineVariableMap.get(lineNum));
                }
            }
        }
        Map<String, Collection<Variable>> variablesMap = new HashMap<>();
        variablesMap.put("undeclared", undeclaredVariables);
//        variablesMap.put("declared", declaredVariables);
        declaredVariables.addAll(undeclaredVariables);
        variablesMap.put("declared", declaredVariables);
        return variablesMap;
    }
}

