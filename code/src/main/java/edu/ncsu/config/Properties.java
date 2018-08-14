package edu.ncsu.config;

import org.apache.commons.lang3.StringUtils;
import java.io.File;

public class Properties {

    public static String HOME = System.getenv("HOME");

    public static String ROOT_PATH = StringUtils.join(new Object[]{HOME, "Raise", "ProgramRepair"}, File.separator);

    public static String PROJECT_HOME = StringUtils.join(new Object[]{ROOT_PATH, "CodeSeer"}, File.separator);

    public static String CODE_HOME = StringUtils.join(new Object[]{PROJECT_HOME, "code"}, File.separator);

    public static String CODEJAM_JAVA_FOLDER = StringUtils.join(new Object[]{CODE_HOME, "projects", "java"},
            File.separator);

}
