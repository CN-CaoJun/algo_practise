#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#
from typing import List
# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        results = []
        
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                results.append(words[i + 2])
        return results
    
solution = Solution()

# 测试用例 1
text1 = "alice is a good girl she is a good student"
first1 = "a"
second1 = "good"
print(f"Test Case 1: {solution.findOcurrences(text1, first1, second1)}")  # 预期输出: ["girl", "student"]
# @lc code=end

