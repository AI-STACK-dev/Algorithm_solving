class Solution {
    public int solution(int m, int n, String[] map) {
        int answer = 0;
        char[][] board = convert2board(m, n, map);
        
        while (true) {
            int cnt = checkBox(m, n, board);
            if(cnt == 0) break;
            answer += cnt;
            dropBox(m, n, board);
        }
        return answer;
    }
    
    private char[][] convert2board(int m, int n, String[] board) {
        char[][] temp = new char[m][n];
        for (int i=0; i<m; i++) {
            temp[i] = board[i].toCharArray();
        }
        return temp;
    }
    
    private int checkBox(int m, int n, char[][] board) {
		int cnt = 0;
		boolean[][] isValid = new boolean[m][n];
		
		for(int i = 0 ; i < m - 1 ; i++) {
			for(int j = 0 ; j < n - 1 ; j++) {
				if(board[i][j] == ' ') continue;
				checkValid(board, isValid, i, j);
			}
		}
		
		for(int i = 0 ; i < m ; ++i) {
			for(int j = 0 ; j < n ; ++j) {
				if(isValid[i][j]) {
					cnt++;
					board[i][j] = ' ';
				}
			}
		}
        return cnt;
    }
    
	private void checkValid(char[][] board, boolean[][] isValid, int i, int j) {
		char block = board[i][j];
		
		for(int r = i ; r < i + 2 ; r++) {
			for(int c = j ; c < j + 2 ; c++) {
				if(board[r][c] != block) return;
			}
		}
		
		for(int r = i ; r < i + 2 ; r++) {
			for(int c = j ; c < j + 2 ; c++) {
				isValid[r][c] = true;
			}
		}
	}
    
    private void dropBox(int m, int n, char[][] board) {
        for(int i = 0 ; i < n ; i++) {
			for(int j = m - 1 ; j >= 0 ; j--) {
				if(board[j][i] == ' ') {
					for(int nj = j - 1 ; nj >= 0 ; nj--) {
						if(board[nj][i] != ' ') {
							board[j][i] = board[nj][i];
							board[nj][i] = ' ';
							break;
						}
					}
				}
			}
		}   
    }
}
