#include <unordered_map>
#include <vector>
using namespace std;
class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {

        int a = -1, b = -1;     // 两个果篮
        int vala = 0, valb = 0; // 果篮中果实数量
        int left = -1, right = 0, len = 0;

        for (right; right < fruits.size(); right++)
        {
            // 符合种类
            if (fruits[right] == b)
                ++valb;
            else if (fruits[right] == a)
                ++vala;
            else // 出现不相同种类
            {
                // 遇到新种类，且篮子有空位
                if (a == -1)
                {
                    a = fruits[right];
                    vala = 1;
                }
                else if (b == -1)
                {
                    b = fruits[right];
                    valb = 1;
                }
                else // 遇到新种类，且篮子满
                {
                }
            }
        }
        return len;
    }
};

class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {
        int a = -1, b = -1;     // 两个果篮
        int vala = 0, valb = 0; // 果篮中果实数量
        int left = 0, right = 0, maxLen = 0;
        int n = fruits.size();

        while (right < n)
        {
            // 符合当前种类
            if (fruits[right] == a)
                ++vala;
            else if (fruits[right] == b)
                ++valb;
            else
            {
                // 遇到新种类，且篮子有空位
                if (a == -1)
                {
                    a = fruits[right];
                    vala = 1;
                }
                else if (b == -1)
                {
                    b = fruits[right];
                    valb = 1;
                }
                else
                {
                    // 篮子已满，需要移动左指针
                    maxLen = max(maxLen, vala + valb);

                    // 移动左指针，直到一个篮子为空
                    while (left < right && vala > 0 && valb > 0)
                    {
                        if (fruits[left] == a)
                            --vala;
                        else if (fruits[left] == b)
                            --valb;
                        ++left;
                    }

                    // 重置空篮子(将新种类放入空篮子)
                    if (vala == 0)
                    {
                        a = fruits[right];
                        vala = 1;
                    }
                    else
                    {
                        b = fruits[right];
                        valb = 1;
                    }
                }
            }

            ++right;
        }

        // 最后还要更新一次最大长度
        maxLen = max(maxLen, vala + valb);

        return maxLen;
    }
};
// 优化版 哈希表

class Solution
{
public:
    int totalFruit(vector<int> &fruits)
    {
        unordered_map<int, int> basket; // 水果种类 -> 数量
        int left = 0, maxFruits = 0;

        for (int right = 0; right < fruits.size(); ++right)
        {
            basket[fruits[right]]++;

            // 如果篮子里的水果种类超过2种，移动左指针
            while (basket.size() > 2)
            {
                basket[fruits[left]]--;
                if (basket[fruits[left]] == 0)
                    basket.erase(fruits[left]);
                left++;
            }

            maxFruits = max(maxFruits, right - left + 1);
        }

        return maxFruits;
    }
};