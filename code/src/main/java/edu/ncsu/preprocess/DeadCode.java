package edu.ncsu.preprocess;

import com.github.javaparser.ast.CompilationUnit;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.helpers.PackageManager;
import edu.ncsu.utils.Utils;

import java.util.List;
import java.util.logging.Logger;

public class DeadCode {

    private static Logger LOGGER = Logger.getLogger(DeadCode.class.getName());

    private static String EXTRACTED = "extracted";

    private static void transfer(String sourceFile, String targetFile) {
        CompilationUnit source = Utils.getCompilationUnit(sourceFile);
        CompilationUnit target = Utils.getCompilationUnit(targetFile);
        target.setTypes(source.getTypes());
        Utils.writeFileContent(target.toString(), targetFile);
    }

    private static void clean(String packageName, String className) {
        String classPath = Utils.pathJoin(Utils.packageToFolder(packageName), String.format("%s.java", className));
        String sourcePath = Utils.pathJoin(Settings.CODE_HOME, EXTRACTED, classPath);
        String targetPath = Utils.pathJoin(Settings.PROJECTS_JAVA_FOLDER, classPath);
        transfer(sourcePath, targetPath);
    }

    public static void clean(String dataset) {
        List<Class> classes = PackageManager.findClasses(dataset);
        for (Class clazz: classes) {
            if (clazz.getSimpleName().startsWith(Settings.GENERATED_CLASS_PREFIX)) {
                clean(clazz.getPackage().getName(), clazz.getSimpleName());
                LOGGER.info(String.format("Cleaning %s.%s ... ", clazz.getPackage(), clazz.getSimpleName()));
            }
        }
    }

    public static void main(String[] args) {
//        transfer("/Users/panzer/Raise/ProgramRepair/CodeSeer/code/extracted/IntroClassJava/checksum/checksum_2c155667_003/generated_class_c703a0aa86ba42c7a2cbee415f9f4142.java",
//                "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/IntroClassJava/checksum/checksum_2c155667_003/generated_class_c703a0aa86ba42c7a2cbee415f9f4142.java");
//        clean("IntroClassJava.checksum.checksum_2c155667_003", "generated_class_c703a0aa86ba42c7a2cbee415f9f4142");
        clean("IntroClassJava");
    }

}
