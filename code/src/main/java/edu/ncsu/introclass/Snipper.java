package edu.ncsu.introclass;

import edu.ncsu.config.IntroClassConfig;
import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

import java.util.logging.Logger;

public class Snipper {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    private static void snipProblem(String problem) {
        String problemDir = Utils.pathJoin(IntroClassConfig.SRC_JAVA_FOLDER, problem);
        for (String javaFile: Utils.listFilesWithExtension(problemDir, ".java", true, true)) {
            String fileName = Utils.getFileName(javaFile);
            if (!fileName.startsWith(Properties.GENERATED_CLASS_PREFIX) && !fileName.startsWith(Properties.TEMPORARY_CLASS_PREFIX)) {
                MethodAndVariableAdapter.generateMethodsForJavaFile(javaFile);
            }
        }
    }

    private static void snipAll() {
        for (String problem: Utils.listDir(IntroClassConfig.SRC_JAVA_FOLDER)) {
            LOGGER.info(String.format("Running for problem: %s ..... ", problem));
            snipProblem(problem);
        }
    }

    public static void main(String[] args) {
        if (args.length <= 0) {
            LOGGER.info("Running for all");
            snipAll();
        } else {
            LOGGER.info(String.format("Running for %s" , args[0]));
            snipProblem(args[0]);
        }
    }

}
