package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.stmt.IfStmt;
import com.github.javaparser.ast.stmt.Statement;
import com.github.javaparser.ast.stmt.SwitchStmt;
import edu.ncsu.visitors.helpers.StatementHelper;

import java.util.ArrayList;
import java.util.List;

public class ChoiceGroupedStatementBlock extends StatementBlock{

    /***
     * Optional set of StatementBlocks. Eg. If else, Switchcase
     */
    protected List<StatementBlock> statementBlocks;

    /***
     * @return Getter statementBlocks
     */
    public List<StatementBlock> getStatementBlocks() {
        return statementBlocks;
    }

    /***
     * Initialize ChoiceGroupedStatement
     * @param fileSource: Source of file
     * @param parentClass: Parent class
     * @param methodName: Name of method
     * @param statementAST: AST node of statement.
     * @param parentStatement: Parent statement block
     */
    public ChoiceGroupedStatementBlock(String fileSource, String parentClass, String methodName, Statement statementAST, StatementBlock parentStatement) {
        super(fileSource, parentClass, methodName, statementAST, parentStatement);
        statementBlocks = new ArrayList<>();
        if (statementAST instanceof IfStmt) {
            IfStmt ifStmt = (IfStmt) statementAST;
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ifStmt.getThenStmt(), this));

            if (ifStmt.getElseStmt() != null) {
                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, ((IfStmt) statementAST).getElseStmt(), this));
            }
        } else if (statementAST instanceof SwitchStmt) {
            for (Statement entry: ((SwitchStmt) statementAST).getEntries()) {
                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, entry, this));
            }
        }
    }
}
