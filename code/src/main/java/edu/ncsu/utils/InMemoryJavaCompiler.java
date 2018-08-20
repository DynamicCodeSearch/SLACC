package edu.ncsu.utils;

import org.apache.commons.lang3.StringUtils;

import javax.tools.JavaCompiler;
import javax.tools.ToolProvider;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class InMemoryJavaCompiler {

    private final static JavaCompiler COMPILER = ToolProvider.getSystemJavaCompiler();

    private static OutputStream getErrorStream() {
        final StringBuilder stringBuilder = new StringBuilder();

        return new OutputStream() {
            @Override
            public void write(int b) throws IOException {
                stringBuilder.append((char) b);
            }

            @Override
            public String toString() {
                return stringBuilder.toString();
            }
        };
    }


    public static boolean compile(String className, String packageName, String sourceFolder, String content) {
        String writePath = String.format("%s%s", sourceFolder, packageName.replaceAll("\\.", File.separator));
        Utils.mkdir(writePath);
        OutputStream errorStream = getErrorStream();
        String fileName = writePath + "/" + className + ".java";
        try {
            FileOutputStream outputStream = new FileOutputStream(fileName);
            byte[] bytes = content.getBytes();
            outputStream.write(bytes);
            outputStream.close();
            COMPILER.run(null, null, errorStream, fileName, "-nowarn");
            String errorMsg = errorStream.toString();
            errorStream.close();
            if (!StringUtils.isEmpty(errorMsg)) {
                throw new RuntimeException(errorMsg);
            }
        } catch (IOException e) {
            return false;
        } finally {
            File javaFile = new File(fileName);
            if (javaFile.exists()) javaFile.delete();
            File classFile = new File(writePath + "/" + className + ".class");
            if (classFile.exists()) classFile.delete();
        }
        return true;
    }

    public static boolean compile(String fileName, boolean raiseException) {
        try {
            OutputStream errorStream = getErrorStream();
            COMPILER.run(null, null, errorStream, fileName, "-nowarn");
            String errorMsg = errorStream.toString();
            errorStream.close();
            if (!StringUtils.isEmpty(errorMsg)) {
                if (raiseException)
                    throw new RuntimeException(errorMsg);
                else
                    return false;
            }
        } catch (IOException e) {
            return false;
        } finally {
            File parentFolder = new File(fileName).getParentFile();
            for (String className: Utils.listFilesWithExtension(parentFolder.getAbsolutePath(), ".class", true, false)) {
                File classFile = new File(className);
                classFile.delete();
            }

        }
        return true;
    }
}
