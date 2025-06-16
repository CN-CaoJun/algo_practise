#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, defaultdict(int)
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] += 1
            
        degree = max(count.values())
        min_len = float('inf')
        
        for num in count:
            if count[num] == degree:
                min_len = min(min_len, right[num]-left[num]+1)
        
        return min_len
# @lc code=end

