package edu.ncsu.visitors.blocks;

import com.github.javaparser.ast.stmt.Statement;
import com.google.common.base.MoreObjects;

public class StatementBlock {

    /**
     * Path of class file
     */
    private String fileSource;

    /**
     * Name of class
     */
    private String parentClass;

    /**
     * Name of method
     */
    private String methodName;

    /**
     * Line number of start of statement
     */
    private Integer startLine;

    /**
     * Start column number of statement
     */
    private Integer startColumn;

    /**
     * End line of statement
     */
    private Integer endLine;

    /**
     * End column of statement
     */
    private Integer endColumn;

    /**
     * Node of statement
     */
    private Statement statementAST;

    /**
     * Parent Statement block
     */
    private StatementBlock parentStatement;


    /**
     * @return Get the file source
     */
    public String getFileSource() {
        return fileSource;
    }

    /**
     * @return Get the name of class
     */
    public String getParentClass() {
        return parentClass;
    }

    /**
     * @return Get the name of the method
     */
    public String getMethodName() {
        return methodName;
    }

    /**
     * @return Get the start line of the statement
     */
    public Integer getStartLine() {
        return startLine;
    }

    /**
     * @return Get the start column of the statement
     */
    public Integer getStartColumn() {
        return startColumn;
    }

    /**
     * @return Get the end line of the statement
     */
    public Integer getEndLine() {
        return endLine;
    }

    /**
     * @return Get the end column of the statement
     */
    public Integer getEndColumn() {
        return endColumn;
    }

    /**
     * @return Get the statement node
     */
    public Statement getStatementAST() {
        return statementAST;
    }

    /**
     * @return Get the parent statement node
     */
    public StatementBlock getParentStatement() {
        return parentStatement;
    }

    /**
     * @param fileSource Path of the class file
     * @param parentClass Name of the class
     * @param methodName Name of the method
     * @param statementAST AST node of statement
     * @param parentStatement StatementBlock pointing to the parent
     */
    public StatementBlock(String fileSource, String parentClass, String methodName, Statement statementAST, StatementBlock parentStatement) {
        this.fileSource = fileSource;
        this.parentClass = parentClass;
        this.methodName = methodName;
        this.statementAST = statementAST;
        this.startLine = statementAST.getBeginLine();
        this.startColumn = statementAST.getBeginColumn();
        this.endLine = statementAST.getEndLine();
        this.endColumn = statementAST.getEndColumn();
        this.parentStatement = parentStatement;
    }

    protected MoreObjects.ToStringHelper toStringHelper() {
        return MoreObjects.toStringHelper(this).omitNullValues()
//                .add("fileSource", fileSource)
                .add("parentClass", parentClass)
                .add("methodName", methodName)
                .add("sLine", startLine)
                .add("sCol", startColumn)
                .add("eLine", endLine)
                .add("eCol", endColumn)
                .add("statement", statementAST.toString());
    }

    @Override
    public String toString() {
        return toStringHelper().toString();
    }

}
