package b2562;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int[] arr = {in.nextInt(),in.nextInt(),in.nextInt(),
					 in.nextInt(),in.nextInt(),in.nextInt(),
					 in.nextInt(),in.nextInt(),in.nextInt()};
		in.close();
		
		int index = 0;
		int max = 0;
		int count = 0;
		for(int value : arr) {
			count ++;
			if(value > max) {
				max = value;
				index = count;
			}
		}
		System.out.println(max);
		System.out.println(index);
	}
}
