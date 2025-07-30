/*
 * @lc app=leetcode.cn id=1071 lang=c
 *
 * [1071] 字符串的最大公因子
 */

// @lc code=start
int gcd(int a, int b)
{
    while(b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
char* gcdOfStrings(char* str1, char* str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);

    char * temp1 = (char*)malloc((len1 + len2 + 1) * sizeof(char));
    char * temp2 = (char*)malloc((len1 + len2 + 1) * sizeof(char));
    strcpy(temp1, str1);
    strcat(temp1, str2);
    
    strcpy(temp2, str2);
    strcat(temp2, str1);
    
    // 如果 str1 + str2 != str2 + str1，则没有公共因子
    if (strcmp(temp1, temp2) != 0) {
        free(temp1);
        free(temp2);
        char* result = (char*)malloc(1 * sizeof(char));
        result[0] = '\0';
        return result;
    }
    
    free(temp1);
    free(temp2);
    
    // 计算最大公约数
    int gcd_len = gcd(len1, len2);
    
    // 创建结果字符串
    char* result = (char*)malloc((gcd_len + 1) * sizeof(char));
    strncpy(result, str1, gcd_len);
    result[gcd_len] = '\0';
    
    return result;

}
// @lc code=end

