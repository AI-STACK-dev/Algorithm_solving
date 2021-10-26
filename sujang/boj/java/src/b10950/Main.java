package b10950;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		int arr[] = new int[n];
		for(int i =0; i<n;i++) {
			int a = s.nextInt();
			int b = s.nextInt();
			arr[i] = a+b;
		}
		s.close();
		for (int k : arr) {
			System.out.println(k);
		}
	}

}
