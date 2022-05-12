package com.java.StringBuilder;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Calendar;
import java.util.GregorianCalendar;

public class LoggingListener implements EventListener {
    private File log;

    public LoggingListener(String log_filename) {
        FileWriter fw;
        try {
            this.log = new File(log_filename);
            log.createNewFile();
            fw = new FileWriter(log.getName());
            fw.write("----TIME----   ----COMMAND----   ----STRING----\n");
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void update(EventType eventType, String newString) {
        FileWriter fw;
        try {
            fw = new FileWriter(log.getName(), true);
            Calendar calendar = new GregorianCalendar();
            String data = "%-12s   %-15s   %-14s\n";
            fw.write(String.format(data, calendar.get(Calendar.HOUR) + ":" + calendar.get(Calendar.MINUTE) +
                            ":" + calendar.get(Calendar.SECOND) + ":" + calendar.get(Calendar.MILLISECOND),
                    eventType.getType(), newString));
            fw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
