package edu.ncsu.codejam;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;

public class CodejamUtils {

    public static String DATASET = "codejam";

    public static Pattern CODEJAM_PROBLEM_PATTERN = Pattern.compile("Y\\d{2}R\\dP\\d");

    public static List<String> listGeneratedFiles() {
        List<String> generatedFiles = new ArrayList<>();
        String sourceJavaFolder = Settings.getDatasetSourceFolder(DATASET);
        for (String problem: Utils.listDir(sourceJavaFolder)) {
            if (CODEJAM_PROBLEM_PATTERN.matcher(problem).matches()) {
                String problemDir = Utils.pathJoin(sourceJavaFolder, problem);
                generatedFiles.addAll(Utils.listGeneratedFiles(problemDir));
            }
        }
        return generatedFiles;
    }

}
