/*
 * @lc app=leetcode.cn id=24 lang=c
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// struct ListNode *createNode(int val){
    
// }
#include <stdio.h>
#include <stdlib.h>

// // 定义链表节点结构
// struct ListNode {
//     int val;
//     struct ListNode *next;
// };

// // 创建新节点
// struct ListNode* createNode(int val) {
//     struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
//     newNode->val = val;
//     newNode->next = NULL;
//     return newNode;
// }

// 交换相邻节点
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode dummy = {0, head};
    struct ListNode *node0 = &dummy;
    struct ListNode *node1 = head;
    
    while (node1 && node1->next)
    {
        struct ListNode* node2 = node1->next;
        struct ListNode* node3 = node2->next;
        
        node0 -> next =  node2;
        node2-> next = node1;
        node1 -> next = node3;

        node0 = node1;
        node1 = node1 -> next;
    }
    return dummy.next;

}

// 打印链表
// void printList(struct ListNode* head) {
//     while (head != NULL) {
//         printf("%d -> ", head->val);
//         head = head->next;
//     }
//     printf("NULL\n");
// }

// 主函数测试
// int main() {
//     // 创建链表 1 -> 2 -> 3 -> 4
//     struct ListNode* head = createNode(1);
//     head->next = createNode(2);
//     head->next->next = createNode(3);
//     head->next->next->next = createNode(4);
//     head->next->next->next->next = createNode(5);

//     printf("Original list: ");
//     printList(head);

//     // 交换相邻节点
//     head = swapPairs(head);

//     printf("Swapped list: ");
//     printList(head);

//     // 释放内存
//     while (head != NULL) {
//         struct ListNode* temp = head;
//         head = head->next;
//         free(temp);
//     }

//     return 0;
// }
// @lc code=end

