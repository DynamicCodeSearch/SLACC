package edu.ncsu.database;

import edu.ncsu.utils.Utils;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.logging.Logger;

public class MongoDriver {

    private static final Logger LOGGER = Logger.getLogger(MongoDriver.class.getName());

    private static String getDefaultHostName() {
        try {
            String hostName = InetAddress.getLocalHost().getHostName();
            return hostName;
        } catch (UnknownHostException e) {
            LOGGER.severe(String.format("Failed to fetch host name. Exception: %s", e.getMessage()));
            throw new RuntimeException(e);
        }
    }

    public static String getHostName() {
        String mongoHome = System.getenv("MONGO_HOME");
        if ( mongoHome != null && !mongoHome.isEmpty()) {
            String fileName = Utils.pathJoin(mongoHome, "host_machine.txt");
            String hostName = Utils.getFileContent(fileName);
            if (hostName == null) {
                return getDefaultHostName();
            }
            return hostName;
        }
        return getDefaultHostName();
    }

    public static void main(String[] args) {
        LOGGER.info(String.format("HostName of MongoD Server: %s", getHostName()));
    }

}
