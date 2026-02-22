// KMP 字符串匹配算法实现
#include <vector>
#include <string>
/**
 * 计算部分匹配表（LPS，Longest Prefix Suffix）
 * 对于模式串 pattern，lps[i] 表示子串 pattern[0..i] 的最长相等真前缀与真后缀的长度
 * 该表用于在匹配失败时快速跳过已匹配的部分，避免重复比较
 *
 * @param pattern 模式串
 * @return 部分匹配表，长度为 pattern.size()
 */
std::vector<int> computeLPS(const std::string &pattern)
{
    int m = pattern.size();          // 模式串长度
    std::vector<int> lps(m, 0);      // 初始化 LPS 数组，默认全为 0
    int len = 0;                     // 当前最长公共前后缀长度，初始为 0
    int i = 1;                       // 从第二个字符开始计算 LPS 值

    // 遍历模式串，逐个计算 lps[i]
    while (i < m)
    {
        // 如果当前字符与最长前缀的下一个字符匹配，则扩展当前最长前后缀长度
        if (pattern[i] == pattern[len])
        {
            len++;
            lps[i] = len;  // 记录当前位置的最长前后缀长度
            i++;
        }
        else
        {
            // 如果不匹配且 len > 0，则回退到前一个最长前后缀的末尾继续尝试匹配
            if (len != 0)
                len = lps[len - 1];
            else
            {
                // 如果 len 已经为 0，说明没有更短的前后缀可尝试，当前 lps[i] 为 0
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

/**
 * KMP 搜索主函数：在文本 text 中查找模式 pattern
 * 利用预先计算好的 LPS 数组，在匹配失败时避免回溯文本指针，提高效率
 *
 * @param text    待搜索的文本
 * @param pattern 要查找的模式串
 * @return 若找到，返回 pattern 在 text 中首次出现的起始索引；否则返回 -1
 */
int kmpSearch(const std::string &text, const std::string &pattern)
{
    int n = text.size();    // 文本长度
    int m = pattern.size(); // 模式串长度

    // 空模式串视为在位置 0 匹配（根据实际需求可调整）
    if (m == 0)
        return 0;

    // 计算模式串的 LPS 数组
    std::vector<int> lps = computeLPS(pattern);

    int i = 0; // text 的当前比较位置指针
    int j = 0; // pattern 的当前比较位置指针

    // 遍历文本，进行匹配
    while (i < n)
    {
        // 当前字符匹配，则同时移动文本和模式指针
        if (text[i] == pattern[j])
        {
            i++;
            j++;
        }

        // 模式串完全匹配，返回匹配起始位置
        if (j == m)
        {
            return i - j; // 找到匹配，返回起始索引
        }
        // 当前字符不匹配，且模式指针未回到开头
        else if (i < n && text[i] != pattern[j])
        {
            if (j != 0)
            {
                // 利用 LPS 数组回退模式指针，避免重新比较已匹配部分
                j = lps[j - 1];
            }
            else
            {
                // 模式指针已在开头，文本指针后移一位
                i++;
            }
        }
    }

    // 遍历结束仍未找到匹配
    return -1;
}
