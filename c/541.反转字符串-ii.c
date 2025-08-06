/*
 * @lc app=leetcode.cn id=541 lang=c
 *
 * [541] 反转字符串 II
 */

// @lc code=start
void reverse(char*s , int left, int right)
{
    while ( left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        right --;
        left ++ ;
    }
    
}
char* reverseStr(char* s, int k) {
    int len = strlen(s);
    
    for (int i = 0; i < len; i += 2 * k)
    {
        int end = (i+k-1 < len -1) ? (i + k - 1) : (len - 1);
        reverse(s, i, end);
    }
    return s;
}

