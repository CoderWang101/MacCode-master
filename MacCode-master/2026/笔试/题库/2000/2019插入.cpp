// #include <iostream>
// using namespace std;

// struct Data
// {
//     int data;
//     Data *next;
// };

// int main()
// {
//     int n, m;
//     Data *head = new Data();

//     while (cin >> n >> m)
//     {
//         if (m == n == 0)
//             continue;

//         // 创建带头节点的链表
//         Data *head = new Data();
//         head->next = nullptr;
//         Data *tail = head;  // 尾指针，用于尾插法
        
//         // 构建初始链表
//         for (int i = 0; i < n; i++)
//         {
//             int val;
//             cin >> val;
//             Data *node = new Data();
//             node->data = val;
//             node->next = nullptr;
//             tail->next = node;
//             tail = node;
//         }

        
//         Data *p = head->next;
//         while (m < p->data)
//         {
//             p = p->next;
//         }
//         Data *newnode = new Data();
//         newnode->data = m;
//         newnode->next = p->next;
//         p->next = newnode;

//         cout << "插入后的链表为：" << endl;
//         Data *q = head->next;
//         while (q != nullptr)
//         {
//             cout << q->data << " ";
//             q = q->next;
//         }
//         cout << endl;
//     }

//     return 0;
// }
