#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_map = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char] + 1)
                char_map[char] = right
            else:
                char_map[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len


                
        
# @lc code=end
