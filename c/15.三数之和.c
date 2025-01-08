/*
 * @lc app=leetcode.cn id=15 lang=c
 *
 * [15] 三数之和
 */

// @lc code=start
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int cmp(const void* pa, const void* pb){
    int a=*(int*)pa;
    int b=*(int*)pb;
    return a>b?1:-1;
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    int base=100;//数组的初始长度，可更改
    //初始化处理返回值，二维数组的大小和保存每一个一维数组大小的数组的空间保持一致
    int** res=(int**)malloc(sizeof(int*)*base);
    *returnColumnSizes=(int*)malloc(sizeof(int)*base);
    *returnSize=0;
    int i,j,k;
    //排序
    qsort(nums,numsSize,sizeof(int),cmp);
    for(i=0;i<numsSize;i++){
        //先确定第三个数的值，再对剩下的两个数进行两数之和的操作
        //若本次的第三个数与上一次的情况相同，则跳过这个数
        if(i>0&&nums[i]==nums[i-1])
            continue;
        //给定nums[i]，以j，k作为双指针进行两数之和操作
        j=i+1;
        k=numsSize-1;
        while(j<k){
            int sum=nums[i]+nums[j]+nums[k];
            if(sum==0){//刚好遇见符合要求的三元组
                //申请返回值二维数组的空间
                res[*returnSize]=(int*)malloc(sizeof(int)*3);
                //每一个数组大小都为3
                (*returnColumnSizes)[*returnSize]=3;
                //给申请的空间赋值
                res[*returnSize][0]=nums[i];
                res[*returnSize][1]=nums[j];
                res[*returnSize][2]=nums[k];
                //二维数组的行数加1
                (*returnSize)++;
                //如果二维数组的大小达到初始设定的行数，则进行空间扩容
                if(*returnSize==base){
                    base*=2;
                    res=(int**)realloc(res,sizeof(int*)*base);
                    *returnColumnSizes=(int*)realloc(*returnColumnSizes,sizeof(int)*base);
                }
                //记录符合要求的两个数，进行去重
                int num1=nums[j],num2=nums[k];
                while(nums[j]==num1&&j<k)
                    j++;
                while(nums[k]==num2&&j<k)
                    k--;
            }
            //若三个数之和小于0，则左边的指针右移
            else if(sum<0)
                j++;
            //若三个数的之和大于0，则右边的指针往左移
            else k--;
        }
    }
    return res;
}

// 示例用法
// int main() {
//     int nums[] = {-1, 0, 1, 2, -1, -4};
//     int numsSize = sizeof(nums) / sizeof(nums[0]);
//     int returnSize;
//     int* returnColumnSizes;

//     int** result = threeSum(nums, numsSize, &returnSize, &returnColumnSizes);

//     printf("Result:\n");
//     for (int i = 0; i < returnSize; i++) {
//         printf("[%d, %d, %d]\n", result[i][0], result[i][1], result[i][2]);
//         free(result[i]);
//     }
//     free(result);
//     free(returnColumnSizes);

//     return 0;
// }
// @lc code=end

