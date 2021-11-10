package main.solution;

import java.util.List;
import java.util.ArrayList;
import java.io.*;

public class Solution {
    public static List<String> parse(String filePath) throws Exception {
        List<String> result = new ArrayList<String>();
        File file = new File(filePath);
        if (file.exists()) {
            BufferedReader inFile = new BufferedReader(new FileReader(file));
            String sLine = null;
            while ((sLine = inFile.readLine()) != null) {
                result.add(sLine);
            }
        }
        return result;
    };
}
