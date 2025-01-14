#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
from typing import List 
# 双指针
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        UNREPEAT_VALUE = 2
        slow = UNREPEAT_VALUE
        fast = UNREPEAT_VALUE
        
        while fast < len(nums):
            if nums[slow - UNREPEAT_VALUE] != nums[fast]:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast +1
            
        return slow
    
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3,3,3,3,3,3,5,5,5,5,5,5,5,5,5]
    s = Solution()
    new_length = s.removeDuplicates(nums)
    print(f"New length: {new_length}")
    print(f"Modified array: {nums[:new_length]}")
# @lc code=end

