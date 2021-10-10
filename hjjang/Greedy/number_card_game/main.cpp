#include <iostream>
#include <algorithm>

using namespace std;
int N,M;
const int MAX  = 105;
int arr[MAX][MAX];
int answer[105];
void find_answer()
{
    for(int i =0; i < N; i++)
    {
        int Min_val = 1000005;
        for(int j =0; j < M;j++)
        {
            if(arr[i][j] < Min_val)
                Min_val = arr[i][j];
        }
        answer[i] = Min_val;
    }
}
int main() {

    cin >> N >> M;

    for(int i= 0; i < N; i++)
    {
        for(int j =0; j < M; j++)
        {
            cin >> arr[i][j];
        }
    }
    find_answer();
    for(int i =0; i < N; i++)
        cout << answer[i] << " ";
    cout << "\n";

    sort(answer,answer+ N);

    cout << answer[N-1] << "\n";

    return 0;
}
