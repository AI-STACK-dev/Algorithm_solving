// string_reversed.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>

std::string input;

int zero_group;
int one_group;

int main()
{
	std::cin >> input;

	if (input[0] == '0')
	{
		zero_group++;
	}
	else
	{
		one_group++;
	}

	for (int i = 0; i < input.size() - 1; i++)
	{
		if (input[i] != input[i + 1])
		{
			if (input[i + 1] == '0')
			{
				zero_group++;
			}
			else 
			{
				one_group++;
			}
		}
	}

	//std::cout << zero_group << ", " << one_group << std::endl;
	std::cout << std::min(zero_group, one_group) << std::endl;
	return EXIT_SUCCESS;
}

