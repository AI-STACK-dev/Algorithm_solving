package b10818;

import java.util.Arrays;
import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		int N = s.nextInt();
		int[] arr = new int[N];
		
		for(int i=0; i<N;i++) {
			arr[i] = s.nextInt();
		}
		s.close();
		Arrays.sort(arr);
		System.out.println(arr[0]+" "+arr[N-1]);

	}

}
