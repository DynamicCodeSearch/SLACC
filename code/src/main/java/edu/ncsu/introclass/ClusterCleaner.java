package edu.ncsu.introclass;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import edu.ncsu.store.BaseStorage;
import edu.ncsu.store.IClusterStore;
import gumtree.spoon.AstComparator;

public class ClusterCleaner {

    private IClusterStore store;

    private final static AstComparator AST_COMPARATOR = new AstComparator();

    public ClusterCleaner() {
        this.store = BaseStorage.loadClusterStore(IntroClassUtils.DATASET);
    }

    public void clean(){
        JsonArray clusters = store.getClusters("non_overlapping");
        for (JsonElement c: clusters) {
            JsonObject cluster = (JsonObject) c;
            Integer clusterId = cluster.get("cluster_id").getAsInt();
            for (JsonElement f : cluster.get("functions").getAsJsonArray()) {
                String body = f.getAsJsonObject().get("body").getAsString();

                System.out.println(body);
                System.out.println("\n **** \n");
            }
            System.exit(0);
        }
    }

    private void codeDiff(String codeA, String codeB) {

    }

    private static void astGen(String code) {

    }

    private static void testClean() {
        String codeA = "public static IntObj func_b93593d54eda441380ac71e70da65afc(IntObj sum, CharObj next){\n" +
                "    ;\n" +
                "    sum.value = sum.value + next.value;\n" +
                "    return sum;\n" +
                "}";

    }


    public static void main(String[] args) {
        ClusterCleaner cleaner = new ClusterCleaner();
        cleaner.clean();
    }

}
