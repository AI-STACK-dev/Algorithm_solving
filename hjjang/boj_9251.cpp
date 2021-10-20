#include<iostream>
#include <cstring>
#include <algorithm>

using namespace std;
const int MAX = 1005;
int Table[MAX][MAX];
char str1[MAX];
char str2[MAX];
int N, M;


class LCS {
public:
	void find_answer(int N,int M);
};

void LCS::find_answer(int N, int M)
{
	for (int i = 1; i <=N; i++)
	{
		for (int j = 1; j <=M; j++)
		{
			if (str1[i-1] == str2[j-1]) {
				Table[i][j] = Table[i - 1][j - 1] + 1;
			}
			else {
				Table[i][j] = max(Table[i - 1][j], Table[i][j - 1]);
			}
		}
	}
	cout << Table[N][M] << "\n";
}

int main()
{
	cin >> str1;
	cin >> str2;

	if (strlen(str1) < strlen(str2)) {
		swap(str1, str2);
	}

	N = strlen(str1);
	M = strlen(str2);

	LCS L1;
	L1.find_answer(N, M);
	
	return 0;
}
