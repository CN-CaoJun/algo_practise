#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicate_val = curr.val
                while curr and curr.val == duplicate_val:
                    curr = curr.next
                
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        
        return dummy.next
            
# @lc code=end

