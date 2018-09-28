package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.executors.MetadataExtractor;
import edu.ncsu.utils.Utils;

import java.util.logging.Logger;

public class Metadata {

    private static final Logger LOGGER = Logger.getLogger(Metadata.class.getName());

    public static void extractMetadata() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
            String problemPath = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
            for(String javaFile: CodejamUtils.listGeneratedFiles(problemPath)) {
                MetadataExtractor extractor = new MetadataExtractor(javaFile);
                extractor.extract();
            }
        }
    }

    public static void main(String[] args) {
        extractMetadata();
    }

}
