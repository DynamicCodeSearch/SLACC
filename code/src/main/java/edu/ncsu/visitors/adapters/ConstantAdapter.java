package edu.ncsu.visitors.adapters;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.executors.models.Primitive;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

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


    @Override
    public void visit(IntegerLiteralExpr n, Object arg) {
        Primitive primitive = Primitive.SHORT;
        Set<Object> shorts = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            shorts = constantsMap.get(primitive);
        }
        Short shortValue = Short.decode(getValidNumericString(n.getValue(), null));
        shorts.add(shortValue);
        shorts.add(shortValue + 1);
        shorts.add(shortValue - 1);
        constantsMap.put(primitive, shorts);

        primitive = Primitive.INTEGER;
        Set<Object> integers = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            integers = constantsMap.get(primitive);
        }
        Integer longValue = Integer.decode(getValidNumericString(n.getValue(), null));
        integers.add(longValue);
        integers.add(longValue + 1);
        integers.add(longValue - 1);
        constantsMap.put(primitive, integers);
    }

    @Override
    public void visit(LongLiteralExpr n, Object arg) {
        Primitive primitive = Primitive.LONG;
        Set<Object> longs = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            longs = constantsMap.get(primitive);
        }
        Long value = Long.decode(getValidNumericString(n.getValue(), "l"));
        longs.add(value);
        longs.add(value + 1);
        longs.add(value - 1);
        constantsMap.put(primitive, longs);
    }

    @Override
    public void visit(DoubleLiteralExpr n, Object arg) {
        Primitive primitive = Primitive.FLOAT;
        Set<Object> floats = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            floats = constantsMap.get(primitive);
        }
        Float floatValue = Float.parseFloat(getValidNumericString(n.getValue(), "f"));
        floats.add(floatValue);
        floats.add(floatValue + 1.0f);
        floats.add(floatValue - 1.0f);
        constantsMap.put(primitive, floats);

        primitive = Primitive.DOUBLE;
        Set<Object> doubles = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            doubles = constantsMap.get(primitive);
        }
        Double doubleValue = Double.parseDouble(getValidNumericString(n.getValue(), "d"));
        doubles.add(doubleValue);
        doubles.add(doubleValue + 1.0);
        doubles.add(doubleValue - 1.0);
        constantsMap.put(primitive, doubles);
    }

    @Override
    public void visit(CharLiteralExpr c, Object arg) {
        Primitive primitive = Primitive.CHARACTER;
        Set<Object> characters = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            characters = constantsMap.get(primitive);
        }
        Character value = c.getValue().charAt(0);
        characters.add(value);
        characters.add(value - 1);
        characters.add(value + 1);
        constantsMap.put(primitive, characters);
    }

    @Override
    public void visit(StringLiteralExpr n, Object arg) {
        Primitive primitive = Primitive.STRING;
        Set<Object> strings = new HashSet<>();
        if (constantsMap.containsKey(primitive)) {
            strings = constantsMap.get(primitive);
        }
        strings.add(n.getValue());
        constantsMap.put(primitive, strings);
    }

    public Map<Primitive, Set<Object>> getConstantsMap() {
        return constantsMap;
    }

    public String getValidNumericString(String longString, String suffix) {
        longString = longString.replaceAll("_", "");
        if (suffix == null) {
            return longString;
        }
        if (longString.toLowerCase().endsWith(suffix)) {
            return longString.substring(0, longString.length()-1);
        }
        return longString;
    }

}
