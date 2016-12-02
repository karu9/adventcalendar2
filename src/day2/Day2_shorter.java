package day2;

import util.FileUtil;

public class Day2_shorter {

  /**
   * @param args
   */

  enum Instruction{
    R, L, U, D
  }

  public static String[] input = FileUtil.readFileLines("res/day2/input.txt");

  static String[][] keys1 = new String[][]{
      new String[]{"1","2","3"},
      new String[]{"4","5","6"},
      new String[]{"7","8","9"}};

  static String[][] keys2 = new String[][]{
      new String[]{null, null,"1",null, null},
      new String[]{null,"2","3","4", null},
      new String[]{"5","6","7","8", "9"},
      new String[]{null,"A","B","C", null},
      new String[]{null, null,"D",null, null}};


  public static void main(String[] args) {
    move(0, 0, new KeyPad(keys1, 1, 1));
    System.out.println();
    move(0, 0, new KeyPad(keys2, 0, 3));
  }

  private static void move(int i, int j, KeyPad keyPad) {
    if(j != input.length){
      if(i == input[j].length()){
        keyPad.print();
        move(0, j+1, keyPad);
      }
      else{
        keyPad.move(Instruction.valueOf(input[j].substring(i, i+1)));
        move(i+1, j, keyPad);
      }
    }
  }

  public static class KeyPad{
    String[][] keys;
    int x;
    int y;

    public KeyPad(String[][] keyZ, int startX, int startY){
      x = startX;
      y = startY;
      keys = keyZ;
    }

    public void print() {
      System.out.print(keys[y][x]);
    }

    public void move(Instruction inst){
      switch (inst){
      case R : x++; if(!exists()){x--;}; break;
      case L : x--; if(!exists()){x++;};break;
      case U : y--; if(!exists()){y++;};break;
      default : y++; if(!exists()){y--;};break;
      }
    }

    public boolean exists() {
      if(x < 0 || y < 0 || x == keys[0].length || y == keys[0].length || keys[y][x] == null){
        return false;
      }
      return true;
    }
  }

}
