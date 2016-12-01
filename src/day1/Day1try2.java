package day1;

import java.util.ArrayList;
import java.util.List;

public class Day1try2 {

  /**
   * @param args
   */
  public static String[] input = "L1, L3, L5, L3, R1, L4, L5, R1, R3, L5, R1, L3, L2, L3, R2, R2, L3, L3, R1, L2, R1, L3, L2, R4, R2, L5, R4, L5, R4, L2, R3, L2, R4, R1, L5, L4, R1, L2, R3, R1, R2, L4, R1, L2, R3, L2, L3, R5, L192, R4, L5, R4, L1, R4, L4, R2, L5, R45, L2, L5, R4, R5, L3, R5, R77, R2, R5, L5, R1, R4, L4, L4, R2, L4, L1, R191, R1, L1, L2, L2, L4, L3, R1, L3, R1, R5, R3, L1, L4, L2, L3, L1, L1, R5, L4, R1, L3, R1, L2, R1, R4, R5, L4, L2, R4, R5, L1, L2, R3, L4, R2, R2, R3, L2, L3, L5, R3, R1, L4, L3, R4, R2, R2, R2, R1, L4, R4, R1, R2, R1, L2, L2, R4, L1, L2, R3, L3, L5, L4, R4, L3, L1, L5, L3, L5, R5, L5, L4, L2, R1, L2, L4, L2, L4, L1, R4, R4, R5, R1, L4, R2, L4, L2, L4, R2, L4, L1, L2, R1, R4, R3, R2, R2, R5, L1, L2".split(", ");
  public static List<Vector> vectors = new ArrayList<Day1try2.Vector>();

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    deliver(0, new Vector(0,0), 0);
  }

  private static void deliver(int iteration, Vector start, int direction) {
    if(iteration == input.length){
      start.print();
    }
    else{

      int gap = Integer.parseInt(input[iteration].substring(1, input[iteration].length()));
      direction = "R".equals(input[iteration].substring(0,1)) ? (direction + 3) % 4 : (direction + 1) % 4;
      start.move(gap, direction);
      deliver(iteration + 1, start, direction);
    }
  }

  public static class Vector{
    int x = 0;
    int y = 0;
    public Vector(int x, int y){
      this.x = x;
      this.y = y;
    }
    public void move(int gap, int direction) {
      if(gap != 0){
        switch (direction) {
        case 0 : x++; break;
        case 1 : y++; break;
        case 2 : x--; break;
        default : y--; break;
        }
        if(vectors.contains(this)){
          print();
        }
        vectors.add(new Vector(x, y));
        move(gap - 1, direction);
      }
    }

    @Override
    public boolean equals(Object o){
      return o instanceof Vector && x == ((Vector) o).x && y == ((Vector) o).y;
    }

    public void print(){
      System.out.println(Math.abs(x) + Math.abs(y));
    }
  }

}
