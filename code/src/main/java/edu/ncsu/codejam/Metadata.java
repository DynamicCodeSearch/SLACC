package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.executors.MetadataExtractor;
import edu.ncsu.utils.Utils;

import java.util.logging.Logger;

public class Metadata {

    private static final Logger LOGGER = Logger.getLogger(Metadata.class.getName());

    public static void extractMetadata() {
        for (String problem: Utils.listDir(Properties.getDatasetSourceFolder(CodejamUtils.DATASET))) {
            LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
            String problemPath = Utils.pathJoin(Properties.getDatasetSourceFolder(CodejamUtils.DATASET), problem);
            for(String javaFile: Utils.listGeneratedFiles(problemPath)) {
                MetadataExtractor extractor = new MetadataExtractor(CodejamUtils.DATASET, javaFile);
                extractor.extract();
            }
        }
    }

    public static void main(String[] args) {
        extractMetadata();
    }

}
