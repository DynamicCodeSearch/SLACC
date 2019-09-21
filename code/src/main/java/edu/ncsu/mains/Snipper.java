package edu.ncsu.mains;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

import java.util.logging.Logger;

public class Snipper {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());


    private static void snipDataset(String dataset) {
        LOGGER.info(String.format("Processing for Dataset: %s", dataset));
        String datasetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        snipFolder(dataset, datasetPath);
    }


    private static void snipProblem(String dataset, String problem) {
        LOGGER.info(String.format("Processing for Dataset: %s and Problem: %s", dataset, problem));
        String problemPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset, problem);
        snipFolder(dataset, problemPath);
    }

    private static void snipFolder(String dataset, String folderPath) {
        for (String javaFile: Utils.listFilesWithExtension(folderPath, ".java", true, true)) {
            String fileName = Utils.getFileName(javaFile);
            if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX) &&
                    !fileName.startsWith(Settings.TEMPORARY_CLASS_PREFIX) &&
                    !fileName.startsWith(Settings.PERMUTATED_CLASS_PREFIX)) {
                MethodAndVariableAdapter.generateMethodsForJavaFile(dataset, javaFile);
            }
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            LOGGER.severe("Dataset should be the first argument");
            System.exit(0);
        }
        String dataset = args[0];
        if (args.length > 1) {
            String problem = args[1];
            snipProblem(dataset, problem);
        } else {
            snipDataset(dataset);
        }

    }

}
