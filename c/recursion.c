#include <stdio.h>

int forlooprecursion(int n)
{
    if (n == 0)
        return 0;
    else
        return n + forlooprecursion(n - 1);
}

int simulaterecursion(int n)
{
    int stack[1000] = {};
    int top = -1;
    int res = 0;
    
 // 将初始值 n 压入栈
    stack[++top] = n;

    for (; top >= 0; ) {
        int current = stack[top--];

        if (current == 0) {
            // 如果 current 为 0，不累加
            continue;
        } else {
            // 累加当前值
            res += current;
            // 将 current - 1 压入栈
            stack[++top] = current - 1;
        }
    }

    return res;
    
}

int main()
{
    int n  = 5;
    printf("Sum of first %d natural numbers using simulaterecursion: %d\n", n, simulaterecursion(n));
    printf("Sum of first %d natural numbers using recursion:         %d\n", n, forlooprecursion(n));
    return 0;
}