package edu.ncsu.crawler;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Enumeration;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import edu.ncsu.config.Properties;


public class CodeJamCrawler {

    private static final Logger LOGGER = Logger.getLogger(CodeJamCrawler.class.getName());

    private static final String BASE_URL = "http://www.go-hero.net/jam/";

    private static final String MATCH_STRING = "http://code.google.com/codejam/contest/scoreboard/do?cmd=GetSourceCode";

    private static void writeFile(InputStream inputStream, File destFile, String packageName) {
        try {
            FileOutputStream fos = new FileOutputStream(destFile);
            String fileHeader = "package " + packageName + ";\n\n";
            fos.write(fileHeader.getBytes());
            int bufferSize = 4096;
            byte[] buf = new byte[bufferSize];
            int n = inputStream.read(buf);
            while (n >= 0) {
                fos.write(buf, 0, n);
                n = inputStream.read(buf);
            }
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

    public static void main(String[] args) throws Exception{
        if (args.length < 3) {
            LOGGER.log(Level.SEVERE, "Illegal number of arguments. Provide year, round and id.");
            System.exit(0);
        }
        try {
            int year = Integer.parseInt(args[0]);
            System.out.println(String.format("Code jam year: %d", year));
//			int year = 11;
            int round = Integer.parseInt(args[1]);
            System.out.println(String.format("Code jam round (World Finals = 6): %d", round));
//            int round = 5;
            int problemId = Integer.parseInt(args[2]);
            System.out.println(String.format("Problem id: %d", problemId));
//            int problemId = 2;
            String problemKey = String.format("Y%dR%dP%d", year, round, problemId);
            String finalUrl = BASE_URL + year + "/solutions/" + round + "/" + problemId + "/Java";
            String codeRepo = Properties.CODEJAM_JAVA_FOLDER;

            File problemDir = new File(codeRepo + "/" + problemKey);
            if (!problemDir.exists()) {
                problemDir.mkdirs();
            }
            Document codeJamHome = Jsoup.connect(finalUrl).validateTLSCertificates(false).get();

            int userCounter = 0;
            for (Element e: codeJamHome.select("a[href]")) {
                String link = e.attr("abs:href");
                if (link.startsWith(MATCH_STRING)) {
                    String[] sep = link.split("&");

                    String userString = sep[sep.length - 1];
                    int eqPos = userString.indexOf("=");
                    String userName = userString.substring(eqPos + 1, userString.length())
                            .replaceAll("\\.", "").replaceAll("\\d", "");
                    File userDir = new File(problemDir.getAbsolutePath(), userName);
                    if (!userDir.exists()) {
                        userDir.mkdirs();
                    }
                    File tmpFile = File.createTempFile("arc", ".zip", userDir);
                    tmpFile.deleteOnExit();
                    downloadFile(tmpFile, link);
                    String packageName = problemKey + "." + userName;
                    userCounter += unpackArchive(tmpFile, userDir, packageName);
                }
            }
            System.out.println("Total code files: " + userCounter);
        } catch (Exception ex) {
//			ex.printStackTrace();
            throw ex;
        }
    }

}
