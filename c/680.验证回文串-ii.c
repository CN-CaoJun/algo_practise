/*
 * @lc app=leetcode.cn id=680 lang=c
 *
 * [680] 验证回文串 II
 */

// @lc code=start
bool isPalindrome(char* s, int left, int right)
{
    while (left < right)
    {
        if (s[left] != s[right])
        {
            return false;
        }
        left++;
        right--; // Fixed: Should be decrementing right pointer
    }
    return true;    
}

bool validPalindrome(char* s) {
    int left = 0;
    int right = strlen(s) - 1;
    
    while (left < right) {
        if (s[left] != s[right]) {
            // When mismatch found, try skipping either left or right character
            return isPalindrome(s, left + 1, right) || isPalindrome(s, left, right - 1);
        }
        left++;
        right--;
    }
    // If we exit the loop without finding a mismatch, the string is a palindrome
    return true; 
}
