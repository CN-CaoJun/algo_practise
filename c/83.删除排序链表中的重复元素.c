/*
 * @lc app=leetcode.cn id=83 lang=c
 *
 * [83] 删除排序链表中的重复元素
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL)
    {
        return NULL;
    }

    struct ListNode * cur = head;
    
    while (cur->next != NULL)
    {
        if (cur->val == cur->next->val)
        {
            cur->next = cur->next->next;
        }
        else
        {
            cur = cur -> next;
        }
    }
    return head;    
}
// @lc code=end

