package b10951;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		while(s.hasNextInt()) {
			int a = s.nextInt();
			int b = s.nextInt();
			System.out.println(a+b);
		}
		s.close();
		
	}
}
