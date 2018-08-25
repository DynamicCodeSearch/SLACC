package edu.ncsu.visitors.adapters;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParseException;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.ImportDeclaration;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import com.google.gson.JsonArray;
import edu.ncsu.config.Properties;
import edu.ncsu.store.ObjectStore;
import edu.ncsu.visitors.blocks.Variable;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ObjectStoreAdapter extends VoidVisitorAdapter {

    private CompilationUnit compilationUnit;

    public ObjectStoreAdapter(String javaFile) {
        try {
            File file = new File(javaFile);
            compilationUnit = JavaParser.parse(file, null, false);
        } catch (ParseException | IOException e) {
            e.printStackTrace();
            throw new RuntimeException(e);
        }
    }

    private List<String> getImports() {
        List<String> imports = new ArrayList<>();
        for (ImportDeclaration importDec : compilationUnit.getImports()) {
            imports.add(importDec.toStringWithoutComments());
        }
        return imports;
    }

    public void storeClasses(ObjectStore store) {
        String packageName = VisitorHelper.getPackage(compilationUnit);
        JsonArray imports = new JsonArray();
        for (String imp0rt : getImports())
            imports.add(imp0rt);
        for (TypeDeclaration type: compilationUnit.getTypes()) {
            if (!(type instanceof ClassOrInterfaceDeclaration))
                continue;
            ClassOrInterfaceDeclaration classDeclaration = (ClassOrInterfaceDeclaration) type;
            JsonArray variables =  new JsonArray();
            JsonArray extendsList = null;
            if (classDeclaration.getExtends().size() > 0) {
                extendsList = new JsonArray();
                for (ClassOrInterfaceType parent: classDeclaration.getExtends())
                    extendsList.add(parent.getName());
            }
            for (BodyDeclaration member: classDeclaration.getMembers()) {
                if (member instanceof FieldDeclaration) {
                    FieldDeclaration fieldDeclaration = (FieldDeclaration) member;
                    Type fieldType = fieldDeclaration.getType();
                    String modifier = Variable.getModifier(fieldDeclaration.getModifiers());
                    for (VariableDeclarator fieldVariable: fieldDeclaration.getVariables()) {
                        String variableName = fieldVariable.getId().getName();
                        variables.add(new Variable(variableName, fieldType, modifier).toJson());
                    }
                }
            }
            store.saveClass(packageName, classDeclaration.getName(), imports, variables, extendsList);
        }
    }

    public static void main(String[] args) {
        ObjectStoreAdapter adapter = new ObjectStoreAdapter("/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/Y11R5P1/Egor/Main.java");
        ObjectStore store = new ObjectStore(Properties.CODEJAM_OBJECT_STORE);
        adapter.storeClasses(store);
    }
}
