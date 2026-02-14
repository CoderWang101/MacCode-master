#include <iostream>

// 红黑树节点结构体
struct RBNode
{
    int key;        // 节点的键值
    int color;      // 节点的颜色（0表示黑色，1表示红色）
    RBNode *left;   // 左子节点
    RBNode *right;  // 右子节点
    RBNode *parent; // 父节点

    // 构造函数
    RBNode(int k, int c, RBNode *l = nullptr, RBNode *r = nullptr, RBNode *p = nullptr)
        : key(k), color(c), left(l), right(r), parent(p) {}
};

// 红黑树类
class RedBlackTree
{
private:
    RBNode *root; // 根节点
    RBNode *NIL;  // 空节点（叶子节点）

    // 左旋操作
    void leftRotate(RBNode *x)
    {
        RBNode *y = x->right; // y 是x的右子节点
        x->right = y->left;   // 将y的左子树作为x的右子树
        if (y->left != NIL)
            y->left->parent = x; // 更新y左子树的父节点为x
        
        y->parent = x->parent; // y的父节点设为x的父节点
        
        if (x->parent == NIL)// 如果x是根节点
            root = y; // 更新根节点为y
        else if (x == x->parent->left)
            x->parent->left = y; // x是左子节点，更新父节点的左子节点为y
        else
            x->parent->right = y; // x是右子节点，更新父节点的右子节点为y
        
        y->left = x;   // 将x作为y的左子节点
        x->parent = y; // 更新x的父节点为y
    }

    // 右旋操作
    void rightRotate(RBNode *x)
    {
        RBNode *y = x->left; // y 是x的左子节点
        x->left = y->right;  // 将y的右子树作为x的左子树
        if (y->right != NIL)
            y->right->parent = x; // 更新y右子树的父节点为x

        y->parent = x->parent; // y的父节点设为x的父节点

        if (x->parent == NIL)// 如果x是根节点
            root = y; // 更新根节点为y
        else if (x == x->parent->right)
            x->parent->right = y; // x是右子节点，更新父节点的右子节点为y
        else
            x->parent->left = y; // x是左子节点，更新父节点的左子节点为y

        y->right = x;  // 将x作为y的右子节点
        x->parent = y; // 更新x的父节点为y
    }

    // 插入后的修复操作
    void insertFixup(RBNode *z)
    {
        while (z->parent->color == 1)
        { // 父节点是红色
            if (z->parent == z->parent->parent->left)
            {                                         // 父节点是祖父节点的左子节点
                RBNode *y = z->parent->parent->right; // y是祖父节点的右子节点（叔叔节点）
                if (y->color == 1)
                {                                 // 叔叔节点是红色
                    z->parent->color = 0;         // 将父节点设为黑色
                    y->color = 0;                 // 将叔叔节点设为黑色
                    z->parent->parent->color = 1; // 将祖父节点设为红色
                    z = z->parent->parent;        // 继续向上调整
                }
                else
                { // 叔叔节点是黑色
                    if (z == z->parent->right)
                    {                  // z是右子节点
                        z = z->parent; // 将z移动到父节点
                        leftRotate(z); // 左旋
                    }
                    z->parent->color = 0;           // 将父节点设为黑色
                    z->parent->parent->color = 1;   // 将祖父节点设为红色
                    rightRotate(z->parent->parent); // 右旋
                }
            }
            else
            {                                        // 父节点是祖父节点的右子节点
                RBNode *y = z->parent->parent->left; // y是祖父节点的左子节点（叔叔节点）
                if (y->color == 1)
                {                                 // 叔叔节点是红色
                    z->parent->color = 0;         // 将父节点设为黑色
                    y->color = 0;                 // 将叔叔节点设为黑色
                    z->parent->parent->color = 1; // 将祖父节点设为红色
                    z = z->parent->parent;        // 继续向上调整
                }
                else
                { // 叔叔节点是黑色
                    if (z == z->parent->left)
                    {                   // z是左子节点
                        z = z->parent;  // 将z移动到父节点
                        rightRotate(z); // 右旋
                    }
                    z->parent->color = 0;          // 将父节点设为黑色
                    z->parent->parent->color = 1;  // 将祖父节点设为红色
                    leftRotate(z->parent->parent); // 左旋
                }
            }
        }
        root->color = 0; // 确保根节点是黑色
    }

public:
    // 构造函数
    RedBlackTree()
    {
        NIL = new RBNode(0, 0); // 创建空节点
        root = NIL;             // 初始化根节点为空
    }

    // 插入操作
    void insert(int key)
    {
        RBNode *z = new RBNode(key, 1, NIL, NIL, NIL); // 创建新节点，颜色为红色
        RBNode *y = NIL;                               // 用于追踪插入位置的父节点
        RBNode *x = root;                              // 从根节点开始查找插入位置

        // 查找插入位置
        while (x != NIL)
        {
            y = x; // 记录当前节点为父节点
            if (z->key < x->key)// 新节点的键值小于当前节点的键值
                x = x->left; // 移动到左子节点
            else
                x = x->right; // 移动到右子节点
        }

        // 插入新节点
        z->parent = y;
        if (y == NIL)// 树为空，z成为根节点
            root = z;
        else if (z->key < y->key)
            y->left = z;// 插入左子树
        else
            y->right = z;// 插入右子树

        insertFixup(z); // 调整树，使其满足红黑树性质
    }

    // 删除操作（简化实现，仅删除节点，不完全处理所有情况）
    void remove(int key)
    {
        RBNode *z = search(root, key); // 查找要删除的节点
        if (z == NIL)
            return; // 如果未找到，直接返回

        // 删除节点的逻辑（简化实现）
        // 实际实现中需要处理更多情况，例如：
        // 1. 节点是叶子节点
        // 2. 节点只有一个子节点
        // 3. 节点有两个子节点
        // 4. 删除后的颜色调整
        // 这里仅提供一个基本的删除框架，具体实现较为复杂
    }

    // 查找操作
    RBNode *search(RBNode *x, int key)
    {
        while (x != NIL && x->key != key)
        {
            if (key < x->key)
                x = x->left;
            else
                x = x->right;
        }
        return x;
    }

    // 获取根节点
    RBNode *getRoot()
    {
        return root;
    }
};

