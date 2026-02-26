#include <iostream>
#include <vector>
#include <deque>
#include <cstdlib>
#include <ctime>
#include <string>
#include <unistd.h>
#include <sys/select.h>

using namespace std;

// 检查标准输入是否有数据可读
bool isStdinReady()
{
    fd_set readfds;
    FD_ZERO(&readfds);
    FD_SET(STDIN_FILENO, &readfds);

    struct timeval timeout;
    timeout.tv_sec = 0;
    timeout.tv_usec = 0;

    return select(STDIN_FILENO + 1, &readfds, nullptr, nullptr, &timeout) > 0;
}

// 方向枚举
enum Direction
{
    UP,
    DOWN,
    LEFT,
    RIGHT,
    NONE
};

// 坐标结构体
struct Point
{
    int x, y;
    bool operator==(const Point &other) const
    {
        return x == other.x && y == other.y;
    }
};

// 游戏状态枚举
enum GameState
{
    RUNNING,
    GAME_OVER,
    VICTORY
};

// 贪吃蛇后端逻辑类
class SnakeGameBackend
{
private:
    int width;
    int height;
    deque<Point> snake;
    Point food;
    Direction currentDir;
    GameState state;
    int score;

public:
    // 构造函数：初始化地图大小
    SnakeGameBackend(int w, int h) : width(w), height(h), state(RUNNING), score(0), currentDir(RIGHT)
    {
        // 初始化蛇的位置 (默认在地图中间)
        int startX = width / 2;
        int startY = height / 2;
        snake.push_back({startX, startY});     // 蛇头
        snake.push_back({startX - 1, startY}); // 蛇身
        snake.push_back({startX - 2, startY}); // 蛇尾

        srand(time(0));
        generateFood();
    }

    // 生成食物，确保不生成在蛇身上
    void generateFood()
    {
        bool onSnake = true;
        while (onSnake)
        {
            food.x = rand() % width;
            food.y = rand() % height;
            onSnake = false;
            for (const auto &bodyPart : snake)
            {
                if (bodyPart == food)
                {
                    onSnake = true;
                    break;
                }
            }
        }
    }

    // 处理输入方向
    void changeDirection(Direction newDir)
    {
        // 防止反向移动
        if ((currentDir == UP && newDir == DOWN) ||
            (currentDir == DOWN && newDir == UP) ||
            (currentDir == LEFT && newDir == RIGHT) ||
            (currentDir == RIGHT && newDir == LEFT))
        {
            return;
        }
        currentDir = newDir;
    }

    // 更新游戏状态（移动一步）
    void update()
    {
        if (state != RUNNING)
            return;

        Point newHead = snake.front();
        switch (currentDir)
        {
        case UP:
            newHead.y -= 1;
            break;
        case DOWN:
            newHead.y += 1;
            break;
        case LEFT:
            newHead.x -= 1;
            break;
        case RIGHT:
            newHead.x += 1;
            break;
        default:
            break;
        }

        // 1. 检查边界碰撞
        if (newHead.x < 0 || newHead.x >= width || newHead.y < 0 || newHead.y >= height)
        {
            state = GAME_OVER;
            return;
        }

        // 2. 检查自身碰撞 (注意：此时蛇尾还没移动，所以如果是追尾且没有吃到食物，尾巴会移走，不算碰撞。
        // 但简单起见，通常先判断是否撞到当前的身体。更精确的做法是先看是不是撞到除了尾巴以外的身体，或者如果吃到了食物尾巴不缩才看尾巴)
        // 这里采用简化逻辑：先判断是否撞到当前身体的任何部位（除了尾巴，因为尾巴即将移走，除非吃到食物）
        for (size_t i = 0; i < snake.size() - 1; ++i)
        { // 不检查尾巴
            if (snake[i] == newHead)
            {
                state = GAME_OVER;
                return;
            }
        }
        // 如果吃到食物，尾巴不缩，所以如果newHead撞到尾巴也是GameOver
        // 如果没吃到食物，尾巴缩回，所以newHead撞到尾巴不算GameOver
        // 这里的逻辑稍微复杂，为了严谨：
        bool eatsFood = (newHead == food);
        if (eatsFood)
        {
            // 检查是否撞到尾巴（因为尾巴不会动）
            if (snake.back() == newHead)
            {
                state = GAME_OVER;
                return;
            }
        }
        else
        {
            // 没吃到食物，尾巴会移走，所以只有当newHead撞到除了尾巴之外的身体时才算输
            // 上面的循环已经检查了 snake.size() - 1，即不包括尾巴
        }

        snake.push_front(newHead);

        if (eatsFood)
        {
            score += 10;
            generateFood();
        }
        else
        {
            snake.pop_back();
        }
    }

