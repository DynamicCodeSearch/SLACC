package edu.ncsu.codejam;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Enumeration;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

import edu.ncsu.config.Settings;
import edu.ncsu.utils.InMemoryJavaCompiler;
import edu.ncsu.utils.Utils;
import org.apache.commons.io.IOUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;


public class Crawler {

    private static final Logger LOGGER = Logger.getLogger(Crawler.class.getName());

    private static final String BASE_URL = "http://www.go-hero.net/jam/";

    private static final String MATCH_STRING = "http://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode";

    private static void writeFile(InputStream inputStream, File destFile, String packageName) {
        try {
            FileOutputStream fos = new FileOutputStream(destFile);
            String fileHeader = "package " + packageName + ";\n\n";
            fos.write(fileHeader.getBytes());
            String content = IOUtils.toString(inputStream).replaceAll("^\\s*package\\s+.+;", "");
//            content = content.replaceAll("\\s*private\\s+", "");
            fos.write(IOUtils.toByteArray(content));
            fos.flush();
            fos.close();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    private static int unpackArchive(File tmpFile, File pkgDir, String packageName) {
        try {
            ZipFile zipFile = new ZipFile(tmpFile);
            int counter = 0;
            for (Enumeration entries = zipFile.entries(); entries.hasMoreElements();) {
                ZipEntry entry = (ZipEntry)entries.nextElement();
                String fileName = pkgDir.getAbsolutePath() + "/" + entry.getName();
                File javaFile = new File(fileName);
                writeFile(zipFile.getInputStream(entry), javaFile, packageName);
                counter++;
            }
            return counter;
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        return 0;
    }

    private static void downloadFile(File filename, String fileURL) {
        try {
            long startTime = System.currentTimeMillis();

            URL url = new URL(fileURL);
            URLConnection conn = url.openConnection();
            conn.setDoInput(true);
            conn.setDoInput(true);
            // Go to the redirected https page to obtain authentication token.
            conn = new URL(conn.getHeaderField("location")).openConnection();
            conn.setDoInput(true);
            conn.setDoInput(true);
            InputStream reader = conn.getInputStream();
            FileOutputStream writer = new FileOutputStream(filename);
            byte[] buffer = new byte[1024];
            int totalBytesRead = 0;
            int bytesRead = 0;
            while ((bytesRead = reader.read(buffer)) > 0) {
                writer.write(buffer, 0, bytesRead);
                buffer = new byte[1024];
                totalBytesRead += bytesRead;
            }
            long endTime = System.currentTimeMillis();
            LOGGER.info("Done: " + fileURL + ". " + Integer.toString(totalBytesRead) +
                    " bytes read (" + (endTime - startTime) + " millseconds).");
            writer.close();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int crawlLink(String link, String problemKey) {
        try {
            String codeRepo = Settings.getDatasetSourceFolder(CodejamUtils.DATASET);
            File problemDir = new File(codeRepo + "/" + problemKey);
            if (!problemDir.exists()) {
                problemDir.mkdirs();
            }
            String[] sep = link.split("&");
            String userString = sep[sep.length - 1];
            int eqPos = userString.indexOf("=");
            String userName = userString.substring(eqPos + 1).replaceAll("\\.", "").replaceAll("\\d", "");
            File userDir = new File(problemDir.getAbsolutePath(), userName);
            if (!userDir.exists()) {
                userDir.mkdirs();
            }
            File tmpFile = File.createTempFile("arc", ".zip", userDir);
            tmpFile.deleteOnExit();
            downloadFile(tmpFile, link);
            String packageName = "CodeJam" + "." + problemKey + "." + userName;
            int num_files = unpackArchive(tmpFile, userDir, packageName);
            for (String javaFileName: Utils.listFilesWithExtension(userDir.getAbsolutePath(), ".java", true, true)) {
                if (!InMemoryJavaCompiler.compile(javaFileName, false)) {
                    LOGGER.info(String.format("%s has a compilation error. Deleting it.", javaFileName));
                    File javaFile = new File(javaFileName);
                    File parentFolder = javaFile.getParentFile();
                    javaFile.delete();
                    List<String> kids = Utils.listFilesWithExtension(parentFolder.getAbsolutePath(), ".java", false, false);
                    if (kids.size() == 0)
                        parentFolder.delete();
                    num_files -= 1;
                }
            }
            return num_files;
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void crawl(int year, int round, int problemId){
        String problemKey = String.format("Y%dR%dP%d", year, round, problemId);
        String finalUrl = BASE_URL + year + "/solutions/" + round + "/" + problemId + "/Java";
        try {
            Document codeJamHome = Jsoup.connect(finalUrl)
                    .userAgent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36")
                    .validateTLSCertificates(false).get();
            int userCounter = 0;
            for (Element e: codeJamHome.select("a[href]")) {
                String link = e.attr("abs:href");
                if (link.startsWith(MATCH_STRING)) {
                    userCounter += crawlLink(link, problemKey);
                }
            }
            System.out.println("Total code files: " + userCounter);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }

    public static void crawlMain(String[] args) {
        if (args.length < 3) {
            LOGGER.log(Level.SEVERE, "Illegal number of arguments. Provide year, round and id.");
            System.exit(0);
        }
        int year = Integer.parseInt(args[0]);
        System.out.println(String.format("Code jam year: %d", year));
//			int year = 11;
        int round = Integer.parseInt(args[1]);
        System.out.println(String.format("Code jam round (World Finals = 6): %d", round));
//            int round = 5;
        int problemId = Integer.parseInt(args[2]);
        System.out.println(String.format("Problem id: %d", problemId));
//            int problemId = 2;
        crawl(year, round, problemId);
    }

    public static void main(String[] args) {
//        crawlMain(new String[]{"12", "5", "1"});
        crawlMain(args);
    }

}
