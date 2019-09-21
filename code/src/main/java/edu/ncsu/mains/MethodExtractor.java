package edu.ncsu.mains;

import edu.ncsu.codejam.CodejamUtils;
import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;

public class MethodExtractor {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    private static void extractMethods(String dataset) {
        String outFile = "/Users/panzer/Raise/ProgramRepair/CodeSeer/code/results/method_names.csv";
        String folderPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        StringBuilder builder = new StringBuilder();
        builder.append("Class").append(",")
                .append("Package").append(",")
                .append("Method").append(",")
                .append("Args").append(",")
                .append("Return").append("\n");
        for (String problem: Utils.listDir(folderPath)) {
            LOGGER.info(String.format("Processing for Dataset: %s and Problem: %s", dataset, problem));
            String problemPath = Utils.pathJoin(folderPath, problem);
            for (String javaFile: Utils.listFilesWithExtension(problemPath, ".java", true, true)) {
                String fileName = Utils.getFileName(javaFile);
                if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX) && !fileName.startsWith(Settings.TEMPORARY_CLASS_PREFIX)) {
                    List<Map<String, String>> methodMetas = MethodAndVariableAdapter.extractMethodProps(dataset, javaFile, true);
                    for (Map<String, String> methodMeta :methodMetas) {
                        builder.append(methodMeta.get("Class")).append(",");
                        builder.append(methodMeta.get("Package")).append(",");
                        builder.append(methodMeta.get("Method")).append(",");
                        builder.append(methodMeta.get("Args")).append(",");
                        builder.append(methodMeta.get("Return"));
                        builder.append("\n");
                    }
                }
            }
            builder.append("\n");
        }
        LOGGER.info("Writing ... ");
        try (PrintWriter writer = new PrintWriter(new File(outFile))) {
            writer.append(builder.toString());
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        extractMethods(CodejamUtils.DATASET);
    }

}
