#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
from typing import List 
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        current_len = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current_len = current_len + 1
            else:
                current_len = 1

            max_len = max(max_len, current_len)
            
        return max_len
            

def test_findLengthOfLCIS():
    solution = Solution()
    # 测试用例 1: 普通递增序列
    nums1 = [1, 3, 5, 4, 7]
    assert solution.findLengthOfLCIS(nums1) == 3, "Test case 1 failed"
    
    # 测试用例 2: 完全递增序列
    nums2 = [1, 2, 3, 4, 5]
    assert solution.findLengthOfLCIS(nums2) == 5, "Test case 2 failed"
    
    # 测试用例 3: 完全递减序列
    nums3 = [5, 4, 3, 2, 1]
    assert solution.findLengthOfLCIS(nums3) == 1, "Test case 3 failed"
    
    # 测试用例 4: 空数组
    nums4 = []
    assert solution.findLengthOfLCIS(nums4) == 0, "Test case 4 failed"
    
    # 测试用例 5: 单个元素
    nums5 = [2]
    assert solution.findLengthOfLCIS(nums5) == 1, "Test case 5 failed"
    
    # 测试用例 6: 包含重复元素的递增序列
    nums6 = [1, 3, 5, 5, 7]
    assert solution.findLengthOfLCIS(nums6) == 3, "Test case 6 failed"
    
    print("All test cases passed!")

test_findLengthOfLCIS()