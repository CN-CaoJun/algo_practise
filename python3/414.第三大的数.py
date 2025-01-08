#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')
        
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            
            elif num > second and num != first:
                
                third = second
                second = num
            
            elif num> third and num != second and num != first :
                
                third = num 
        
        if third != float('-inf'):
            return third
        else:
            return first 
        

                
        
# @lc code=end

