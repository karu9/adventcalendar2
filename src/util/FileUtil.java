package util;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class FileUtil {
  public static String readFile(String fileURL){
    String output = "";
    try {
      FileInputStream file = new FileInputStream(new File(fileURL));
      while(file.available() > 0){
        output += String.valueOf(Character.toChars(file.read())[0]);
      }
    }
    catch (IOException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    return output;
  }


  public static String[] readFileLines(String fileURL){
    return readFile(fileURL).split("\r\n");
  }
}
