// Basic_BFS.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <queue>

class MyGraph
{
private:
	std::vector<bool>mVisited;
	std::vector<std::vector<int>> mGraph;
public:
	void setGraph(int a, int b);
	std::vector<std::vector<int>> getGraph();
	std::vector<bool> getVisited();
	MyGraph(int size);
	void BFS(int vertex);
};

MyGraph::MyGraph(int size)
{
	mVisited.resize(size + 1, false);
	mGraph.resize(size + 1, std::vector<int>());
}

void MyGraph::setGraph(int a, int b)
{
	mGraph[a].emplace_back(b);
	mGraph[b].emplace_back(a);
}

std::vector<std::vector<int>> MyGraph::getGraph()
{
	return mGraph;
}

std::vector<bool> MyGraph::getVisited()
{
	return mVisited;
}

void MyGraph::BFS(int vertex)
{
	std::queue<int> Queue;
	mVisited[vertex] = true;
	Queue.push(vertex);
	
	while (!Queue.empty())
	{
		int cur = Queue.front();
		std::cout << cur << " ";
		Queue.pop();
		for (size_t j = 0; j < mGraph[cur].size(); ++j)
		{
			if (!mVisited[mGraph[cur][j]])
			{
				Queue.push(mGraph[cur][j]);
				mVisited[mGraph[cur][j]] = true;
			}
		}
	}
	std::cout << std::endl;
}

int main()
{
	int size;
	std::cin >> size;
	MyGraph* myGraph = new MyGraph(size);

	for (int i = 0; i < 9; ++i)
	{
		int a, b;
		std::cin >> a >> b;
		myGraph->setGraph(a, b);
	}

	for (size_t idx = 0; idx < myGraph->getGraph().size(); ++idx)
	{
		for (size_t i = 0; i < myGraph->getGraph()[idx].size(); ++i)
		{
			std::cout << myGraph->getGraph()[idx][i] << " ";
		}
		std::cout << std::endl;
	}

	myGraph->BFS(1);
	return 0;
}
