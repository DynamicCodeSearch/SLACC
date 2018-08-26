package edu.ncsu.codejam;

import edu.ncsu.config.Properties;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.adapters.MethodAndVariableAdapter;

import java.util.Arrays;
import java.util.logging.Logger;

public class Snipper {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    private static void snipProblem(String problem) {
        String problemDir = Utils.pathJoin(Properties.CODEJAM_JAVA_FOLDER, problem);
        String[] users = Utils.listDir(problemDir);
        Arrays.sort(users);
        for (String user: users) {
            String userDir = Utils.pathJoin(problemDir, user);
            for (String javaFile: Utils.listFilesWithExtension(userDir, ".java", true, true)) {
                String fileName = Utils.getFileName(javaFile);
                if (!fileName.startsWith(Properties.GENERATED_CLASS_PREFIX) && !fileName.startsWith(Properties.TEMPORARY_CLASS_PREFIX))
                    MethodAndVariableAdapter.generateMethodsForJavaFile(javaFile);
            }
        }
    }

    private static void snipAll() {
        for (String problem: Utils.listDir(Properties.CODEJAM_JAVA_FOLDER)) {
            snipProblem(problem);
        }
    }

    public static void main(String[] args) {
        if (args.length > 0) {
            LOGGER.info(String.format("Running for %s" , args[0]));
            snipProblem(args[0]);
        } else {
            LOGGER.info("Running for all");
            snipAll();
        }
    }

}