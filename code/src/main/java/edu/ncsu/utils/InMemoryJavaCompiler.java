package edu.ncsu.utils;

import edu.ncsu.config.Settings;

import javax.tools.*;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class InMemoryJavaCompiler {

    private final static JavaCompiler COMPILER = ToolProvider.getSystemJavaCompiler();

    private final static String CLASSPATH = System.getProperty("java.class.path") + File.pathSeparator + Utils.pathJoin(Settings.PROJECTS_HOME, "target", "classes");

    private final static List<String> COMPILER_OPTIONS = Arrays.asList("-nowarn", "-classpath",CLASSPATH);

    private final static  StandardJavaFileManager FILE_MANAGER = COMPILER.getStandardFileManager(
            new DiagnosticCollector<JavaFileObject>(), null, null);


    private static OutputStreamWriter getOutputStream() {
        final StringBuilder stringBuilder = new StringBuilder();

        return new OutputStreamWriter(new OutputStream() {
            @Override
            public void write(int b) {
                stringBuilder.append((char) b);
            }

            @Override
            public String toString() {
                return stringBuilder.toString();
            }
        });
    }


    public static boolean compile(String className, String packageName, String sourceFolder, String content) {
        String writePath = Utils.pathJoin(sourceFolder, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writePath);
        String fileName = writePath + "/" + className + ".java";
        try {
            FileOutputStream outputStream = new FileOutputStream(fileName);
            byte[] bytes = content.getBytes();
            outputStream.write(bytes);
            outputStream.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try {
            return compile(fileName, false);
        } finally {
            File javaFile = new File(fileName);
            if (javaFile.exists()) javaFile.delete();
            File classFile = new File(writePath + "/" + className + ".class");
            if (classFile.exists()) classFile.delete();
        }
    }

    public static boolean compile(String fileName, boolean raiseException) {
        try {
            List<File> sourceFileList = new ArrayList<>();
            sourceFileList.add (new File(fileName));
            Iterable<? extends JavaFileObject> compilationUnits = FILE_MANAGER.getJavaFileObjectsFromFiles (sourceFileList);
            OutputStreamWriter writer = getOutputStream();
            JavaCompiler.CompilationTask task = COMPILER.getTask (writer,null, null, COMPILER_OPTIONS, null, compilationUnits);
            boolean result = task.call();
            writer.close();
            if (result) {
                return true;
            } else if (raiseException) {
                throw new RuntimeException(String.format("Failed to compile %s", fileName));
            } else {
                return false;
            }
        } catch (IOException e) {
            if (raiseException) {
                throw new RuntimeException(e);
            } else {
                return false;
            }
        } finally {
            try {
                FILE_MANAGER.close();
            } catch (IOException ex) {
                System.out.println("Failed to close file manager");
            }
            File parentFolder = new File(fileName).getParentFile();
            for (String className: Utils.listFilesWithExtension(parentFolder.getAbsolutePath(), ".class", true, false)) {
                File classFile = new File(className);
                classFile.delete();
            }

        }
    }

    public static void main(String[] args) {
        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/Junk/temp_class_1ffcf8fa52f24822bcbc1283d8912402.java";
        System.out.println(InMemoryJavaCompiler.compile(fileName, false));
    }

}
