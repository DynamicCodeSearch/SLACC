package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CodejamUtils {

    public static List<String> listGeneratedFiles() {
        List<String> generatedFiles = new ArrayList<>();
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            String[] users = Utils.listDir(problemDir);
            Arrays.sort(users);
            for (String user: users) {
                String userDir = Utils.pathJoin(problemDir, user);
                for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                    String fileName = Utils.getFileName(javaFile);
                    if (!fileName.startsWith(Properties.GENERATED_CLASS_PREFIX))
                        generatedFiles.add(javaFile);
                }
            }
        }
        return generatedFiles;
    }

}
