package edu.ncsu.executors.helpers;

import com.google.common.reflect.ClassPath;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PackageManager {

    public static List<Class> findClasses(String packageName) {
        List<Class> classes = new ArrayList<>();
        try {
            ClassPath classPath = ClassPath.from(Thread.currentThread().getContextClassLoader());
            for (ClassPath.ClassInfo classInfo: classPath.getTopLevelClassesRecursive(packageName)) {
                classes.add(classInfo.load());
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return classes;
    }

    public static Class findClass(String packageName, String className) {
        String packageClass = String.format("%s.%s", packageName, className);
        try {
            return Class.forName(packageClass);
        } catch (ClassNotFoundException e){
            throw new RuntimeException(e);
        }

    }

    public static void main(String[] args) {
        List<Class> classes = PackageManager.findClasses("IntroClassJava");
        for (Class clazz: classes) {
            System.out.println(String.format("%s.%s", clazz.getPackage(), clazz.getName()));
        }
    }

}
