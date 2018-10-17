package edu.ncsu.introclass;

import edu.ncsu.config.IntroClassConfig;
import edu.ncsu.utils.Utils;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.FilenameFilter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Logger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;



/**
 * A filter to check and extract parameters from the filename of IntroClass source java file
 */
class DirectoryFilter implements FilenameFilter {
    private static Pattern pattern = Pattern.compile(Utils.pathJoin(IntroClassConfig.DATASET_HOME, "(\\w+)",
            "(\\w{128})", "(\\d+)", "src", "main", "java", "(\\w+)", "(\\w+)\\.java"));

    @Override
    public boolean accept(File dir, String name) {
        return pattern.matcher(name).matches();
    }

    /***
     * Fetch metadata groups from the filePath
     * @param filePath - Path of the file name.
     * @return - HashMap containing the metadata
     */
    Map<String, String> groups(String filePath) {
        Matcher matcher = pattern.matcher(filePath);
        if (matcher.find()) {
            Map<String, String> groups= new HashMap<>();
            groups.put("problem", matcher.group(1));
            groups.put("sha", matcher.group(2));
            groups.put("number", matcher.group(3));
            groups.put("package", matcher.group(4));
            groups.put("className", matcher.group(5));
            return groups;
        } else {
            return null;
        }
    }
}

public class Crawler {

    private static final Logger LOGGER = Logger.getLogger(Crawler.class.getName());

    private static final String PACKAGE_REGEX = "package \\w+(\\.\\w+)*;";

    private static DirectoryFilter filter = new DirectoryFilter();

    public static void process() {
        List<String> javaFiles = Utils.listFiles(IntroClassConfig.DATASET_HOME, filter, true, true);
        int i = 0;
        for (String javaPath: javaFiles) {
            LOGGER.info(String.format("Processing %s. Completed: %d/%d", Utils.getFileName(javaPath), i, javaFiles.size()));
            processJavaFile(javaPath);
            i++;
        }
    }

    private static void processJavaFile(String javaPath) {
        Map<String, String> metadata = filter.groups(javaPath);
        if (metadata == null) {
            LOGGER.info(String.format("This is not a valid IntroClass java file: %s", javaPath));
            return;
        }
        String packageName = String.format("%s.%s.%s", IntroClassConfig.NAME, metadata.get("problem"),
                metadata.get("className"));
        String contents = Utils.getFileContent(javaPath);
        if (contents == null) {
            LOGGER.info(String.format("This IntroClass java file is empty: %s", javaPath));
            return;
        }
        contents = contents.replaceAll(PACKAGE_REGEX, String.format("package %s;", packageName));
        String writeFilePath = Utils.pathJoin(IntroClassConfig.SRC_JAVA_FOLDER, metadata.get("problem"),
                metadata.get("className"), String.format("%s.java", metadata.get("className")));
        Utils.writeFileContent(contents, writeFilePath);
    }

    public static void main(String[] args) {
        process();
    }
}


