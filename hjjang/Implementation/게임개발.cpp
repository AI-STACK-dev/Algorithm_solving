// 게임개발.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>

class Game
{
private:
	class pos
	{
	public:
		int y, x;
	};
	int mRow, mCol;
	int mDirection;
	int m_dy[4] = { -1,0,1,0 }, m_dx[4] = { 0,1,0,-1 };
	int mAnswer;
	std::vector<std::vector<int>> mMap;
	std::vector<std::vector<bool>>mCheck;
	
	bool CheckMap(int NextRow,int NextCol);
	void Turn90Degree();
public:
	pos Current_pos;
	Game(int row, int col,int direction);
	void setPos(int start_y, int start_x);
	pos getPos();
	void InputMap(int row,int col,int val);
	Game* move();
	int OutputAnswer();
};

Game::Game(int row, int col,int direction) : mRow(row), mCol(col), mAnswer(1),mDirection(direction)
{ 
	Current_pos.y = 0;
	Current_pos.x = 0;
	mMap.resize(mRow, std::vector<int>(mCol, 0));
	mCheck.resize(mRow, std::vector<bool>(mCol, false));
}

Game::pos Game::getPos()
{
	return Current_pos;
}

void Game::setPos(int start_y, int start_x)
{
	Game::Current_pos.y = start_y;
	Game::Current_pos.x = start_x;
}

void Game::InputMap(int row, int col,int val)
{
	mMap[row][col] = val;
}

void Game::Turn90Degree()
{
	mDirection -= 1;
	if (mDirection == -1)
		mDirection = 3;
}

bool Game::CheckMap(int NextRow, int NextCol)
{
	return mCheck[NextRow][NextCol] == 0 && mMap[NextRow][NextCol] != 1 ? true : false;
}
	
Game* Game::move()
{
	mCheck[Current_pos.y][Current_pos.x] = 1;
	int turnTime = 0;
	while (1)
	{
		Turn90Degree();
		Game::pos nextPos;
		nextPos.y = Current_pos.y + m_dy[mDirection];
		nextPos.x = Current_pos.x + m_dx[mDirection];
		if(CheckMap(nextPos.y,nextPos.x))
		{
			mCheck[nextPos.y][nextPos.x] = 1;
			Current_pos = nextPos;
			mAnswer++;
			turnTime = 0;
			continue;
		}
		else
		{
			turnTime++;
		}
		if (turnTime == 4)
		{
			nextPos.y = Current_pos.y - m_dy[mDirection];
			nextPos.x = Current_pos.x - m_dx[mDirection];
			if (mCheck[nextPos.y][nextPos.x] == 0)
				Current_pos = nextPos;
			else
				break;
		}
	}
	turnTime = 0;
	return this;
}

int Game::OutputAnswer()
{
	return mAnswer;
}

int main()
{
	int r, c;
	std::cin >> r >> c;

	int cur_y,cur_x, direction;
	std::cin >> cur_y >> cur_x >> direction;
	Game* game = new Game(r, c,direction);
	game->setPos(cur_y, cur_x);
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
		{
			int value;
			std::cin >> value;
			game->InputMap(i, j, value);
		}
	}

	std::cout << game->move()->OutputAnswer() << std::endl;
	return 0;
}

