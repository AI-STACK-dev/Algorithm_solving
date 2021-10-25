package b10952;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		while(true) {
			int A = s.nextInt();
			int B = s.nextInt();
			
			if (A==0 && B==0) {
				s.close();
				break;
			}
			System.out.println(A+B);
		}
	}

}
