// 상하좌우.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

struct Point
{
	int y;
	int x;
};
const int MAX = 105;
int N;

Point user_pos = { 1,1 };

bool IsValid(Point pos)
{
	if (pos.x >= 1 && pos.y >= 1 && pos.x <= N && pos.y <= N)
		return true;
	else 
		return false;
}

void find_destination(std::string dir)
{
	if (dir == "R")
	{
		user_pos.y++;
		if (!IsValid(user_pos))
			user_pos.y--;
	}
	else if (dir == "L")
	{
		user_pos.y--;
		if (!IsValid(user_pos))
			user_pos.y++;
	}
	else if (dir == "U")
	{
		user_pos.x--;
		if (!IsValid(user_pos))
			user_pos.x++;
	}
	else if (dir == "D")
	{
		user_pos.x++;
		if (!IsValid(user_pos))
			user_pos.x--;
	}
}

int main()
{
	std::cin >> N;

	for (int i = 0; i < 6; ++i)
	{
		std::string dir_str;
		std::cin >> dir_str;
		find_destination(dir_str);
	}
	std::cout << user_pos.x << " " << user_pos.y << std::endl;
	return 0;
}

