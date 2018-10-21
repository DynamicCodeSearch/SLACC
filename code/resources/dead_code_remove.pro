-injars  <user.home>/Raise/ProgramRepair/CodeSeer/code/jars/projects-1.0-SNAPSHOT-jar-with-dependencies.jar
-outjars <user.home>/Raise/ProgramRepair/CodeSeer/code/cleaned/projects-1.0-SNAPSHOT-jar-with-dependencies.jar

-libraryjars <java.home>/lib/rt.jar

-dontshrink
-dontobfuscate
-optimizations method/removal/parameter
-optimizationpasses 5

-keepclasseswithmembernames class generated_class_* {
    *;
}

-keep public class Main


