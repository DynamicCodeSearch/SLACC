package edu.ncsu.permutator;

import com.google.gson.JsonObject;
import edu.ncsu.config.Settings;
import edu.ncsu.executors.models.ClassMethods;
import edu.ncsu.executors.models.Function;
import edu.ncsu.executors.models.FunctionVariable;
import edu.ncsu.mains.Snipper;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IMetadataStore;
import edu.ncsu.utils.JavaFormatter;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.blocks.Imports;
import org.apache.commons.lang3.StringUtils;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Logger;

public class Permutator {

    private static Logger LOGGER = Logger.getLogger(Snipper.class.getName());

    public static void permutateFile(String dataset, String generated_file) {
        IMetadataStore metadataStore = BaseStorage.loadMetadataStore();
        String fileName = Utils.getFileName(generated_file);
        if (!fileName.startsWith(Settings.GENERATED_CLASS_PREFIX)) {
            LOGGER.info(String.format("%s is not a generated file. Not permutating!", generated_file));
            return;
        }
        String parentFolder = Utils.getFolderPath(generated_file);
        String suffix = fileName.substring(Settings.GENERATED_CLASS_PREFIX.length());

        String className = Settings.PERMUTATED_CLASS_PREFIX + suffix.split(".java")[0];
        String permutatedFile = Utils.pathJoin(parentFolder, className + ".java");
//        if (Utils.fileExists(permutatedFile)) {
//            LOGGER.info(String.format("Processed file: %s. Moving on ...", generated_file));
//            return;
//        }
        ClassMethods classMethods = new ClassMethods(dataset, generated_file);
        List<String> functionsAsString = new ArrayList<>();
        List<JsonObject> functionsMetadata = new ArrayList<>();
        for (Method method: classMethods.getMethods()) {
            Function function = classMethods.getFunction(method);
            if (function.shouldBeSkipped()) {
                continue;
            }
            JsonObject metadata = metadataStore.getFunctionMetadata(dataset, function.getName());
            assert metadata != null;
            metadata.remove("_id");
            String body = function.getAst().getBody().toString();
            String returnType = function.getReturnVariable().getDataTypeAsString();
            if (returnType == null) {
                returnType = method.getReturnType().getName();
            }
            List<Object> functionParameters = new ArrayList<Object>(function.getArguments());
            List<List<Object>> argPermutations = Function.getPermutations(functionParameters);
            for(List<Object> argPermutation : argPermutations) {
                JsonObject cloned = metadata.deepCopy();
                List<FunctionVariable> permutatedArgs = new ArrayList<>();
                List<String> permutatedArgsAsStr = new ArrayList<>();
                for (Object argObj: argPermutation) {
                    FunctionVariable arg = (FunctionVariable) argObj;
                    permutatedArgs.add(arg);
                    permutatedArgsAsStr.add(arg.toFunctionParameter());
                }
                String inputKey = Function.constructArgumentTypesKey(permutatedArgs);
                String argStr = StringUtils.join(permutatedArgsAsStr, ", ");
                String functionName = "func_" + Utils.randomString();
                String functionAsString = String.format("public static %s %s(%s)%s", returnType, functionName, argStr, body);
                cloned.addProperty("name", functionName);
                cloned.addProperty("body", functionAsString);
                cloned.addProperty("inputKey", inputKey);
                cloned.addProperty("filePath", permutatedFile);
                functionsMetadata.add(cloned);
                functionsAsString.add(functionAsString);
            }
        }
        StringBuilder javaContent = new StringBuilder();
        javaContent.append("package ").append(classMethods.getPackageName()).append(";\n\n").
                append(Imports.defaultImports()).
                append("public class ").append(className).append(" {\n");
        for (String function: functionsAsString) {
            javaContent.append(function).append("\n");
        }
        javaContent.append("}");
        File writeFile = new File(permutatedFile);
        try (PrintWriter out = new PrintWriter(writeFile)) {
            out.println(javaContent.toString());
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        metadataStore.saveClassFunctionsMetadata(dataset, functionsMetadata);
//        JavaFormatter.formatAndSave(permutatedFile);
    }

    public static void main(String[] args) {
        permutateFile("IntroClassJava", "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/IntroClassJava/digits/digits_65e02c1a_015/generated_class_7dfb0e91f5f64432814ecd68964bc88e.java");
    }
}
