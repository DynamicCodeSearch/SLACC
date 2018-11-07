package edu.ncsu.executors;

import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.Utils;

import java.lang.reflect.Method;
import java.util.logging.Logger;

public class MetadataExtractor {

    private static final Logger LOGGER = Logger.getLogger(MetadataExtractor.class.getName());

    private ClassMethods classMethods;

    private IMetadataStore metadataStore;

    public MetadataExtractor(String dataset, String filePath) {
        classMethods = new ClassMethods(dataset, filePath);
        metadataStore = BaseStorage.loadMetadataStore();
    }

    public void extract() {
        LOGGER.info(String.format("Extracting metadata for class: %s.%s",
                classMethods.getPackageName(), classMethods.getClassName()));
        JsonObject metadata = new JsonObject();
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            metadata.add(function.getName(), function.getMetaData());
        }
        this.metadataStore.saveClassFunctionsMetadata(metadata, classMethods);
    }

    public static void extractForDataset(String dataset) {
        String sourceFolder = Settings.getDatasetSourceFolder(dataset);
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
