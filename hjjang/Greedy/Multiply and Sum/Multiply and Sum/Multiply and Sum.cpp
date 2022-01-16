// Multiply and Sum.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::string input;
const int MAX = 20;
int arr[MAX];

int main()
{
	std::cin >> input;
	
	long long result = (long long)(input[0] - '0');

	for (int i = 1; i < input.size(); i++)
	{
		int num = input[i] - '0';
		
		if (num <= 1 || result <= 1)
		{
			result += num;
		}
		else
		{
			result *= num;
		}
	}

	std::cout << result << std::endl;


	/*
	std::istringstream ss(input);
	std::string stringBuffer;
	std::vector<std::string> x;

	while (std::getline(ss, stringBuffer,' '))
	{

	}
	*/

	return EXIT_SUCCESS;
}

