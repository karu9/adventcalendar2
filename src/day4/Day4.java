package day4;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import util.FileUtil;

public class Day4 {

	public static String[] input = FileUtil.readFileLines("res/day4/input.txt");
	public static String alphabet = "abcdefghijklmnopqrstuvwxyz";
	public static long sum = 0;

	public static void main(String[] args) {
		readroom(0);
	}

	private static void readroom(int i) {
		if(i == input.length){
			System.out.println(sum);
		}
		else{
			Room room = new Room(input[i]);
			if(room.isReal()){
				sum += room.sectorId;
			}
			if("northpole object storage".equalsIgnoreCase(room.secretCode)){
				System.out.println(room.sectorId);
			}
			readroom(i+1);
		}
	}

	public static class Room{
		int sectorId;
		String checkSum;
		Map<String, Integer> occurences;
		String secretCode;
		public Room(String roomInput){
			String[] raw = roomInput.split("-");
			String sectorIdAndChecksum = raw[raw.length - 1];
			sectorId = Integer.parseInt(sectorIdAndChecksum.substring(0, sectorIdAndChecksum.length() - 7));
			checkSum = sectorIdAndChecksum.substring(sectorIdAndChecksum.length() - 6, sectorIdAndChecksum.length() - 1);
			createMap(raw);
			secretCode = getSecretCode(raw);
		}

		public String getSecretCode(String[] raw) {
			String secretCode = "";
			for(int i = 0; i < raw.length - 1; i++){
				secretCode += " ";
				for(int j = 0; j < raw[i].length(); j++){
					secretCode += alphabet.charAt((alphabet.indexOf(raw[i].substring(j, j+1)) + sectorId) % 26);
				}
			}
			return secretCode.trim();
		}

		public boolean isReal() {
			List<Integer> occs = new ArrayList<Integer>(occurences.values());
			Collections.sort(occs);
			Collections.reverse(occs);
			Integer[] maxOccs = occs.subList(0, 5).toArray(new Integer[5]);
			for(int i = 0; i < 5; i++){
				if(!maxOccs[i].equals(occurences.get(checkSum.substring(i, i+1)))){
					return false;
				}
			}
			return true;
		}

		private void createMap(String[] raw) {
			occurences = new HashMap<String, Integer>();
			for(int i = 0; i < raw.length - 1; i++){
				for(int j = 0; j < raw[i].length(); j++){
					String curr = raw[i].substring(j, j+1);
					if(occurences.containsKey(curr)){
						occurences.put(curr, occurences.get(curr) + 1);
					}
					else{
						occurences.put(curr, 1);
					}
				}
			}
		}
	}
}
