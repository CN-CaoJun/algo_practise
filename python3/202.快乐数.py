#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
Calculate the sum of squares of digits for a given number.

This function is part of the solution for the 'Happy Number' problem (LeetCode 202).
It computes the next number in the sequence by summing the squares of each digit
of the input number.

Parameters:
    n (int): The input number to process.

Returns:
    int: The sum of squares of digits of the input number.

Local Variables:
    total_sum (int): Accumulates the sum of squared digits.
    digit (int): Stores each digit of the number during processing.

Notes:
    - This function is used in a loop to determine if a number is a 'happy number'.
    - A 'happy number' is defined as a number that eventually reaches 1 when replaced
      by the sum of the square of each digit.
    - The function uses divmod() for efficient digit extraction and division.
    - The time complexity is O(log n) as it processes each digit of the number.
    - The space complexity is O(1) as it uses a constant amount of extra space.
"""
        def get_next(n):
                    total_sum = 0
                    while n > 0:
                        n, digit = divmod(n, 10)
                        total_sum += digit ** 2
                    return total_sum
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1
    
# @lc code=end

