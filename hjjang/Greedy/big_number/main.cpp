#include <iostream>
#include <algorithm>

using namespace std;

int N,M,K;
const int MAX = 1005;
int arr[MAX];
int result;
int first,second;
void find_answer(int first,int second)
{
    while(M > 0)
    {
        for(int i =0; i < K; i++)
        {
            result += first;
            M--;
            if(M == 0) {
                cout << result << "\n";
                return;
            }
        }
        M--;
        result += second;
    }
    cout << result << "\n";
}
int main() {

    cin >> N >> M >> K;

    for(int i =0; i < N; i++)
    {
        cin >> arr[i];
    }
    sort(arr,arr+N);
    first = arr[N -1];
    second = arr[N - 2];
    cout << first << " " << second << "\n";
    find_answer(first,second);

    return 0;
}
