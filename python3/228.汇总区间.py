#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ranges.append(f"{start}" if start == end else f"{start}->{end}")
                start = end = nums[i]
        
        ranges.append(f"{start}" if start == end else f"{start}->{end}")  
        
        return ranges              
# @lc code=end

