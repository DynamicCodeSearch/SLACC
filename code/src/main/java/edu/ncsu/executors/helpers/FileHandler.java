package edu.ncsu.executors.helpers;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.Utils;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.logging.Logger;

public class FileHandler {

    private final static String RANDOM_INPUT_FOLDER = Utils.pathJoin(Settings.CODE_RESOURCES_FOLDER, "test_files");

    private final static String RANDOM_OUTPUT_FOLDER = Utils.pathJoin(Settings.CODE_RESOURCES_FOLDER, "test_files_output");

    private final static Set<String> INPUT_CLASSES = new HashSet<>();

    private final static Set<String> OUTPUT_CLASSES = new HashSet<>();

    public final static String FILE_INPUT_TYPE = "__SLACC_FILE_INPUT__";

    public final static String FILE_OUTPUT_TYPE = "__SLACC_FILE_OUTPUT__";

    static {
        INPUT_CLASSES.add("java.util.Scanner");

        OUTPUT_CLASSES.add("java.io.PrintWriter");
    }


    public static Set<String> getInputClasses() {
        return INPUT_CLASSES;
    }

    public static Set<String> getOutputClasses() {
        return OUTPUT_CLASSES;
    }

    public static boolean isInputClass(String className) {
        return INPUT_CLASSES.contains(className);
    }

    public static boolean isOutputClass(String className) {
        return OUTPUT_CLASSES.contains(className);
    }

    public static boolean isSupportedFileClass(String className) {
        return isInputClass(className) || isOutputClass(className);
    }

    public static String getRandomFileContent() {
        List<String> randomFiles = Utils.listFilesWithExtension(RANDOM_INPUT_FOLDER, ".in", true, false);
        String randomFilePath = randomFiles.get(new Random().nextInt(randomFiles.size()));
        try {
            return new String(Files.readAllBytes(Paths.get(randomFilePath)));
        } catch (IOException e) {
            throw new RuntimeException(String.format("Error while reading '%s'", randomFilePath), e);
        }
    }

    public static Object convertFileInput(String className, String contents) {
        contents = contents.replaceAll("^\"|\"$", "").replace("\\n", System.lineSeparator());
        try {
            switch (className) {
                case "java.util.Scanner":
                    return new Scanner(contents);
                default:
                    throw new RuntimeException(String.format("WTF!! We do not support %s?", className));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public static Object convertFileOutput(String className, int objUUID, int argIndex) {
        try {
            Utils.mkdir(RANDOM_OUTPUT_FOLDER);
            File tempFile = new File(Utils.pathJoin(RANDOM_OUTPUT_FOLDER, getWriteFileName(objUUID, argIndex)));
            tempFile.deleteOnExit();
            switch (className) {
                case "java.io.PrintWriter":
                    return new PrintWriter(tempFile);
                default:
//                    f.delete();
                    throw new RuntimeException(String.format("WTF!! We do not support %s?", className));
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static String getWriteFileName(int objUUID, int argIndex) {
        return String.format("test-%d-%d.out", objUUID, argIndex);
    }

    public static String dumpOutputAsText(int objUUID, int argIndex) {
        return Utils.readFromFile(Utils.pathJoin(RANDOM_OUTPUT_FOLDER, getWriteFileName(objUUID, argIndex)));
    }

    /***
     * Inputs:
     * java.util.Scanner
     * java.util.BufferedReader
     * java.io.FileInputStream
     * java.io.StreamTokenizer
     */

    /***
     * Outputs:
     * java.io.PrintWriter
     * java.io.PrintStream
     * java.io.BufferedWriter
     */

}
