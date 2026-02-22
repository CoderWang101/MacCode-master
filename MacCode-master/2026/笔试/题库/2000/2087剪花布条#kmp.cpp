#include <iostream> // 标准输入输出
#include <iomanip>  // 保留小数等格式控制（本题不使用，但保留）
#include <string>   // 字符串类型
#include <vector>   // 动态数组，用于存储前缀函数
using namespace std;
namespace kmp
{ /**
   * @brief 计算模式串的 LPS（最长前后缀）数组
   *
   * KMP 的核心是利用模式串自身结构，避免在匹配失败时回退主串指针。
   * LPS[i] 表示 pattern[0..i] 的最长“既是前缀又是后缀”的长度。
   * 在匹配中，当 pattern[j] 与 text[i] 不等时，令 j = LPS[j-1] 继续比较。
   *
   * @param pattern 模式串
   * @return vector<int> LPS 数组
   */
    vector<int> patterns(string pattern)
    {
        int m = pattern.size();     // 模式串长度
        vector<int> pm(m, 0);       // 前缀函数（LPS）数组，初始为 0
        int j = 0;                  // 当前“有效前后缀”长度
        for (int i = 1; i < m; i++) // 从下标 1 开始构造 LPS
        {
            // 回退 j：直到能匹配或 j 归零
            while (j > 0 && pattern[i] != pattern[j])
                j = pm[j - 1];
            // 若当前字符匹配，扩展有效前后缀长度
            if (pattern[i] == pattern[j])
                j++;
            pm[i] = j; // 记录当前位置的 LPS 值
        }
        return pm;
    }
    int main()
    {
        string text, pattern;
        // 输入格式：每组两行，第一行是布条 text；第二行是花样 pattern；text 为 "#" 表示结束
        while (cin >> text)
        {
            if (text == "#") // 终止条件
                break;
            if (!(cin >> pattern)) // 读取失败则退出
                break;
            vector<int> pm = patterns(pattern); // 预处理模式串的 LPS
            int n = (int)text.size(), m = (int)pattern.size();
            int j = 0;     // 模式串当前匹配到的位置
            int count = 0; // 非重叠匹配的次数
            // 扫描主串
            for (int i = 0; i < n; i++)
            {
                // 若当前字符不匹配，按照 LPS 回退 j
                while (j > 0 && text[i] != pattern[j])
                    j = pm[j - 1];
                // 当前字符匹配，推进 j
                if (text[i] == pattern[j])
                    j++;
                // 完成一次匹配：统计一次并重置 j=0 保证“非重叠”
                if (j == m)
                {
                    count++;
                    j = 0; // 非重叠匹配的关键：从头重新匹配下一段
                }
            }
            cout << count << "\n"; // 输出当前组的匹配次数
        }
        return 0;
    }
}