/*
 * @lc app=leetcode.cn id=605 lang=c
 *
 * [605] 种花问题
 */

// @lc code=start
#include <stdbool.h>
bool canPlaceFlowers(int* flowerbed, int flowerbedSize, int n) {
    int count = 0;
    
    for(int i = 0; i < flowerbedSize; i++)
    {
        if (flowerbed[i] == 0)
        {
            bool left_ok = (i == 0) || (flowerbed[i - 1] == 0);
            bool right_ok = (i == flowerbedSize - 1) || (flowerbed[i + 1] == 0);

            if (left_ok && right_ok)
            {
                flowerbed[i] = 1;
                count++;
                if (count >= n)
                {
                    return 1;
                }
            }
        }
    }
    return count >= n;
}
// @lc code=end

