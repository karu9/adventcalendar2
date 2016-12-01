package day1;

import java.util.ArrayList;
import java.util.List;

public class Day1 {

  /**
   * @param args
   */
  public static void main(String[] args) {
    // TODO Auto-generated method stub
    String[] input = "L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2".split(", ");

    int degrees = 0;
    int x = 0;
    int y = 0;
    List<String> xys = new ArrayList<String>();

    for(int i = 0; i < input.length; i++){
      String direction = input[i].substring(0,1);
      int pace = Integer.parseInt(input[i].substring(1, input[i].length()));
      int angle = direction.equals("R") ? 90 : -90;
      if(degrees + angle < 0){
        degrees += 360;
      }
      degrees = (degrees + angle) % 360;
      int previousx = x;
      int previousy = y;
      switch (degrees){
        case 0 : x += pace; break;
        case 90 : y += pace; break;
        case 180 : x -= pace; break;
        default : y -= pace; break;
      }
      if(x - previousx != 0){
        int toadd = x - previousx > 0 ? 1: -1;
        for(int j = 1; j < pace + 1; j++){
          int xx = previousx + toadd * j;
          String xy = xx + "," + previousy;
          if(xys.contains(xy)){
            System.out.println(Math.abs(xx)+ Math.abs(previousy));
            break;
          }
          else{
            xys.add(xy);
          }
        }
      }
      else{
        int toadd = y - previousy > 0 ? 1: -1;
        for(int j = 1; j < pace + 1; j++){
          int yy = previousy + toadd * j;
          String xy = previousx + "," + yy ;
          if(xys.contains(xy)){
            System.out.println(Math.abs(previousx)+ Math.abs(yy));
            break;
          }
          else{
            xys.add(xy);
          }
        }
      }
    }
    System.out.println(Math.abs(x)+ Math.abs(y));
  }
}
