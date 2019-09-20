package edu.ncsu.executors;

import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.Utils;

import java.lang.reflect.Method;
import java.util.List;
import java.util.Set;
import java.util.logging.Logger;

public class MetadataExtractor {

    private static final Logger LOGGER = Logger.getLogger(MetadataExtractor.class.getName());

    private ClassMethods classMethods;

    private IMetadataStore metadataStore;

    private MetadataExtractor(String dataset, String filePath) {
        classMethods = new ClassMethods(dataset, filePath);
        metadataStore = BaseStorage.loadMetadataStore();
    }

    private void extract() {
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
        String sourceFolder = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, dataset);
        List<String> javaFiles = Utils.listPermutatedFiles(sourceFolder);
        if (javaFiles == null || javaFiles.size() == 0) {
            javaFiles = Utils.listGeneratedFiles(sourceFolder);
        }
        for(String javaFile: javaFiles) {
            MetadataExtractor extractor = new MetadataExtractor(dataset, javaFile);
            extractor.extract();
        }
    }

    public static void main(String[] args) {
        extractForDataset("Dummy");
    }

}
