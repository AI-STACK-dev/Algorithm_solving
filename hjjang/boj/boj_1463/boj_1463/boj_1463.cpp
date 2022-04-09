// boj_1463.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

int result,number,count;
int ans,temp;

int main()
{
    std::cin >> number;

    while (number != count)
    {
        ans++;
        temp = ans;
        while (temp != 0)
        {
            if (temp % 1000 == 666)
            {
                count++;
                break;
            }
            else
            {
                temp /= 10;
            }
        }
    }
    std::cout << ans << std::endl;
    return 0;
}


   