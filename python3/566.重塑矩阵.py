#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
from typing import List
# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m*n != r*c:
            return mat

        flat = []
        for i in range(m):
            for j in range(n):
                flat.append(mat[i][j])
        
        print("falt:",flat)
        
        flat_reshape = []
        flat_reshapex = []
        
        for i in range(r):
            for j in range(c):
                flat_reshapex.append(flat[i*c + j])
            flat_reshape.append(flat_reshapex)
            flat_reshapex = []
        return flat_reshape
    
if __name__ == '__main__':
    solution = Solution()
    
    mat = [[1, 2], [3, 4],[5,6]]
    r = 2
    c = 3
    print(solution.matrixReshape(mat, r, c))  # 输出: [[1, 2, 3, 4]]
    # @lc code=end  

