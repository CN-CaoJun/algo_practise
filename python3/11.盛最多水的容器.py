#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

# 1. 向内移动短板
# 2. 使用双指针
        i = 0
        j = len(height) - 1
        res = 0
    
        while i < j :

            res = max(res, min(height[i], height[j]) * (j - i))
            
            i += 1 if height[i] < height[j] else j -= 1
            
        return res
    
# @lc code=end

