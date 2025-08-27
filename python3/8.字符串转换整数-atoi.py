#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 -1
        INT_MIN = -2**31
        
        s = s.strip()
        
        if not s:
            return 0

        sign = 1
        index = 0
        
        if s[index] == '+':
            sign = 1
            index += 1
        elif s[index] == '-':
            sign = -1
            index += 1
        
        result = 0
        
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        result *= sign
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
        
        
# @lc code=end

