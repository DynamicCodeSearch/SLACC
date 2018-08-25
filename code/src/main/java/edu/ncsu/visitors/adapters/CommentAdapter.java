package edu.ncsu.visitors.adapters;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.comments.BlockComment;
import com.github.javaparser.ast.comments.Comment;
import com.github.javaparser.ast.comments.JavadocComment;
import com.github.javaparser.ast.comments.LineComment;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class CommentAdapter extends VoidVisitorAdapter {

    private String javaFile;

    private Set<Integer> nonSourceCodeLineNumbers = new HashSet<>();

    private CompilationUnit compilationUnit;

    private List<String> lines;

    public CommentAdapter(String javaFile) {
        this.javaFile = javaFile;
        this.compilationUnit = VisitorHelper.loadCompilationUnit(javaFile);
        initialize();
    }

    public CommentAdapter(String javaFile, CompilationUnit compilationUnit) {
        this.javaFile = javaFile;
        this.compilationUnit = compilationUnit;
        initialize();
    }

    private void initialize() {
        lines = Utils.readLinesFromFile(javaFile);
        if (lines != null) {
            int i = 1;
            for (String line: lines) {
                if (line.replaceAll("\\s+", "").length() == 0) {
                    nonSourceCodeLineNumbers.add(i);
                }
                i += 1;
            }
        }
        for (Comment comment: compilationUnit.getComments()) {
            if (comment instanceof LineComment) {
                visit((LineComment) comment, null);
            } else if (comment instanceof BlockComment) {
                visit((BlockComment) comment, null);
            } else if (comment instanceof JavadocComment) {
                visit((JavadocComment) comment, null);
            }
        }
    }

    @Override
    public void visit(LineComment n, Object arg) {
        int lineNumber =  n.getBeginLine();
        String line = lines.get(lineNumber - 1);
        if (line.replaceAll("\\s+", "").startsWith("//"))
            nonSourceCodeLineNumbers.add(lineNumber);
    }

    @Override
    public void visit(BlockComment n, Object arg) {
        int beginLine = n.getBeginLine();
        int endLine = n.getEndLine();
        for (int i=beginLine; i <= endLine; i++)
            nonSourceCodeLineNumbers.add(i);
    }

    @Override
    public void visit(JavadocComment n, Object arg) {
        int beginLine = n.getBeginLine();
        int endLine = n.getEndLine();
        for (int i=beginLine; i <= endLine; i++)
            nonSourceCodeLineNumbers.add(i);
    }

    public Set<Integer> getSourceCodeLines() {
        int startLine = compilationUnit.getBeginLine();
        int endLine = compilationUnit.getEndLine();
        Set<Integer> sourceCodeLines = new HashSet<>();
        for (int i=startLine; i <= endLine; i++) {
            if (!nonSourceCodeLineNumbers.contains(i))
                sourceCodeLines.add(i);
        }
        return sourceCodeLines;
    }

}
