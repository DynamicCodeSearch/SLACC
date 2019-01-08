package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.ModifierSet;
import com.github.javaparser.ast.stmt.Statement;
import edu.ncsu.config.Settings;
import edu.ncsu.visitors.helpers.StatementHelper;

import java.util.*;



public class MethodBlock {

    /**
     * Path of the class
     */
    private String fileSource;

    /**
     * Name of the method
     */
    private String name;

    /**
     * Name of the class
     */
    private String parentClass;

    /**
     * Return type of function
     */
    private String returnType;

    /**
     * Start line of function
     */
    private Integer startLine;

    /**
     * Start column of function
     */
    private Integer startColumn;

    /**
     * End line of function
     */
    private Integer endLine;

    /**
     * End column of function
     */
    private Integer endColumn;

    /**
     * AST node for method
     */
    private MethodDeclaration methodNode;

    /**
     * Map of all variables and the lines they declared.
     */
    private Map<String, Map<Integer, Variable>> variableDeclareMap;

    /**
     * Map of all variables used on a certain line.
     */
    private Map<Integer, Set<Variable>> lineNumVariableUsageMap;

    /**
     * Groups of statements from methods
     */
    private List<List<StatementBlock>> statementGroups;

    /**
     * @return Path of file source
     */
    public String getFileSource() {
        return fileSource;
    }

    /**
     * @return Name of method
     */
    public String getName() {
        return name;
    }

    /**
     * Set name of method
     * @param name
     */
    public void setName(String name) {
        this.name = name;
    }

    /***
     * @return Name of class
     */
    public String getParentClass() {
        return parentClass;
    }

    /**
     * @return Return type of method
     */
    public String getReturnType() {
        return returnType;
    }

    /**
     * @return Start line of the method
     */
    public Integer getStartLine() {
        return startLine;
    }

    /**
     * @return Start column of the method
     */
    public Integer getStartColumn() {
        return startColumn;
    }

    /**
     * @return End line of the method
     */
    public Integer getEndLine() {
        return endLine;
    }

    /**
     * @return End column of the method
     */
    public Integer getEndColumn() {
        return endColumn;
    }

    /**
     * @return MethodAST
     */
    public MethodDeclaration getMethodNode() {
        return methodNode;
    }

    /**
     * @return Map of variable name and line numbers where the variables were declared
     */
    public Map<String, Map<Integer, Variable>> getVariableDeclareMap() {
        return variableDeclareMap;
    }

    /***
     * Initialize instace of Method Block
     * @param methodDeclaration Method AST node
     * @param fileSource Path of class file
     * @param parentClass Name of the class
     */
    public MethodBlock(MethodDeclaration methodDeclaration, String fileSource, String parentClass) {
        this.fileSource = fileSource;
        this.parentClass = parentClass;
        this.returnType = methodDeclaration.getType().toString();
        this.name = methodDeclaration.getName();
        this.startLine = methodDeclaration.getBeginLine();
        this.startColumn = methodDeclaration.getBeginColumn();
        this.endLine = methodDeclaration.getEndLine();
        this.endColumn = methodDeclaration.getEndColumn();
        this.methodNode = methodDeclaration;
    }

    public boolean isStatic() {
        return ModifierSet.isStatic(this.methodNode.getModifiers());
    }


    /**
     * Insert variable when declared.
     * @param localVariable Instance of Variable
     */
    public void insertVariableDeclare(Variable localVariable) {
        if (variableDeclareMap == null)
            variableDeclareMap = new HashMap<>();
        Map<Integer, Variable> lineVariableMap;
        if (variableDeclareMap.containsKey(localVariable.getName())) {
            lineVariableMap = variableDeclareMap.get(localVariable.getName());
        } else {
            lineVariableMap = new HashMap<>();
        }
        lineVariableMap.put(localVariable.getStartPosition().getLine(), localVariable);
        variableDeclareMap.put(localVariable.getName(), lineVariableMap);
    }

    /**
     * @return Line numbers and variables used on those lines
     */
    public Map<Integer, Set<Variable>> getLineNumVariableUsageMap() {
        return lineNumVariableUsageMap;
    }

    /**
     * Insert usage of a variable on the line
     * @param variableName Name of variable
     * @param position Position of variable
     * @return True of variable is successfully inserted.
     */
    public boolean insertVariableUsage(String variableName, VariablePosition position) {
        Variable variable = getNearestVariable(variableName, position);
        if (variable == null)
            return false;
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
        return true;
    }

    public boolean updateVariableUsage(String variableName, VariablePosition position, boolean updateAssign) {
        Variable variable = getNearestVariable(variableName, position);
        if (variable == null)
            return false;
        if (updateAssign || variable.isMutable())
            variable.insertAssignPosition(position);
        insertVariableUsage(variableName, position);
        return true;
    }

