package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.stmt.*;

import java.util.ArrayList;
import java.util.List;

import edu.ncsu.visitors.helpers.StatementHelper;

public class GroupedStatementBlock extends StatementBlock{

    /***
     * List of statement blocks in a group of statement blocks
     */
    protected List<StatementBlock> statementBlocks;

    /***
     * List of statement blocks in a grouped statement block
     * @return
     */
    public List<StatementBlock> getStatementBlocks() {
        return statementBlocks;
    }


    /***
     * @param fileSource Path of class file
     * @param parentClass Class name of parent
     * @param methodName Name of the method
     * @param statementAST AST of statement
     * @param parentStatement StatementBlock pointing to the parent
     */
    public GroupedStatementBlock(String fileSource, String parentClass, String methodName, Statement statementAST, StatementBlock parentStatement) {
        super(fileSource, parentClass, methodName, statementAST, parentStatement);
        statementBlocks = new ArrayList<>();
        if (statementAST instanceof BlockStmt) {
            List<Statement> statements = ((BlockStmt) statementAST).getStmts();
            for (Statement statement: statements) {
                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass, methodName, statement, this));
            }
        } else if (statementAST instanceof DoStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((DoStmt) statementAST).getBody(), this));
        } else if (statementAST instanceof ForeachStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((ForeachStmt) statementAST).getBody(), this));
        } else if (statementAST instanceof ForStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((ForStmt) statementAST).getBody(), this));
        }
//        else if (statementAST instanceof IfStmt) {
//            IfStmt ifStmt = (IfStmt) statementAST;
//            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                    methodName, ifStmt.getThenStmt()));
//
//            if (ifStmt.getElseStmt() != null) {
//                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                        methodName, ((IfStmt) statementAST).getElseStmt()));
//            }
//        }
        else if (statementAST instanceof LabeledStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((LabeledStmt) statementAST).getStmt(), this));
        }
//        else if (statementAST instanceof SwitchStmt) {
//            for (Statement entry: ((SwitchStmt) statementAST).getEntries()) {
//                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
//                        methodName, entry));
//            }
//        }
        else if (statementAST instanceof SwitchEntryStmt) {
            for (Statement statement: ((SwitchEntryStmt) statementAST).getStmts()) {
                statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                        methodName, statement, this));
            }
        } else if (statementAST instanceof TryStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass, methodName,
                    ((TryStmt) statementAST).getTryBlock(), this));
        } else if (statementAST instanceof  WhileStmt) {
            statementBlocks.add(StatementHelper.parseStatementNode(fileSource, parentClass,
                    methodName, ((WhileStmt) statementAST).getBody(), this));
        }
    }

    @Override
    public String toString() {
        return super.toStringHelper()
                .add("statements", statementBlocks)
                .toString();
    }
}
