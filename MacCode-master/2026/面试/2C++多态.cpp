#include <iostream>
using namespace std;

// 基类 Shape
class Shape
{
public:
    // 虚函数，支持多态
    virtual void draw() const
    { 
        cout << "Drawing a generic shape." << endl;
    }
    virtual ~Shape() {} // 虚析构函数，确保正确释放
};

// 派生类 Circle
class Circle : public Shape
{
public:
    void draw() const override
    { // 重写虚函数
        cout << "Drawing a circle." << endl;
    }
};

// 派生类 Rectangle
class Rectangle : public Shape
{
public:
    void draw() const override
    {
        cout << "Drawing a rectangle." << endl;
    }
};

// 通过基类引用展示多态的函数
void render(const Shape &s)
{
    s.draw(); // 运行时决定调用哪个 draw()
}

int main()
{
    Circle c;
    Rectangle r;

    // 使用基类指针指向派生类对象
    Shape *p1 = &c;
    Shape *p2 = &r;

    p1->draw(); // 输出: Drawing a circle.
    p2->draw(); // 输出: Drawing a rectangle.

    // 使用引用同样支持多态
    render(c); // 输出: Drawing a circle.
    render(r); // 输出: Drawing a rectangle.

    return 0;
}