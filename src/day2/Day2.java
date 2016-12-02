package day2;

public class Day2 {

  /**
   * @param args
   */

  enum Instruction{
    R, L, U, D
  }

  public static String[] input = {"RDLRUUULRRDLRLLRLDDUDLULULDDULUDRRUURLRLLUULDURRULLRULDRRDLLULLRLLDRLDDRRRRLLRLURRRDRDULRDUULDDDULURUDDRRRUULUDRLLUUURLUDRUUUDRDUULLRLLUDDRURRDDDRDLUUURLRLLUDRURDUDUULDDLLRDURULLLURLDURLUUULDULDDULULLLRRUDLRUURDRDLLURLUDULDUUUURRLDLUDRULUDLDLLDRLDDDRRLLDUDLLRRDDDRLUDURLLLDRUDDLDDRRLUDRRDUDLRRLULDULURULDULUULDRLLDRUUDDRLLUDRULLRRRLRDLRLUDLRULDRDLRDRLRULUDUURRUUULLDDDDUDDLDDDDRRULRDLRDDULLDLDLLDLLDLLDRRDDDRDDLRRDDDRLLLLURRDLRRLDRURDDURDULDDRUURUDUDDDRDRDDRLRRLRULLDRLDLURLRLRUDURRRDLLLUDRLRDLLDDDLLUDRLDRRUUDUUDULDULLRDLUDUURLDDRUDR",
    "URULDDLDDUDLLURLUUUUUULUDRRRDDUDURDRUURLLDRURLUULUDRDRLLDRLDULRULUURUURRLRRDRUUUDLLLLRUDDLRDLLDUDLLRRURURRRUDLRLRLLRULRLRLRDLRLLRRUDDRLRUDULDURDLDLLLRDRURURRULLLDLLRRDRLLDUUDLRUUDDURLLLDUUDLRDDURRDRRULLDRLRDULRRLLRLLLLUDDDRDRULRRULLRRUUDULRRRUDLLUUURDUDLLLURRDDUDLDLRLURDDRRRULRRUDRDRDULURULRUDULRRRLRUDLDDDDRUULURDRRDUDLULLRUDDRRRLUDLRURUURDLDURRDUUULUURRDULLURLRUUUUULULLDRURULDURDDRRUDLRLRRLLLLDDUURRULLURURRLLDRRDDUUDLLUURRDRLLLLRLUDUUUDLRLRRLDURDRURLRLRULURLDULLLRRUUUDLLRRDUUULULDLLDLRRRDUDDLRULLULLULLULRU",
    "DURUUDULRRLULLLDDUDDLRRDURURRRDDRRURDRURDRLULDUDUDUULULDDUURDDULRDUDUDRRURDRDDRLDRDRLDULDDULRULLDULURLUUDUDULRDDRRLURLLRRDLLDLDURULUDUDULDRLLRRRUDRRDDDRRDRUUURLDLURDLRLLDUULLRULLDDDDRULRRLRDLDLRLUURUUULRDUURURLRUDRDDDRRLLRLLDLRULUULULRUDLUDULDLRDDDDDRURDRLRDULRRULRDURDDRRUDRUDLUDLDLRUDLDDRUUULULUULUUUDUULDRRLDUDRRDDLRUULURLRLULRURDDLLULLURLUDLULRLRRDDDDDRLURURURDRURRLLLLURLDDURLLURDULURUUDLURUURDLUUULLLLLRRDUDLLDLUUDURRRURRUUUDRULDDLURUDDRRRDRDULURURLLDULLRDDDRRLLRRRDRLUDURRDLLLLDDDDLUUURDDDDDDLURRURLLLUURRUDLRLRRRURULDRRLULD",
    "LLUUURRDUUDRRLDLRUDUDRLRDLLRDLLDRUULLURLRRLLUDRLDDDLLLRRRUDULDLLLDRLURDRLRRLURUDULLRULLLURRRRRDDDLULURUDLDUDULRRLUDDURRLULRRRDDUULRURRUULUURDRLLLDDRDDLRRULRDRDRLRURULDULRRDRLDRLLDRDURUUULDLLLRDRRRLRDLLUDRDRLURUURDLRDURRLUDRUDLURDRURLRDLULDURDDURUUDRLULLRLRLDDUDLLUUUURLRLRDRLRRRURLRULDULLLLDLRRRULLUUDLDURUUUDLULULRUDDLLDLDLRLDDUDURDRLLRRLRRDDUDRRRURDLRLUUURDULDLURULUDULRRLDUDLDDDUUDRDUULLDDRLRLLRLLLLURDDRURLDDULLULURLRDUDRDDURLLLUDLLLLLUDRDRDLURRDLUDDLDLLDDLUDRRDDLULRUURDRULDDDLLRLDRULURLRURRDDDRLUUDUDRLRRUDDLRDLDULULDDUDURRRURULRDDDUUDULLULDDRDUDRRDRDRDLRRDURURRRRURULLLRRLR",
    "URLULLLDRDDULRRLRLUULDRUUULDRRLLDDDLDUULLDRLULRRDRRDDDRRDLRRLLDDRDULLRRLLUDUDDLDRDRLRDLRDRDDUUDRLLRLULLULRDRDDLDDDRLURRLRRDLUDLDDDLRDLDLLULDDRRDRRRULRUUDUULDLRRURRLLDRDRRDDDURUDRURLUDDDDDDLLRLURULURUURDDUDRLDRDRLUUUULURRRRDRDULRDDDDRDLLULRURLLRDULLUUDULULLLLRDRLLRRRLLRUDUUUULDDRULUDDDRRRULUDURRLLDURRDULUDRUDDRUURURURLRDULURDDDLURRDLDDLRUDUUDULLURURDLDURRDRDDDLRRDLLULUDDDRDLDRDRRDRURRDUDRUURLRDDUUDLURRLDRRDLUDRDLURUDLLRRDUURDUDLUDRRL"};

