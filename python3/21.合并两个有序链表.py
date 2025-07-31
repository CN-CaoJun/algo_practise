#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        head = list1
        
        while list1.next and list2:
            if list1.next.val <= list2.val:
                list1 = list1.next
            else:
                temp = list2.next
                list2.next = list1.next
                list1.next = list2
                list2 = temp
                list1 = list1.next
        
        if list2:
            list1.next = list2
        
        return head
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 测试用例
def run_tests():
    solution = Solution()
    
    print("=== 合并两个有序链表测试用例 ===")
    
    # 测试用例1：基本情况
    print("\n测试用例1: 基本合并")
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,4] 和 [1,3,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,2,3,4,4]")
    
    # 测试用例2：空链表
    print("\n测试用例2: 一个链表为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 [0]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [0]")
    
    # 测试用例3：两个空链表
    print("\n测试用例3: 两个链表都为空")
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [] 和 []")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: []")
    
    # 测试用例4：长度不同的链表
    print("\n测试用例4: 长度不同的链表")
    list1 = create_linked_list([1, 3, 5, 7, 9])
    list2 = create_linked_list([2, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,3,5,7,9] 和 [2,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,7,9]")
    
    # 测试用例5：所有元素相同
    print("\n测试用例5: 所有元素相同")
    list1 = create_linked_list([1, 1, 1])
    list2 = create_linked_list([1, 1, 1])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,1,1] 和 [1,1,1]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,1,1,1,1,1]")
    
    # 测试用例6：单个节点
    print("\n测试用例6: 单个节点")
    list1 = create_linked_list([5])
    list2 = create_linked_list([3])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [5] 和 [3]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [3,5]")
    
    # 测试用例7：负数
    print("\n测试用例7: 包含负数")
    list1 = create_linked_list([-3, -1, 2])
    list2 = create_linked_list([-2, 0, 4])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [-3,-1,2] 和 [-2,0,4]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [-3,-2,-1,0,2,4]")
    
    # 测试用例8：一个链表的所有元素都小于另一个
    print("\n测试用例8: 一个链表所有元素都小")
    list1 = create_linked_list([1, 2, 3])
    list2 = create_linked_list([4, 5, 6])
    result = solution.mergeTwoLists(list1, list2)
    print(f"输入: [1,2,3] 和 [4,5,6]")
    print(f"输出: {linked_list_to_array(result)}")
    print(f"预期: [1,2,3,4,5,6]")

# 运行测试
if __name__ == "__main__":
    run_tests()
# @lc code=end

# 辅助函数：创建链表
def create_linked_list(values):
    """根据数组创建链表"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# 辅助函数：链表转数组
def linked_list_to_array(head):
    """将链表转换为数组，便于比较结果"""
    result = []
    current = head

