package day3;

import util.FileUtil;

public class Day3_2 {

	public static String[] input = FileUtil.readFileLines("res/day3/input.txt");

	public static void main(String[] args) {
		readcolumn(0,0,0);
	}

	private static void readcolumn(int i, int j, int possible) {
		if(i > input.length - 2){
			readcolumn(0, j+1, possible);
		}
		else if(j == 3){
			System.out.println(possible);
		}
		else{
			if(new Triangle(input[i].trim().split("\\s+")[j]+ " " + input[i+1].trim().split("\\s+")[j] + " " + input[i+2].trim().split("\\s+")[j]).isPossible()){
				possible++;
			}
			readcolumn(i+3, j, possible);
		}
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
