package edu.ncsu.codejam;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.PreprocessAdapter;

import java.util.logging.Logger;

public class Preprocess {

    private static Logger LOGGER = Logger.getLogger(Preprocess.class.getName());

    private static void preprocess() {
        LOGGER.info(String.format("Preprocessing '%s' dataset ... ", CodejamUtils.DATASET));
        for (String fileName: Utils.listFilesWithExtension(Settings.getDatasetSourceFolder(CodejamUtils.DATASET),
                ".java", true, true)) {
            PreprocessAdapter.preprocess(fileName);
        }
    }

    public static void main(String[] args) {
        preprocess();
    }

}
