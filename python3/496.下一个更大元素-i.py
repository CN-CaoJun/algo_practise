#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

from typing import List

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        while stack:
            next_greater[stack.pop()] = -1
        
        result = []
        for num in nums1:
            result.append(next_greater[num])
        
        return result        
        

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

solution = Solution()
print(solution.nextGreaterElement(nums1, nums2))  # 输出: [-1, 3, -1]

        
# @lc code=end

