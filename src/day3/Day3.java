package day3;

import util.FileUtil;

public class Day3 {
	
  public static String[] input = FileUtil.readFileLines("res/day3/input.txt");

  public static void main(String[] args) {
    int possible = 0;
    for(int i = 0; i < input.length; i++){
    	if(new Triangle(input[i]).isPossible()){
    		possible++;
    	}
    }
    System.out.println(possible);
  }
  
  public static class Triangle{
	  int a;
	  int b;
	  int c;
	  public Triangle(String in){
		  String[] sides = in.trim().split("\\s+");
		  a = Integer.parseInt(sides[0]);
		  b = Integer.parseInt(sides[1]);
		  c = Integer.parseInt(sides[2]);
	  }
	  public boolean isPossible(){
		  return (a+b+c) > 2 * Math.max(a, Math.max(b, c));
	  }
  }
}
