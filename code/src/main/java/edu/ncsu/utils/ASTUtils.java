package edu.ncsu.utils;

import edu.ncsu.config.Settings;
import gumtree.spoon.AstComparator;
import gumtree.spoon.diff.Diff;
import gumtree.spoon.diff.operations.Operation;
import gumtree.spoon.diff.operations.UpdateOperation;
import spoon.Launcher;
import spoon.MavenLauncher;
import spoon.reflect.CtModel;
import spoon.reflect.code.CtBlock;
import spoon.reflect.declaration.CtClass;
import spoon.reflect.declaration.CtElement;
import spoon.reflect.declaration.CtType;
import spoon.reflect.declaration.CtTypeMember;
import spoon.support.reflect.declaration.CtMethodImpl;

import java.util.Iterator;

public class ASTUtils {

//    private static CtModel model;
//
//    public static CtModel getModel() {
//
//        if (model == null) {
////            MavenLauncher launcher = new MavenLauncher(Settings.PROJECTS_HOME, MavenLauncher.SOURCE_TYPE.APP_SOURCE);
////            launcher.buildModel();
////            model = launcher.getModel();
////            Launcher launcher = new Launcher();
//            MavenLauncher launcher = new MavenLauncher(Settings.PROJECTS_HOME, MavenLauncher.SOURCE_TYPE.APP_SOURCE);
//            model = launcher.buildModel();
//        }
//        return model;
//    }

    private final static AstComparator AST_COMPARATOR = new AstComparator();

    private static String createClass(String className, String functionBody) {
        return String.format("public class %s { %s }", className, functionBody);
    }

    public static CtBlock getMethodBody(String className, String functionName, String functionBody) {
        String classSource = createClass(className, functionBody);
        CtClass l = Launcher.parseClass(classSource);
        for (Object member : l.getTypeMembers()) {
            if (member instanceof CtMethodImpl && ((CtMethodImpl) member).getSimpleName().equals(functionName)) {
                CtMethodImpl method = (CtMethodImpl) member;
                return method.getBody();
            }
        }
        return null;
    }

    public static Diff compareAST(CtElement tree1, CtElement tree2) {
        return AST_COMPARATOR.compare(tree1, tree2);
    }

    private static boolean isTypeOne(Diff diff) {
        return diff.getRootOperations().size() == 0;
    }

    public static boolean isTypeOne(CtElement tree1, CtElement tree2) {
        Diff diff = compareAST(tree1, tree2);
        return isTypeOne(diff);
    }

    public static boolean isTypeTwo(CtElement tree1, CtElement tree2) {
        Diff diff = compareAST(tree1, tree2);
        if (isTypeOne(diff))
            return true;
        CtElement ctElement = diff.commonAncestor();
        Iterator iterator = diff.getRootOperations().iterator();
        while (iterator.hasNext()) {
            Operation operation = (Operation) iterator.next();
            if (operation instanceof UpdateOperation) {
                if (operation.getNode().equals(ctElement))
                    break;
            } else {
                return false;
            }
        }
        return true;
    }

    public static void testType1() {
        String functionBody1= "public static DoubleObj func_1badf6228d4043dca6a442b0db0f9e65(DoubleObj n, DoubleObj m, DoubleObj c){\\n    if (m.value > c.value) {\\n        n.value = c.value;\\n    } else if (m.value < c.value) {\\n        n.value = m.value;\\n    }\\n    return n;\\n}";
        String className1 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName1 = "func_1badf6228d4043dca6a442b0db0f9e65";

        String functionBody2 = "public static DoubleObj func_1badf6228d4043dca6a442b0db0f9e65(DoubleObj n, DoubleObj m, DoubleObj c){\\n    if (m.value > c.value) {\\n        n.value = c.value;\\n    } else if (m.value < c.value) {\\n        n.value = m.value;\\n    }\\n    return n;\\n}";
        String className2 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName2 = "func_1badf6228d4043dca6a442b0db0f9e65";

        CtElement tree1 = getMethodBody(className1, functionName1, functionBody1);
        CtElement tree2 = getMethodBody(className2, functionName2, functionBody2);

        Diff diff = compareAST(tree1, tree2);

        System.out.println(isTypeOne(tree1, tree2));
        System.out.println(isTypeTwo(tree1, tree2));
    }


    public static void testType2() {
        String functionBody1= "public static DoubleObj func_1badf6228d4043dca6a442b0db0f9e65(DoubleObj n, DoubleObj m, DoubleObj c){\\n    if (m.value > c.value) {\\n        n.value = c.value;\\n    } else if (m.value < c.value) {\\n        n.value = m.value;\\n    }\\n    return n;\\n}";
        String className1 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName1 = "func_1badf6228d4043dca6a442b0db0f9e65";

        String functionBody2 = "public static DoubleObj func_fdf076c3eddf452d84e9e9b8b5053429(DoubleObj m, DoubleObj a, DoubleObj b){\\n    if (a.value > b.value) {\\n        m.value = b.value;\\n    } else if (a.value < b.value) {\\n        m.value = a.value;\\n    }\\n    return m;\\n}";
        String className2 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName2 = "func_fdf076c3eddf452d84e9e9b8b5053429";

        CtElement tree1 = getMethodBody(className1, functionName1, functionBody1);
        CtElement tree2 = getMethodBody(className2, functionName2, functionBody2);

//        Diff diff = compareAST(tree1, tree2);

        System.out.println(isTypeOne(tree1, tree2));
        System.out.println(isTypeTwo(tree1, tree2));
    }


    public static void testType3() {
        String functionBody1= "public static DoubleObj func_1badf6228d4043dca6a442b0db0f9e65(DoubleObj n, DoubleObj m, DoubleObj c){\\n    if (m.value > c.value) {\\n        n.value = c.value;\\n    } else if (m.value < c.value) {\\n        n.value = m.value + 1;\\n    }\\n    return n;\\n}";
        String className1 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName1 = "func_1badf6228d4043dca6a442b0db0f9e65";

        String functionBody2 = "public static DoubleObj func_fdf076c3eddf452d84e9e9b8b5053429(DoubleObj m, DoubleObj a, DoubleObj b){\\n    if (a.value > b.value) {\\n        m.value = b.value;\\n    } else if (a.value < b.value) {\\n        m.value = a.value;\\n    }\\n    return m;\\n}";
        String className2 = "permutated_class_9fec5b84d2284d3ca954ec26f791a541";
        String functionName2 = "func_fdf076c3eddf452d84e9e9b8b5053429";

        CtElement tree1 = getMethodBody(className1, functionName1, functionBody1);
        CtElement tree2 = getMethodBody(className2, functionName2, functionBody2);

        Diff diff = compareAST(tree1, tree2);

        System.out.println(diff);
    }

    public static void main(String[] args) {
//        getAST("", "", "");
        testType2();
    }

}
