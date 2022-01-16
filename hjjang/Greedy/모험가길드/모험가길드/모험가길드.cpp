// 모험가길드.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <algorithm>

const int MAX = 100005;
int person;

int count; //모험가를 그때 저장할 변수
int group_number; //전체 그룹수 

int fear[MAX];

int main()
{
	std::cin >> person;

	for (int i = 0; i < person; i++)
	{
		std::cin >> fear[i];
	}

	std::sort(fear, fear + person);

	for (int i = 0; i < person; i++)
	{
		count += 1;
		if (count >= fear[i])
		{
			group_number++;
			count = 0;
		}
	}

	std::cout << group_number << std::endl;


	return EXIT_SUCCESS;
}

