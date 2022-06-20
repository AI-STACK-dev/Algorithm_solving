public class ex1 {

	public static void main(String[] args) {
		int n = 1260;
		int cnt = 0;
		int[] coinTypes = {500, 100, 50, 10};

		for (int i = 0; i < 4; i++) {
			int coin = coinTypes[i];
			cnt += n / coin;
			n %= coin;
		}

		System.out.println(cnt);
	}
}
