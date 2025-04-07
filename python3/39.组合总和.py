#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                backtrack(i, target - candidates[i], path + [candidates[i]])
        
        res = []
        candidates.sort()
        backtrack(0, target,[])
        return res

# 测试用例
def test_combinationSum():
    solution = Solution()
    
    # 测试用例 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(solution.combinationSum(candidates1, target1))  # 输出: [[2, 2, 3], [7]]
    
    # 测试用例 2
    candidates2 = [2, 3, 5]
    target2 = 8
    print(solution.combinationSum(candidates2, target2))  # 输出: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    
    # 测试用例 3
    candidates3 = [2]
    target3 = 1
    print(solution.combinationSum(candidates3, target3))  # 输出: []
    
    # 测试用例 4
    candidates4 = [1]
    target4 = 2
    print(solution.combinationSum(candidates4, target4))  # 输出: [[1, 1]]
    
    # 测试用例 5
    candidates5 = [3, 4, 5]
    target5 = 8
    print(solution.combinationSum(candidates5, target5))  # 输出: [[3, 5]]

# 运行测试用例
test_combinationSum()
            
# @lc code=end

