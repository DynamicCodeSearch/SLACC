package edu.ncsu.codejam;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.PreprocessAdapter;

import java.util.logging.Logger;

public class Preprocess {

    private static Logger LOGGER = Logger.getLogger(Preprocess.class.getName());

    private static void preprocess() {
        LOGGER.info(String.format("Preprocessing '%s' dataset ... ", CodejamUtils.DATASET));
        for (String filePath: Utils.listFilesWithExtension(Settings.getDatasetSourceFolder(CodejamUtils.DATASET),
                ".java", true, true)) {
            String fileName = Utils.getFileName(filePath);
            if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX)) {
                PreprocessAdapter.preprocess(filePath);
            }
        }
    }

    public static void main(String[] args) {
        preprocess();
    }

}
