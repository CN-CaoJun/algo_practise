/*
 * @lc app=leetcode.cn id=11 lang=c
 *
 * [11] 盛最多水的容器
 */

// @lc code=start

#define MIN(a,b) ((b) < (a) ? (b) : (a) )
#define MAX(a,b) ((b) > (a) ? (b) : (a) )
int maxArea(int* height, int heightSize) {
    int ans = 0;
    int left = 0;
    int right = heightSize - 1;


    while (left < right)
    {
        int area = MIN(height[left],height[right]) * (right - left);
        ans = MAX(area,ans);

        height[left] < height[right]? left++ : right--;
    }

    return ans;    
}
// @lc code=end

