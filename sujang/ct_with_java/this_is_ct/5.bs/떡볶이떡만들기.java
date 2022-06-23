import java.util.Scanner;

public class 떡볶이떡만들기 {

	private static int bs(int start, int end, int[] dd, int n, int target) {
		int result = 0;
		while (start <= end) {

			int mid = (start + end) / 2;
			long total = 0;
			for (int i = 0; i < n; i++) {
				if (dd[i] > mid) {
					total += dd[i] - mid;
				}
			}

			if (total < target) {
				end = mid - 1;
			} else {
				result = mid;
				start = mid + 1;
			}
		}
		return result;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();

		int[] dd = new int[n];
		for (int i = 0; i < n; i++) {
			dd[i] = sc.nextInt();
		}

		System.out.println(bs(0, (int) 1e9, dd, n, m));
	}
}
