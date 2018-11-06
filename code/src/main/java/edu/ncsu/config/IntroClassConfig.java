package edu.ncsu.config;

import edu.ncsu.utils.Utils;

public class IntroClassConfig   {

    public static String NAME = "IntroClassJava";

    public static String HOME = Utils.pathJoin(Settings.CODESEER_HOME, NAME);

    public static String DATASET_HOME = Utils.pathJoin(HOME, "dataset");

    public static String SRC_JAVA_FOLDER = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, NAME);

}
