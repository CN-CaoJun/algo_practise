#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
from unittest import result


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) <4:
            return []

        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n-3):
                # 去重
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 最小和都大于target，后面不可能有解
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
                
            # 最大和都小于target，当前i不可能有解
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            # 固定第二个数
            for j in range(i+1, n-2):
                # 去重
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                # 最小和都大于target，后面不可能有解
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                    
                # 最大和都小于target，当前j不可能有解
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # 使用双指针寻找后两个数
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # 移动左指针并去重
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        # 移动右指针并去重
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result
# @lc code=end

