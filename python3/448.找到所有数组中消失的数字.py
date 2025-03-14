#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#
from typing import List
# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            
            if nums[index] > 0:
                nums[index] *= -1
                
        resule = []
        for i in range(len(nums)):
            if nums[i] > 0:
                resule.append(i + 1)
                
        return resule
        
# @lc code=end

nums = [4, 3, 2, 7, 8, 2, 3, 1]
solution = Solution()
print(solution.findDisappearedNumbers(nums))  # 输出: [5, 6]