package edu.ncsu.mains;

import edu.ncsu.config.Settings;
import edu.ncsu.permutator.Permutator;
import edu.ncsu.utils.Utils;

import java.util.logging.Logger;

public class Permutate {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    private static void permutateDataset(String dataset) {
        LOGGER.info(String.format("Processing for Dataset: %s", dataset));
        String datasetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        permutateFolder(dataset, datasetPath);
    }

    private static void permutateFolder(String dataset, String folderPath) {
        for (String javaFile : Utils.listGeneratedFiles(folderPath)) {
            String fileName = Utils.getFileName(javaFile);
            String parent_folder = Utils.getFolderPath(javaFile);
            String suffix = fileName.substring(0, Settings.GENERATED_CLASS_PREFIX.length());
            String permutated_file = Utils.pathJoin(parent_folder, Settings.PERMUTATED_CLASS_PREFIX + suffix);
            if (Utils.fileExists(permutated_file)) {
                LOGGER.info(String.format("Processed file: %s. Moving on ...", javaFile));
                continue;
            }
            LOGGER.info(String.format("Processing file: %s. ...", javaFile));
            Permutator.permutateFile(dataset, javaFile);
        }
    }

    public static void main(String[] args) {
        permutateDataset(args[0]);
    }
}
