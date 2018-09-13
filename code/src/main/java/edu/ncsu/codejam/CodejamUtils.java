package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CodejamUtils {

    public static List<String> listGeneratedFiles() {
        List<String> generatedFiles = new ArrayList<>();
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            generatedFiles.addAll(listGeneratedFiles(problemDir));
        }
        return generatedFiles;
    }

    private static List<String> listGeneratedFiles(String problemPath) {
        List<String> generatedFiles = new ArrayList<>();
        String[] users = Utils.listDir(problemPath);
        Arrays.sort(users);
        for (String user: users) {
            String userDir = Utils.pathJoin(problemPath, user);
            for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                String fileName = Utils.getFileName(javaFile);
                if (fileName.startsWith(Properties.GENERATED_CLASS_PREFIX)) {
                    generatedFiles.add(javaFile);
                }
            }
        }
        return generatedFiles;
    }

    public static String getPackageName(String javaFilePath) {
        try {
            String packageRelativePath = javaFilePath.split(Properties.CODEJAM_JAVA_FOLDER)[1].substring(1);
            int separatorIndex = packageRelativePath.lastIndexOf(File.separator);
            if (separatorIndex == -1) {
                return "default";
            } else {
                return packageRelativePath.substring(0, separatorIndex).replaceAll(File.separator, ".");
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static String getClassName(String javaFilePath) {
        String classPath = javaFilePath.split("\\.java")[0].trim();
        int separatorIndex = classPath.lastIndexOf(File.separator);
        return classPath.substring(separatorIndex + 1);
    }

}
