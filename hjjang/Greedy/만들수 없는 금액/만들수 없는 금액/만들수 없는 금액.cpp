// 만들수 없는 금액.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>

const int MAX = 1005;

int main()
{
	int Coin_Number;
	std::cin >> Coin_Number;
	int Input_Coin = 0;
	int Coin_arr[MAX];
	int Target = 1;

	for (int i = 0; i < Coin_Number; i++)
	{
		std::cin >> Input_Coin;
		Coin_arr[i] = Input_Coin;
	}

	std::sort(Coin_arr, Coin_arr + Coin_Number);


	for (auto coin : Coin_arr)
	{
		if (Target < coin)
		{
			std::cout << Target << std::endl;
			break;
		}
		else
		{
			Target += coin;
		}
	}
	return EXIT_SUCCESS;
}

