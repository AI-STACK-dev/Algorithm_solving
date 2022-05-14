// 시각.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <string>
class Time
{
private:
    int m_hour;
    int m_minute;
    int m_second;
    int m_answer;
public:
    Time(int hour, int minute, int second) : m_hour(hour), m_minute(minute), m_second(second),m_answer(0)
    {};

    int Find_3_Counter()
    {
        for (int i = 0; i < m_hour + 1; ++i)
        {
            for (int j = 0; j < m_minute; ++j)
            {
                for (int k = 0; k < m_second; ++k)
                {
                    std::string time_str = std::to_string(i) + std::to_string(j) + std::to_string(k);
                    size_t npos = time_str.find("3");
                    if (npos != std::string::npos)
                    {
                        m_answer++;
                    }
                }
            }
        }
        return m_answer;
    }
    ~Time()
    {}
};

int main()
{
    int N;
    std::cin >> N;

    Time time(N, 60, 60);
    std::cout << time.Find_3_Counter() << std::endl;

    return 0;
}

