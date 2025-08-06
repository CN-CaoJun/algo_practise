#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        str = list(s)
        length = len(s)
        for i in range(0, length, 2*k):
            str[i:i+k] = str[i:i+k][::-1]
    
        return ''.join(str)

if __name__ == "__main__":
    solution = Solution()
    
    test1_s = "abcdefg"
    test1_k = 2
    result1 = solution.reverseStr(test1_s, test1_k)
    print(f"测试案例1: s='{test1_s}', k={test1_k} -> 结果: '{result1}' (期望: 'bacdfeg')")
    
    test2_s = "abcd"
    test2_k = 2
    result2 = solution.reverseStr(test2_s, test2_k)
    print(f"测试案例2: s='{test2_s}', k={test2_k} -> 结果: '{result2}' (期望: 'bacd')")
    
    test3_s = "abcdefgh"
    test3_k = 3
    result3 = solution.reverseStr(test3_s, test3_k)
    print(f"测试案例3: s='{test3_s}', k={test3_k} -> 结果: '{result3}' (期望: 'cbadefhg')")    
        
    
# @lc code=end

