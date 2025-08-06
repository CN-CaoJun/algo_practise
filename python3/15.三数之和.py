#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            if nums[i] > 0:
                break
            
            left = i + 1
            right = n - 1 
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return ans
        
            
# @lc code=end

