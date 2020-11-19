/* 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807 */

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* add = new ListNode(0);
        ListNode* node = add;
        int forward = 0;
        while (l1 != nullptr || l2 != nullptr)
        {
            int l1Val = l1 == nullptr ? 0 : l1->val;
            int l2Val = l2 == nullptr ? 0 : l2->val;
            int sum = l1Val + l2Val + forward;

            int num = sum >= 10 ? sum - 10 : sum;

            forward = sum >= 10 ? 1 : 0;

            node->next = new ListNode(num);
            node = node->next;
            if (forward == 1)
            {
                node->next = new ListNode(1);
            }
            l1 = l1 == nullptr ? nullptr : l1->next;
            l2 = l2 == nullptr ? nullptr : l2->next;
        }
        return add->next;
    }
};