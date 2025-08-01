/*
 * @lc app=leetcode.cn id=61 lang=c
 *
 * [61] 旋转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* rotateRight(struct ListNode* head, int k) {
    
    //Move once first
    if (head == NULL || head->next == NULL || k == 0)
    {
        return head;
    }
    
    int length = 1;
    
    struct ListNode * tail = head;
    
    while (tail -> next != NULL)
    {
        tail = tail -> next;
        length ++;
    }

    k = k % length;

    if (k == 0)
        return head;


    //然后去找新的头节点

    struct ListNode *slow = head;
    struct ListNode *fast = head;

    for (int i = 0; i < k; i++)
    {
        fast = fast -> next;
    }

    while (fast->next !=NULL)
    {
        slow = slow -> next;
        fast = fast -> next;
    }

    struct ListNode *new_head = slow -> next;
    slow -> next = 0;
    tail -> next = head;

    return new_head;
    
    
}
// @lc code=end

