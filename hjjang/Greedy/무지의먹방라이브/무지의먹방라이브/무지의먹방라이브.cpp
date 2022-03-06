// 무지의먹방라이브.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//


#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <queue>


bool compare(std::pair<int, int> a, std::pair<int, int> b)
{
	return a.second < b.second; 
}


int solution(std::vector<int> food_times, long long k) 
{
	if (std::accumulate(food_times.begin(), food_times.end(), 0) <= k)
		return -1;

	std::priority_queue<std::pair<int, int>>  pq;

	for (int i = 0; i < food_times.size(); i++)
	{
		pq.push({ -food_times[i], i + 1 });
	}
	//최소힙을 위에 음수 설정 방법 

	
	/*
	while (!pq.empty())
	{
		std::cout << pq.top().first << ", " << pq.top().second << std::endl;
		pq.pop();
	}
	*/
	
	
	long long summary = 0; //먹기 위해 사용한시간
	long long previous = 0; //직전에 다먹은 음식시간
	long long length = food_times.size();

	while (summary + ((-pq.top().first - previous) * length) <= k)
	{
		int now = -pq.top().first;
		pq.pop();
		summary += (now - previous) * length;
		length -= 1;
		previous = now;
	}


	std::vector<std::pair<int, int>> result;
	while (!pq.empty())
	{
		int food_time = -pq.top().first;
		int num = pq.top().second;
		pq.pop();
		result.push_back({ food_time,num });
	}
	
	std::sort(result.begin(), result.end(), compare);
	return result[(k - summary) % length].second;
}


int main()
{
	std::cout << solution({ 8,6,4 }, 15) << std::endl;

	return 0;
}