    /***
     * Retrieve the nearest variable of a name and the position
     * @param variableName Name of the variable
     * @param position Position of the variable
     * @return The variable used.
     */
    private Variable getNearestVariable(String variableName, VariablePosition position) {
        if (!variableDeclareMap.containsKey(variableName))
            throw new RuntimeException(String.format("Variable %s not found in local variables", variableName));
        ArrayList<Integer> lineNumbers = new ArrayList<>(variableDeclareMap.get(variableName).keySet());
        Collections.sort(lineNumbers);
        Variable variable = null;
        for (Integer lineNum: lineNumbers) {
            Variable currentVariable = variableDeclareMap.get(variableName).get(lineNum);
            if (currentVariable.getStartPosition().isOnOrBefore(position)) {
                variable = currentVariable;
            } else if (currentVariable.getStartPosition().isAfter(position)) {
                break;
            }
        }
        if (variable != null) {
            variable.insertUsedPosition(position);
        }
        return variable;
    }

    /**
     * @return All possible groups of statements.
     */
    public List<List<StatementBlock>> getStatementGroups() {
        if (statementGroups == null)
            createStatementGroups();
        return statementGroups;
    }

    /***
     * Create grouped statements
     */
    public void createStatementGroups() {
        statementGroups = new ArrayList<>();
        List<StatementBlock> statementBlocks = getStatements();
        List<List<StatementBlock>> groups = getStatementGroups(statementBlocks);
        for (List<StatementBlock> statementGroup: groups) {
            List<List<StatementBlock>> combinations = getCombinations(statementGroup);
            statementGroups.addAll(combinations);
        }
        if (statementBlocks != null) {
            for (StatementBlock statementBlock: statementBlocks) {
                if (statementBlock instanceof GroupedStatementBlock || statementBlock instanceof ChoiceGroupedStatementBlock) {
                    List<StatementBlock> sGroup = new ArrayList<>();
                    sGroup.add(statementBlock);
                    statementGroups.add(sGroup);
                }
            }
        }
//        for (List<StatementBlock> combination: statementGroups) {
//            System.out.println("\n**** Combination **** ");
//            for (StatementBlock statementBlock: combination) {
//                System.out.println(statementBlock.getStatementAST());
//            }
//            System.out.println("***********************\n\n");
//        }
//        System.exit(0);
    }

    /***
     * @return Statements in method.
     */
    private List<StatementBlock> getStatements() {
        List<StatementBlock> statementBlocks = new ArrayList<>();
        if (this.methodNode.getBody() == null)
            return null;
        for (Statement stmt : this.methodNode.getBody().getStmts()) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodNode.getName(), stmt, null));
        }
        return statementBlocks;
    }

    /***
     * @param statementBlocks Statement blocks
     * @return All possible statement groups for a list of statements
     */
    private List<List<StatementBlock>> getStatementGroups(List<StatementBlock> statementBlocks) {
        List<List<StatementBlock>> retList = new ArrayList<>();
        List<StatementBlock> statementGroup = new ArrayList<>();
        if (statementBlocks == null
//                || statementBlocks.size() < Settings.MIN_STATEMENT_SIZE
                || statementBlocks.isEmpty())
            return retList;
//        StatementBlock lastStatement = statementBlocks.get(statementBlocks.size()-1);
//        if (lastStatement.getStatementAST() instanceof ReturnStmt) {
//            statementBlocks = statementBlocks.subList(0, statementBlocks.size() - 1);
//        }
        for (StatementBlock statementBlock: statementBlocks) {
            statementGroup.add(statementBlock);
            if (statementBlock instanceof  ChoiceGroupedStatementBlock) {
                ChoiceGroupedStatementBlock choiceGroupedStatementBlock = ((ChoiceGroupedStatementBlock) statementBlock);
                List<StatementBlock> sBlocks;
                for (StatementBlock sBlock: choiceGroupedStatementBlock.getStatementBlocks()) {
                    sBlocks = new ArrayList<>();
                    sBlocks.add(sBlock);
                    retList.addAll(getStatementGroups(sBlocks));
                }
//                sBlocks = new ArrayList<>();
//                sBlocks.add(choiceGroupedStatementBlock);
//                retList.add(sBlocks);
            } else if (statementBlock instanceof GroupedStatementBlock) {
                retList.addAll(getStatementGroups(((GroupedStatementBlock) statementBlock).getStatementBlocks()));
            }
        }
        if (statementGroup.size() >= Settings.MIN_STATEMENT_SIZE) {
            retList.add(statementGroup);
        }
        return retList;
    }

    /***
     * @param statementGroup List of statements
     * @return All possible combinations of a group os statements.
     */
    private List<List<StatementBlock>> getCombinations(List<StatementBlock> statementGroup) {
        List<List<StatementBlock>> combinations = new ArrayList<>();
        for (int step_size = Settings.MIN_STATEMENT_SIZE; step_size < statementGroup.size(); step_size++) {
            for (int counter=0; counter <= statementGroup.size()-step_size; counter++) {
                List<StatementBlock> combination = statementGroup.subList(counter, counter + step_size);
                combinations.add(combination);
            }
        }
        combinations.add(statementGroup);
        return combinations;
    }

}
