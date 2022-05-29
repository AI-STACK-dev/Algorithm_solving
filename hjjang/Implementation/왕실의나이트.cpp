// 왕실의나이트.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <vector>
#include <string>

class KindomOfNight
{
public:
    KindomOfNight(std::string);
    KindomOfNight* FIndAnswerCase();
    void  PrintAnswer();

private:
    std::vector<std::pair<int, int>> direction;
    int mRow;
    int mCol;
    int answer;
};

KindomOfNight::KindomOfNight(std::string position)
{
    direction = { {-2,-1},{-2,1},{2,-1},{2,1},{1,2},{-1,2},{1,-2}, {-1,-2} };
    mRow = position[0] - 'a' + 1;
    mCol = position[1] - '0';
}

KindomOfNight* KindomOfNight::FIndAnswerCase()
{
    for (size_t idx = 0; idx < 8; ++idx)
    {
        int nextRow = mRow + direction[idx].first;
        int nextCol = mCol + direction[idx].second;
        
        if (nextRow <= 8 && nextRow >= 1 && nextCol <= 8 && nextCol >= 1)
        {
            answer++;
        }
    }
    return this;
}
void KindomOfNight::PrintAnswer()
{ 
    std::cout << answer << std::endl;
}

int main()
{
    std::string pos;
    std::cin >> pos;

    KindomOfNight* kindomOfNight = new KindomOfNight(pos);
    kindomOfNight->FIndAnswerCase()->PrintAnswer();

    return 0;
}

