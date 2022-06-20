import java.util.Scanner;

// aka 숫자 카드 게임
public class ex3 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(); int m = sc.nextInt();

		int result = 0;
		for (int i = 0; i < n; i++) {
			int minVal = 10001;
			for (int j = 0; j < m; j++) {
				int x = sc.nextInt();
				minVal = Math.min(minVal, x);
			}
			result = Math.max(result, minVal);
		}
		System.out.println("result = " + result);
	}
}