  public static void main(String[] args) {
    move(0, 0, new KeyPad1());
    System.out.println("");
    move(0, 0, new KeyPad2());
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

  public static interface KeyPad{
    void print();
    void move(Instruction inst);
    boolean exists();
  }
  public static class KeyPad1 implements KeyPad{
    static protected String[] line1 = new String[]{"1","2","3"};
    static protected String[] line2 = new String[]{"4","5","6"};
    static protected String[] line3 = new String[]{"7","8","9"};
    static String[][] keys = new String[][]{line1, line2, line3};
    static int x;
    static int y;

    public KeyPad1(){
      x = 1;
      y = 1;
    }

    @Override
    public void print() {
      System.out.print(keys[y][x]);
    }

    @Override
    public void move(Instruction inst){
      switch (inst){
      case R : x++; if(!exists()){x--;}; break;
      case L : x--; if(!exists()){x++;};break;
      case U : y--; if(!exists()){y++;};break;
      default : y++; if(!exists()){y--;};break;
      }
    }

    @Override
    public boolean exists() {
      if(x < 0 || y < 0 || x > line1.length || y > keys.length){
        return false;
      }
      return true;
    }
  }

  public static class KeyPad2 implements KeyPad{
    static private String[] line1 = new String[]{null, null,"1",null, null};
    static private String[] line2 = new String[]{null,"2","3","4", null};
    static private String[] line3 = new String[]{"5","6","7","8", "9"};
    static private String[] line4 = new String[]{null,"A","B","C", null};
    static private String[] line5 = new String[]{null, null,"D",null, null};
    static String[][] keys = new String[][]{line1, line2, line3, line4, line5};
    int x;
    int y;

    public KeyPad2(){
      x = 0;
      y = 3;
    }

    @Override
    public void print() {
      System.out.print(keys[y][x]);
    }

    @Override
    public void move(Instruction inst){
      switch (inst){
      case R : x++; if(!exists()){x--;}; break;
      case L : x--; if(!exists()){x++;};break;
      case U : y--; if(!exists()){y++;};break;
      default : y++; if(!exists()){y--;};break;
      }
    }
    @Override
    public boolean exists() {
      if(x < 0 || y < 0 || x == line1.length || y == keys.length || keys[y][x] == null){
        return false;
      }
      return true;
    }
  }

}