    // 获取游戏状态信息（用于API返回）
    void getGameState(int map[], int &w, int &h, int &currentScore, int &gameState) const
    {
        w = width;
        h = height;
        currentScore = score;
        gameState = state;

        if (map == nullptr) return; // 如果不需要获取地图数据，直接返回

        // 清空地图 (0: 空, 1: 蛇, 2: 食物)
        for (int i = 0; i < width * height; ++i)
            map[i] = 0;

        // 标记食物
        map[food.y * width + food.x] = 2;

        // 标记蛇
        for (const auto &p : snake)
        {
            map[p.y * width + p.x] = 1;
        }
    }

    // 打印地图（调试用）
    void printBoard()
    {
        for (int y = 0; y < height; ++y)
        {
            for (int x = 0; x < width; ++x)
            {
                bool isBody = false;
                for (const auto &p : snake)
                {
                    if (p.x == x && p.y == y)
                    {
                        cout << (p == snake.front() ? "H" : "O");
                        isBody = true;
                        break;
                    }
                }
                if (isBody)
                    continue;
                if (x == food.x && y == food.y)
                    cout << "F";
                else
                    cout << ".";
            }
            cout << endl;
        }
        cout << "Score: " << score << endl;
    }

    bool isGameOver() const { return state == GAME_OVER; }
};

// 模拟后端接口调用
int main()
{
    // 初始化游戏后端，地图 20x20
    SnakeGameBackend game(20, 20);

    // 模拟后端接口调用
    // 修改为适配 GUI 的协议模式
    // 输出协议：
    // 初始化：INIT <width> <height>
    // 每一帧：
    // FRAME_START
    // SCORE <score>
    // STATE <0:RUNNING, 1:GAME_OVER, 2:VICTORY>
    // MAP <01200...> (一行字符串，0空 1蛇 2食)
    // FRAME_END
    
    int width, height, score, gameState;
    game.getGameState(nullptr, width, height, score, gameState); // 仅获取宽高
    cout << "INIT " << width << " " << height << endl;
    cout.flush();

    char input;
    vector<int> mapData(width * height);

    while (true)
    {
        // 尝试读取输入（非阻塞），读取所有积压的输入，只取最后一个有效方向
        char lastInput = 0;
        
        while (isStdinReady() && read(STDIN_FILENO, &input, 1) > 0)
        {
            if (input == 'q')
                goto end_game;
            if (input == 'w' || input == 's' || input == 'a' || input == 'd')
            {
                lastInput = input;
            }
        }

        if (lastInput != 0)
        {
            Direction dir = NONE;
            switch (lastInput)
            {
            case 'w':
                dir = UP;
                break;
            case 's':
                dir = DOWN;
                break;
            case 'a':
                dir = LEFT;
                break;
            case 'd':
                dir = RIGHT;
                break;
            }
            if (dir != NONE)
            {
                game.changeDirection(dir);
            }
        }

        game.update();
        
        // 获取并输出状态
        game.getGameState(mapData.data(), width, height, score, gameState);
        
        cout << "FRAME_START" << endl;
        cout << "SCORE " << score << endl;
        cout << "STATE " << gameState << endl;
        cout << "MAP ";
        for (int val : mapData)
        {
            cout << val;
        }
        cout << endl;
        cout << "FRAME_END" << endl;
        cout.flush(); // 确保立即发送

        if (game.isGameOver())
        {
            // 游戏结束也发送一帧状态，然后保持或退出？
            // 这里选择继续循环发送结束状态，直到用户按q退出，或者由前端决定
             usleep(100000); // 降低刷新率
             // break; // 如果想后端自动退出
        }
        
        // 控制游戏速度 (例如 100ms 一帧，稍微快一点让前端感觉流畅)
        usleep(100000);
    }
    
end_game:
    return 0;
}
