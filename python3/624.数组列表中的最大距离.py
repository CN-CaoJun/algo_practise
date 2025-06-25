#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # 初始化最大距离为0
        # Initialize the maximum distance as 0
        max_dist = 0
        
        # 获取第一个数组的最小值和最大值
        # Get the minimum and maximum values from the first array
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        # 从第二个数组开始遍历
        # Start iterating from the second array
        for i in range(1, len(arrays)):
            # 当前数组的最小值和最大值
            # Minimum and maximum values of the current array
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            # 计算当前数组最大值与已知最小值的差
            # Calculate the difference between current array's maximum and known minimum
            dist1 = abs(curr_max - min_val)
            
            # 计算已知最大值与当前数组最小值的差
            # Calculate the difference between known maximum and current array's minimum
            dist2 = abs(max_val - curr_min)
            
            # 更新最大距离
            # Update the maximum distance
            max_dist = max(max_dist, dist1, dist2)
            
            # 更新全局最小值和最大值
            # Update the global minimum and maximum values
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return max_dist