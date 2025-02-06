#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) != len(s)

        diff = [(a,b) for a,b in zip(s,goal) if a != b]
                
        return len(diff) == 2 and diff[0] == diff[1][::-1]
# @lc code=end

