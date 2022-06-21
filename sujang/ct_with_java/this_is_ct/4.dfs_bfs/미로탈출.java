import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 미로탈출 {

	public static int n, m;
	public static int[][] graph;

	public static int[] dx = {0, 0, 1, -1};
	public static int[] dy = {1, -1, 0, 0};

	public static class Node {

		private int x;
		private int y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}

		public int getX() {
			return x;
		}

		public int getY() {
			return y;
		}
	}

	public static int bfs(int x, int y) {
		Queue<Node> que = new LinkedList<>();
		que.offer(new Node(x, y));

		while (!que.isEmpty()) {
			Node node = que.poll();
			x = node.getX();
			y = node.getY();

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
					continue;
				}
				if (graph[nx][ny] == 1) {
					graph[nx][ny] = graph[x][y] + 1;
					que.offer(new Node(nx, ny));
				}
			}
		}
		return graph[n - 1][m - 1];
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		n = sc.nextInt();
		m = sc.nextInt();
		sc.nextLine();
		graph = new int[n][m];

		for (int i = 0; i < n; i++) {
			String line = sc.nextLine();
			for (int j = 0; j < m; j++) {
				graph[i][j] = line.charAt(j) - '0';
			}
		}
		System.out.println(bfs(0, 0));
	}

}
