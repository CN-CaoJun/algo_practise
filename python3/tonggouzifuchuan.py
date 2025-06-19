#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool: 
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s
            
        return True
        
# @lc code=end

# Test cases
def run_tests():
    solution = Solution()
    
    # Test case 1: Basic isomorphic strings
    test1_s = "egg"
    test1_t = "add"
    print(f"Test case 1: s = {test1_s}, t = {test1_t}")
    print(f"Result: {solution.isIsomorphic(test1_s, test1_t)}")
    print(f"Expected: True\n")
    
    # Test case 2: Non-isomorphic strings - different chars mapping to same char
    test2_s = "foo"
    test2_t = "bar"
    print(f"Test case 2: s = {test2_s}, t = {test2_t}")
    print(f"Result: {solution.isIsomorphic(test2_s, test2_t)}")
    print(f"Expected: False\n")
    
    # Test case 3: Non-isomorphic strings - same char mapping to different chars
    test3_s = "badc"
    test3_t = "baba"
    print(f"Test case 3: s = {test3_s}, t = {test3_t}")
    print(f"Result: {solution.isIsomorphic(test3_s, test3_t)}")
    print(f"Expected: False\n")
    
    # Test case 4: Empty strings
    test4_s = ""
    test4_t = ""
    print(f"Test case 4: s = {test4_s}, t = {test4_t}")
    print(f"Result: {solution.isIsomorphic(test4_s, test4_t)}")
    print(f"Expected: True\n")
    
    # Test case 5: Strings with different lengths
    test5_s = "ab"
    test5_t = "abc"
    print(f"Test case 5: s = {test5_s}, t = {test5_t}")
    print(f"Result: {solution.isIsomorphic(test5_s, test5_t)}")
    print(f"Expected: False\n")
    
    # Test case 6: Complex isomorphic strings
    test6_s = "paper"
    test6_t = "title"
    print(f"Test case 6: s = {test6_s}, t = {test6_t}")
    print(f"Result: {solution.isIsomorphic(test6_s, test6_t)}")
    print(f"Expected: True\n")

# Execute tests when this file is run directly
if __name__ == "__main__":
    run_tests()