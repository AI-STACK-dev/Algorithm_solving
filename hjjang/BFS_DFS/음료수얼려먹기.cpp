// 음료수얼려먹기.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>

template<typename T>
class IceCreamMap
{
private:
	int mRow;
	int mCol;
	std::vector<std::vector<T>> map;
	std::vector<std::vector<bool>> check;
public:
	IceCreamMap(int N,int M) : mRow(N),mCol(M){ }
	void GenerateMap(std::vector<std::vector<T>>& refMap)
	{
		/*for (int rIdx = 0; refMap.size(); ++rIdx)
		{
			for (int cIdx = 0; refMap[rIdx].size(); ++cIdx)
			{
				map[rIdx][cIdx] = refMap[rIdx][cIdx];
			}
		}*/
		//위와동일 가독성있고 더효율적 
		map.clear();
		map.resize(mRow, std::vector<T>(mCol, 0));
		check.resize(mRow, std::vector<bool>(mCol, 0));
		std::copy(refMap.begin(), refMap.end(), map.begin());
	}
	
	std::vector<std::vector<bool>>& GetCheckMap()
	{
		return check;
	}

	//원래는 setter getter형식을 지키는게 맞음 
	int GetRow() { return mRow; }
	int GetCol() { return mCol; }

	std::vector<std::vector<T>>& GetMap()
	{
		return map;
	}
};

template<typename T>
class MapController
{
private:
	int answer;
	int dy[4] = { 1,-1,0,0 };
	int dx[4] = { 0,0,1,-1 };
	void DFS(int row,int col, IceCreamMap<T>& icecreamMap)
	{
		icecreamMap.GetCheckMap()[row][col] = true;
		icecreamMap.GetMap()[row][col] = 1;
		//이렇게 하는것보다 생성자를 통해 인자를 더 받는 구조가 좋았다.	
		for (int k = 0; k < 4; ++k)
		{
			int nextRow = row + dy[k];
			int nextCol = col + dx[k];

			if (nextRow >= 0 && nextRow < icecreamMap.GetRow() && nextCol >= 0 && nextCol < icecreamMap.GetCol() && icecreamMap.GetMap()[nextRow][nextCol] == 0 && icecreamMap.GetCheckMap()[nextRow][nextCol] == false )
			{
				DFS(nextRow, nextCol, icecreamMap);
			}
		}
	}
public:
	MapController()
	{ 
		answer = 0;
	}
	
	MapController* Find_IceCreamCount(IceCreamMap<T>& icecreamMap)
	{
		for (int i = 0; i < icecreamMap.GetMap().size(); ++i)
		{
			for (int j = 0; j < icecreamMap.GetMap()[i].size(); ++j)
			{
				if (icecreamMap.GetMap()[i][j] == 0)
				{
					answer++;
					DFS(i, j,icecreamMap);
					std::cout << std::endl;
					PrintMap(icecreamMap.GetMap());
				}
			}
		}
		return this;
	}
	
	void PrintAnswer()
	{ 
		std::cout << answer << std::endl; 
	}
	
	void PrintMap(std::vector<std::vector<T>>& map)
	{
		for (int rIdx = 0; rIdx < map.size(); ++rIdx)
		{
			for (int cIdx = 0; cIdx < map[rIdx].size(); ++cIdx)
			{
				std::cout << map.at(rIdx)[cIdx] << " ";
			}
			std::cout << std::endl;
		}
	}
};

int main()
{
	int N, M;
	std::cin >> N >> M;

	std::vector<std::vector<int>> clientMap;
	clientMap.resize(N, std::vector<int>(M, 0));

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < M; ++j)
		{
			int clientInput = 0;
			scanf("%1d", &clientInput);
			clientMap[i][j] = clientInput;
		}
	}

	IceCreamMap<int> client_IceCreamMap(N, M);
	client_IceCreamMap.GenerateMap(clientMap);

	MapController<int> mapController;
	mapController.PrintMap(client_IceCreamMap.GetMap());
	mapController.Find_IceCreamCount(client_IceCreamMap)->PrintAnswer();
	
	return EXIT_SUCCESS;
}

