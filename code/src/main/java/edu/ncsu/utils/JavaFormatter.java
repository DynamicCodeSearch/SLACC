package edu.ncsu.utils;

import com.google.googlejavaformat.java.Formatter;
import com.google.googlejavaformat.java.JavaFormatterOptions;
import org.apache.commons.io.FileUtils;

import java.io.File;
import java.nio.charset.StandardCharsets;
import java.util.logging.Logger;

public class JavaFormatter {

    private final static Logger LOGGER = Logger.getLogger(JavaFormatter.class.getName());

    public static String format(String fileName) {
        String source = null;
        try {
            source = FileUtils.readFileToString(new File(fileName), StandardCharsets.UTF_8);
            Formatter formatter = new Formatter(new JavaFormatterOptions(JavaFormatterOptions.JavadocFormatter.ECLIPSE, JavaFormatterOptions.Style.GOOGLE, JavaFormatterOptions.SortImports.ALSO));
            return formatter.formatSource(source);
        } catch (Exception ex) {
            LOGGER.severe("Format and Save Exception. " + ex.getMessage());
            return source;
        }
    }

    public static void formatAndSave(String fileName) {
        try {
            String formatted = format(fileName);
            FileUtils.writeStringToFile(new File(fileName), formatted);
        } catch (Exception ex) {
            throw new RuntimeException(ex);
        }
    }

    public static void main(String[] args) {
        formatAndSave("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Y11R5P1/Egor1/generated_class_1fe64b355c89496a839e13105bf2a3c8.java");
    }
}
