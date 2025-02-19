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
            

