import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

// aka 큰 수의 법칙
public class ex2 {

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		int k = sc.nextInt();

		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		Arrays.sort(arr);

		int cnt = (m/(k+1))*k + (m%(k+1));

		int result = cnt*arr[n-1] + (m-cnt)*arr[n-2];

		System.out.println("result = " + result);
	}
}
