package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

public class Snipper {

    private static void snipAll() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            for (String user: Utils.listDir(problemDir)) {
                String userDir = Utils.pathJoin(problemDir, user);
                for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                    MethodAndVariableAdapter.generateMethodsForJavaFile(javaFile);
                }
            }
        }
    }

    public static void main(String[] args) {
        snipAll();
    }

}