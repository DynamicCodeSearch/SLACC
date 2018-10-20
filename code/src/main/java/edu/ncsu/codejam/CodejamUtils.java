package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Pattern;

public class CodejamUtils {

    public static String DATASET = "codejam";

    public static Pattern CODEJAM_PROBLEM_PATTERN = Pattern.compile("Y\\d{2}R\\dP\\d");

    public static List<String> listGeneratedFiles() {
        List<String> generatedFiles = new ArrayList<>();
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            if (CODEJAM_PROBLEM_PATTERN.matcher(problem).matches()) {
                String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
                generatedFiles.addAll(Utils.listGeneratedFiles(problemDir));
            }
        }
        return generatedFiles;
    }

    public static List<String> listGeneratedFiles(String problemPath) {
        List<String> generatedFiles = new ArrayList<>();
        String[] users = Utils.listDir(problemPath);
        Arrays.sort(users);
        for (String user: users) {
            String userDir = Utils.pathJoin(problemPath, user);
            generatedFiles.addAll(Utils.listGeneratedFiles(userDir));
        }
        return generatedFiles;
    }

}
