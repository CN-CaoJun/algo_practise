#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) !=  len(t):
            return False
        
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        return True

# @lc code=end
solution = Solution()

# 测试用例 1: 有效的字母异位词
s1 = "anagram"
t1 = "nagaram"
print(f"Test Case 1: {solution.isAnagram(s1, t1)}")  # 预期输出: True

# 测试用例 2: 无效的字母异位词
s2 = "rat"
t2 = "car"
print(f"Test Case 2: {solution.isAnagram(s2, t2)}")  # 预期输出: False

# 测试用例 3: 长度不同
s3 = "listen"
t3 = "silentt"
print(f"Test Case 3: {solution.isAnagram(s3, t3)}")  # 预期输出: False

s4 = ""
t4 = ""
print(f"Test Case 4: {solution.isAnagram(s4, t4)}")  # 预期输出: True