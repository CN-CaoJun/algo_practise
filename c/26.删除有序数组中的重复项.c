/*
 * @lc app=leetcode.cn id=26 lang=c
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) {
        return 0;
    }
    
    int i = 0;
    
    for (int j = 0;  j < numsSize; j++)
    {
        if (nums[i] != nums[j])
        {
            i++;
            nums[i] = nums[j];
        }
    }

    return i+1;
}
// @lc code=end

