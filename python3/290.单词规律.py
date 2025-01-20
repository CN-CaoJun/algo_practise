#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}  # 记录 pattern 中的字符到 s 中的单词的映射
        word_to_char = {}  # 记录 s 中的单词到 pattern 中的字符的映射
    
        for char, word in zip(pattern, words):
            # 检查字符到单词的映射是否一致
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # 检查单词到字符的映射是否一致
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        # 如果遍历完成后没有发现不匹配的情况，返回 True
        return True  
                
# @lc code=end

