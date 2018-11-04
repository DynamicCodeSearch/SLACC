package edu.ncsu.visitors.adapters;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.executors.models.Primitive;

import java.io.File;
import java.io.IOException;
import java.util.*;

public class ConstantAdapter extends VoidVisitorAdapter{

    private String javaFilePath;

    private CompilationUnit compilationUnit;

    private Map<Primitive, Set<Object>> constantsMap;

    public ConstantAdapter(String javaFilePath) {
        this.javaFilePath = javaFilePath;
        loadCompilationUnit();
        constantsMap = new HashMap<>();
        visit(compilationUnit, new Object());
    }

    private void loadCompilationUnit() {
        File javaFile = new File(javaFilePath);
        try {
            compilationUnit = JavaParser.parse(javaFile, null, false);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    private void addPrimitive(Primitive primitive, Set<Object> values) {
        Set<Object> existing = new HashSet<>();
        if (constantsMap.containsKey(primitive))
            existing = constantsMap.get(primitive);
        existing.addAll(values);
        constantsMap.put(primitive, existing);
    }

    private String getValidNumericString(String longString, String suffix) {
        longString = longString.replaceAll("_", "");
        if (suffix == null) {
            return longString;
        }
        if (longString.toLowerCase().endsWith(suffix)) {
            return longString.substring(0, longString.length()-1);
        }
        return longString;
    }


    @Override
    public void visit(IntegerLiteralExpr n, Object arg) {
        int value = Integer.decode(getValidNumericString(n.getValue(), null));
        Set<Object> values = new HashSet<Object>(Arrays.asList(value, value + 1, value - 1));
        if (value > (Short.MIN_VALUE + 1) && value < (Short.MAX_VALUE - 1))
            addPrimitive(Primitive.SHORT, values);
        addPrimitive(Primitive.INTEGER, values);
        addPrimitive(Primitive.LONG, values);
    }

    @Override
    public void visit(LongLiteralExpr n, Object arg) {
        long value = Long.decode(getValidNumericString(n.getValue(), "l"));
        Set<Object> values = new HashSet<Object>(Arrays.asList(value, value + 1, value - 1));
        if (value > (Short.MIN_VALUE + 1) && value < (Short.MAX_VALUE - 1))
            addPrimitive(Primitive.SHORT, values);
        if (value > (Integer.MIN_VALUE + 1) && value < (Integer.MAX_VALUE - 1))
            addPrimitive(Primitive.INTEGER, values);
        addPrimitive(Primitive.LONG, values);
    }

    @Override
    public void visit(DoubleLiteralExpr n, Object arg) {
        float floatValue = Float.parseFloat(getValidNumericString(n.getValue(), "f"));
        Set<Object> floatValues = new HashSet<Object>(Arrays.asList(floatValue, floatValue + 1, floatValue - 1));
        if (floatValue  > (Float.MIN_VALUE + 1) && floatValue < (Float.MAX_VALUE - 1))
            addPrimitive(Primitive.FLOAT, floatValues);
        double doubleValue = Double.parseDouble(getValidNumericString(n.getValue(), "d"));
        Set<Object> doubleValues = new HashSet<Object>(Arrays.asList(doubleValue, doubleValue + 1, doubleValue - 1));
        addPrimitive(Primitive.DOUBLE, doubleValues);
    }

    @Override
    public void visit(CharLiteralExpr c, Object arg) {
        char value = c.getValue().charAt(0);
        Set<Object> charValues = new HashSet<Object>(Arrays.asList(value, value + 1, value - 1));
        addPrimitive(Primitive.CHARACTER, charValues);
        addPrimitive(Primitive.STRING, charValues);
    }

    @Override
    public void visit(StringLiteralExpr n, Object arg) {
        Primitive primitive = Primitive.STRING;
        Set<Object> strings = new HashSet<>();
        strings.add(n.getValue());
        addPrimitive(primitive, strings);
    }

    public Map<Primitive, Set<Object>> getConstantsMap() {
        return constantsMap;
    }
}
