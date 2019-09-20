package edu.ncsu.visitors.parsers;

import edu.ncsu.r.RFilter;
import edu.ncsu.r.RLexer;
import edu.ncsu.r.RParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;



public class AntlrRParser {

    public static void parse(String sourceCode) {
        CharStream codeStream = CharStreams.fromString(sourceCode);
        RLexer lexer = new RLexer(codeStream);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        RFilter filter =  new RFilter(tokens);
        filter.stream();
        tokens.reset();
        RParser parser = new RParser(tokens);
        parser.setBuildParseTree(true);
        RuleContext tree = parser.prog();
        System.out.println(tree.toStringTree(parser));
    }

    public static void main(String[] args) {
        parse("x <- 5;");
    }
}
