package edu.ncsu.executors;

import com.google.gson.JsonObject;
import edu.ncsu.config.Properties;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.StoreUtils;
import edu.ncsu.utils.Utils;

import java.io.File;
import java.lang.reflect.Method;
import java.util.logging.Logger;

public class MetadataExtractor {

    private static final Logger LOGGER = Logger.getLogger(MetadataExtractor.class.getName());

    private ClassMethods classMethods;

    public MetadataExtractor(String dataset, String filePath) {
        classMethods = new ClassMethods(dataset, filePath);
    }

    public void saveMetadata(JsonObject metadata) {
        LOGGER.info("Writing metadata ... ");
        String writeFolder = Utils.pathJoin(Properties.META_STORE, this.classMethods.getDataset(), "functions",
                classMethods.getPackageName().replaceAll("\\.", File.separator));
        Utils.mkdir(writeFolder);
        String writeFile = Utils.pathJoin(writeFolder, String.format("%s.json", classMethods.getClassName()));
        StoreUtils.saveJsonObject(metadata, writeFile, true);

    }

    public void extract() {
        LOGGER.info(String.format("Extracting metadata for class: %s.%s",
                classMethods.getPackageName(), classMethods.getClassName()));
        JsonObject metadata = new JsonObject();
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            metadata.add(function.getName(), function.getMetaData());
        }
        saveMetadata(metadata);
    }

    public static void extractForDataset(String dataset) {
        String sourceFolder = Properties.getDatasetSourceFolder(dataset);
        for (String problem: Utils.listDir(sourceFolder)) {
            LOGGER.info(String.format("Executing methods for problem: %s. Here we go .... ", problem));
            String problemPath = Utils.pathJoin(sourceFolder, problem);
            for(String javaFile: Utils.listGeneratedFiles(problemPath)) {
                MetadataExtractor extractor = new MetadataExtractor(dataset, javaFile);
                extractor.extract();
            }
        }
    }

}
