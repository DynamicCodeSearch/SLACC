package edu.ncsu.visitors.blocks;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

import java.util.Set;

public class GeneratedFunction {

    private String name;

    private String body;

    private String inputKey;

    private String sourceFile;

    private String generatedFile;

    private Set<Integer> linesTouched;

    private Set<Integer> span;

    private JsonObject returnMeta;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public String getInputKey() {
        return inputKey;
    }

    public void setInputKey(String inputKey) {
        this.inputKey = inputKey;
    }

    public String getSourceFile() {
        return sourceFile;
    }

    public void setSourceFile(String sourceFile) {
        this.sourceFile = sourceFile;
    }

    public String getGeneratedFile() {
        return generatedFile;
    }

    public void setGeneratedFile(String generatedFile) {
        this.generatedFile = generatedFile;
    }

    public Set<Integer> getLinesTouched() {
        return linesTouched;
    }

    public void setLinesTouched(Set<Integer> linesTouched) {
        this.linesTouched = linesTouched;
    }

    public Set<Integer> getSpan() {
        return span;
    }

    public void setSpan(Set<Integer> span) {
        this.span = span;
    }

    public JsonObject getReturnMeta() {
        return returnMeta;
    }

    public void setReturnMeta(JsonObject returnMeta) {
        this.returnMeta = returnMeta;
    }

    public JsonObject toJson() {
        JsonObject json = new JsonObject();
        json.addProperty("name", name);
        json.addProperty("body", body);
        json.addProperty("inputKey", inputKey);
        json.addProperty("filePath", generatedFile);
        json.addProperty("baseFilePath", sourceFile);
        if (this.linesTouched != null && this.linesTouched.size() > 0) {
            JsonArray linesTouched = new JsonArray();
            for (Integer line: this.linesTouched)
                linesTouched.add(line);
            json.add("linesTouched", linesTouched);
        }
        if (this.span != null) {
            JsonArray span = new JsonArray();
            for (Integer line: this.span)
                span.add(line);
            json.add("span", span);
        }
        json.add("return", returnMeta);
//        json.add("argNamesKeysMap", Utils.toJson(getArgComboKeyMap()));
        return json;
    }

}
