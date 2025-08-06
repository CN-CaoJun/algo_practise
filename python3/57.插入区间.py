#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        result = []
        i = 0
        n = len(intervals)
      
        # add all intervals that end before newInterval starts
        while i < n and intervals[i][1]  < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
    
        while i < n:
            result.append(intervals[i])
            i = i + 1
        
        return result
    
def test_insert_interval():
    solution = Solution()
    
    # Test Case 1: 基本合并情况 - 新区间与一个现有区间重叠
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    result1 = solution.insert(intervals1, newInterval1)
    print(f"测试1: {intervals1} + {newInterval1} = {result1}")
    print(f"预期结果: [[1,5],[6,9]]")
    print(f"测试通过: {result1 == [[1,5],[6,9]]}\n")
    
    # Test Case 2: 多重合并情况 - 新区间与多个现有区间重叠
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    result2 = solution.insert(intervals2, newInterval2)
    print(f"测试2: {intervals2} + {newInterval2} = {result2}")
    print(f"预期结果: [[1,2],[3,10],[12,16]]")
    print(f"测试通过: {result2 == [[1,2],[3,10],[12,16]]}\n")
    
    # Test Case 3: 无重叠插入 - 新区间插入到末尾
    intervals3 = [[1,2],[3,5]]
    newInterval3 = [6,8]
    result3 = solution.insert(intervals3, newInterval3)
    print(f"测试3: {intervals3} + {newInterval3} = {result3}")
    print(f"预期结果: [[1,2],[3,5],[6,8]]")
    print(f"测试通过: {result3 == [[1,2],[3,5],[6,8]]}\n")

# 运行测试
if __name__ == "__main__":
    test_insert_interval()
# @lc code=end

