#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head and head.next:
            # 初始化要交换的两个节点
            first = head
            second = head.next
            
            # 交换节点
            prev.next = second
            first.next = second.next
            second.next = first
            
            # 更新指针
            prev = first
            head = first.next
        
        return dummy.next
    
def printList(node: ListNode):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

if __name__ == "__main__":
    # 创建一个测试链表 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    
    print("Original list:")
    printList(head)
    
    # 创建 Solution 类的实例
    solution = Solution()
    
    # 调用 swapPairs 函数
    new_head = solution.swapPairs(head)
    
    print("List after swapping pairs:")
    printList(new_head)
# @lc code=end

