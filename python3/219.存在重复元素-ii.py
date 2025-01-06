#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         index_map = {}
#         for i in range(len(nums)):
#             if nums[i] in index_map and i - index_map[nums[i]] <= k:
#                 return True
#             index_map[nums[i]] = i

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i in range(len(nums)):
            if nums[i] in index_map and i - index_map[nums[i]] <= k:
                return True
            index_map[nums[i]] = i
        return False
    
    """
    执行用时：56 ms, 在所有 Python3 提交中击败了99.09% 的用户
    内存消耗：15.9 MB, 在所有 Python3 提交中击败了5.02% 的用户
    """
# @lc code=end

