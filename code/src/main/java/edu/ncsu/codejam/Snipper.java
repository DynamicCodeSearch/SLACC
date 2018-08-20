package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;
import edu.ncsu.visitors.blocks.ClassBlock;
import edu.ncsu.visitors.blocks.Variable;

import java.util.Map;

public class Snipper {

    public static void snipAll() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            for (String user: Utils.listDir(problemDir)) {
                String packageName = String.format("%s.%s", problem, user);
                String userDir = Utils.pathJoin(problemDir, user);
                for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                    MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(packageName, javaFile);
                }
                System.out.println(user);
            }
        }
    }

    public static void extractClasses(String javaFile, String packageName) {
        MethodAndVariableAdapter adapter = new MethodAndVariableAdapter(packageName, javaFile);
        for (ClassBlock classBlock: adapter.getClassBlocks()) {
            if (classBlock.getName().equals("Segment")) {
                Map<String, Variable> variableMap = classBlock.getFieldVariables();
                for (String variableName: variableMap.keySet()) {
                    System.out.println(variableName);
                    System.out.println(variableMap.get(variableName).getType());
                }
            }
        }
    }

    public static void main(String[] args) {
//        snipAll();
        extractClasses("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Y11R5P1/Egor/Main.java", "Y11R5P1.Egor");
    }

}