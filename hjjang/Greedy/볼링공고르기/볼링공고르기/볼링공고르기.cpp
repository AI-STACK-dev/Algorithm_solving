// 볼링공고르기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

const int Range_Max = 12;
int ball[Range_Max];
int result;

int main()
{
  
   /*
	* 나의 설계 
	* 배열에 담긴 숫자들이 하나씩 진행 되면서 본인 기준 우측에 있는 숫자들 중 겹치는 개수파악
	* 이를 누적하며 더해간다.
	* 단점: 진행 하면서 중복되는 숫자들을 검사하는게 비효율적
	*/

   /*
    * 교재 설계
	* 숫자들의 개수를 미리 파악 어떤 배열에 따로 저장
	* 천체개수에서 A가정한 숫자를 B는 정할수 없으로 빼주는 방향
	*/

	int N, M;
	std::cin >> N >> M;

	for (int i = 0; i < N; i++)
	{
		int temp_ball;
		std::cin >> temp_ball;
		ball[temp_ball] += 1;
	}

	for (auto get_ball : ball)
	{
		N = N - get_ball;
		result += get_ball * N;
	}

	std::cout << result << std::endl;
	return 0;
}

