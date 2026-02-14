#include <iostream>
#include <vector>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        if(head==nullptr||head->next==nullptr)
            return head;

        auto tmp=swapPairs(head->next->next);
        auto newHead=head->next;
        head->next->next=head;
        head->next=tmp;
        return newHead;
    }
};