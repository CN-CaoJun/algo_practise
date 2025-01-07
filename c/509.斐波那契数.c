/*
 * @lc app=leetcode.cn id=509 lang=c
 *
 * [509] 斐波那契数
 */

// @lc code=start
int fib(int n) {
    // if (n <= 0) return 0; //这里是从第0位开始计算的
    // if (n == 1) return 1;
    // return fib(n - 1) + fib(n - 2);
    if(n == 0 || n == 1)
        return n;
    
    return fib(n - 1) + fib(n - 2);
}
// @lc code=end

