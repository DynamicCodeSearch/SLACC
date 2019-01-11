package edu.ncsu.visitors.adapters;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.visitor.VoidVisitorAdapter;
import edu.ncsu.utils.InMemoryJavaCompiler;
import edu.ncsu.utils.Utils;
import edu.ncsu.visitors.helpers.VisitorHelper;

import java.util.logging.Logger;

public class PreprocessAdapter extends VoidVisitorAdapter {
    private static final Logger LOGGER = Logger.getLogger(PreprocessAdapter.class.getName());

    private String fileName;

    private CompilationUnit compilationUnit;

    public static void preprocess(String javaFile) {
        String oldSource = Utils.getFileContent(javaFile);
        PreprocessAdapter adapter = new PreprocessAdapter(javaFile);
        String newSource = adapter.compilationUnit.toString();
        Utils.writeFileContent(newSource, adapter.fileName);
        if (!InMemoryJavaCompiler.compile(adapter.fileName, false)) {
            LOGGER.warning(String.format("Preprocessed file '%s' raises compilation error. " +
                    "Reverting to old content ... ", adapter.fileName));
            Utils.writeFileContent(oldSource, adapter.fileName);
        } else {
//            LOGGER.info(String.format("Preprocessed file '%s'.", adapter.fileName));
        }
    }

    private PreprocessAdapter(String javaFile) {
        this.fileName = javaFile;
        this.compilationUnit = VisitorHelper.loadCompilationUnit(javaFile);
        for (TypeDeclaration typeDeclaration: this.compilationUnit.getTypes()) {
            if (typeDeclaration instanceof ClassOrInterfaceDeclaration) {
                parseTypeDeclaration((ClassOrInterfaceDeclaration) typeDeclaration, false);
            }

        }
    }

    private void parseTypeDeclaration(ClassOrInterfaceDeclaration typeDeclaration, boolean isInner) {
        int classModifier = typeDeclaration.getModifiers();
        if (isInner && !ModifierSet.isStatic(classModifier)) {
            classModifier = ModifierSet.addModifier(classModifier, ModifierSet.STATIC);
            typeDeclaration.setModifiers(classModifier);
        }
        for (BodyDeclaration member: typeDeclaration.getMembers()) {
            if (member instanceof FieldDeclaration) {
                FieldDeclaration declaration = (FieldDeclaration) member;
                int modifiers = declaration.getModifiers();
                if (ModifierSet.isPrivate(modifiers)) {
                    modifiers = ModifierSet.removeModifier(modifiers, ModifierSet.PRIVATE);
                    declaration.setModifiers(modifiers);
                }
            } else if (member instanceof MethodDeclaration) {
                MethodDeclaration declaration = (MethodDeclaration) member;
                int modifiers = declaration.getModifiers();
                if (ModifierSet.isPrivate(modifiers)) {
                    modifiers = ModifierSet.removeModifier(modifiers, ModifierSet.PRIVATE);
                    declaration.setModifiers(modifiers);
                }
            } else if (member instanceof ClassOrInterfaceDeclaration){
                parseTypeDeclaration((ClassOrInterfaceDeclaration) member, true);
            }
        }
    }

    private static void testPreprocess() {
        String fileName = "/Users/panzer/Raise/ProgramRepair/CodeSeer/projects/src/main/java/CodeJam/stupid/Dummy.java";
        preprocess(fileName);
    }

    public static void main(String[] args) {
        testPreprocess();
    }

}
