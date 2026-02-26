#include <iostream>
#include <deque>
#include <string>
using namespace std;
int range[51][51] = {0}; // 记录地图上的每个点是否被蛇身体覆盖
struct Snake
{
    int x;
    int y;
};

// 判断是否会撞到自己
bool isCrash(int x, int y)
{
    if (range[x][y] == 1)
        return true;
    return false;
}

// 判断是否会撞到边界
bool isCrashBoundary(int x, int y)
{
    if (x <= 0 || x >= 50 || y <= 0 || y >= 50)
        return true;
    return false;
}

/*
    true:会撞到边界或自己
    false:不会撞到边界或自己
    E:东/W:西/S:南/N:北
    E:右/W:左/S:下/N:上
 */

int main()
{
    Snake snake;
    snake.x = 25;
    snake.y = 30;

    // 双端队列
    deque<Snake> q; // 存储蛇的身体，队头为蛇头，队尾为蛇尾

    // 初始化蛇身体：长度为10，从头(25,30)向左延伸到 (25,21)
    for (int i = 0; i < 10; i++)
    {
        Snake seg{snake.x, snake.y - i};
        q.push_back(seg);
        range[seg.x][seg.y] = 1;
    }

    int n; // 步数
    string step;

    while (cin >> n && n != 0)
    {
        cin >> step;
        int flag = true; // 记录是否会撞到边界或自己
        // 开始游戏
        for (int i = 0; i < n; i++)
        {
            char dir = step[i];
            Snake head = q.front();
            int nx = head.x;
            int ny = head.y;
            
            // 计算下一步的位置
            if (dir == 'E')
                nx = head.x + 1;
            else if (dir == 'W')
                nx = head.x - 1;
            else if (dir == 'S')
                ny = head.y - 1;
            else if (dir == 'N')
                ny = head.y + 1;
            else
            {
                flag = false;
                break;
            }

            // 边界判断
            if (isCrashBoundary(nx, ny))
            {
                cout << "The worm ran into the boundary on move " << i << "." << endl;
                flag = false;
                break;
            }

            // 自身碰撞判断（允许移动到当前尾巴所在格，因为尾巴会移动）
            Snake tail = q.back();
            bool occupy = isCrash(nx, ny);
            if (occupy && !(nx == tail.x && ny == tail.y))// 撞到自己但不是尾巴
            {
                cout << "The worm ran into itself on move " << i << "." << endl;
                flag = false;
                break;
            }

            // 执行移动：头前进，尾巴收缩
            q.push_front({nx, ny});
            range[nx][ny] = 1;
            // 清理尾巴原位置
            range[tail.x][tail.y] = 0;
            q.pop_back();
        }
        if (flag)
            cout << "The worm successfully made all " << n << " moves." << endl;
    }

    return 0;
}
