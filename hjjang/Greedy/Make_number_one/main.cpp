#include <iostream>
#include <algorithm>


using namespace std;

int N,K;
int result = 0;
int main() {

    cin >> N >> K;

    while(1)
    {
        int target = (N / K) * K;
        result += N - target;
        N = target;

        if (N < K) break;

        result += 1;
        N / K ;
    }
    result += (N - 1);
    cout << result << "\n";
    return 0;
}
