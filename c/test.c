#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>
#include <limits.h>

#define BASE_INCREMENT 10000000  // 基础增量
#define VARIATION_PERCENT 2     // 波动百分比
#define MAX_INTERVALS 5         // 记录最长和最短时间间隔的数量

// 全局变量
uint32_t last_time = 0;                     // 上一次的时间值
uint32_t longest_intervals[MAX_INTERVALS];  // 最长的 5 个时间间隔
uint32_t shortest_intervals[MAX_INTERVALS]; // 最短的 5 个时间间隔

// 初始化最长和最短时间间隔数组
void initialize_intervals() {
    for (int i = 0; i < MAX_INTERVALS; i++) {
        longest_intervals[i] = 0;                // 初始化为 0
        shortest_intervals[i] = UINT32_MAX;      // 初始化为最大值
    }
}

// 模拟时间函数（支持溢出处理）
uint32_t get_next_time() {
    // 计算波动范围（±2%）
    uint32_t variation = (BASE_INCREMENT * VARIATION_PERCENT) / 100;
    uint32_t random_variation = rand() % (2 * variation) - variation;

    // 计算新的时间值
    uint32_t next_time = last_time + BASE_INCREMENT + random_variation;

    // 更新上一次的时间值
    last_time = next_time;

    return next_time;
}

// 计算时间间隔（支持溢出处理）
uint32_t calculate_interval(uint32_t current_time, uint32_t last_time) {
    if (current_time >= last_time) {
        // 没有溢出，直接计算间隔
        return current_time - last_time;
    } else {
        // 发生溢出，计算回绕后的间隔
        printf("Exceed!!!!\r\n");
        return (UINT32_MAX - last_time) + current_time + 1;
    }
}

// 更新最长和最短时间间隔数组
void update_intervals(uint32_t interval) {
    // 更新最长间隔数组
    for (int i = 0; i < MAX_INTERVALS; i++) {
        if (interval > longest_intervals[i]) {
            for (int j = MAX_INTERVALS - 1; j > i; j--) {
                longest_intervals[j] = longest_intervals[j - 1];
            }
            longest_intervals[i] = interval;
            break;
        }
    }

    // 更新最短间隔数组
    for (int i = 0; i < MAX_INTERVALS; i++) {
        if (interval < shortest_intervals[i]) {
            for (int j = MAX_INTERVALS - 1; j > i; j--) {
                shortest_intervals[j] = shortest_intervals[j - 1];
            }
            shortest_intervals[i] = interval;
            break;
        }
    }
}

// 回调函数：处理时间值的变化
void time_callback(uint32_t current_time) {
    static uint32_t last_callback_time = 0; // 上一次回调的时间值

    if (last_callback_time != 0) {
        // 计算时间间隔（支持溢出处理）
        uint32_t interval = calculate_interval(current_time, last_callback_time);
        printf("Current time: %u, Interval: %u\n", current_time, interval);

        // 更新最长和最短时间间隔数组
        update_intervals(interval);
    }

    // 更新上一次回调的时间值
    last_callback_time = current_time;
}

// 打印最长和最短时间间隔
void print_intervals() {
    printf("Longest intervals: ");
    for (int i = 0; i < MAX_INTERVALS; i++) {
        printf("%u ", longest_intervals[i]);
    }
    printf("\n");

    printf("Shortest intervals: ");
    for (int i = 0; i < MAX_INTERVALS; i++) {
        printf("%u ", shortest_intervals[i]);
    }
    printf("\n");
}

int main() {
    srand(time(NULL)); // 初始化随机数种子
    initialize_intervals(); // 初始化最长和最短时间间隔数组

    // 模拟调用时间函数和回调函数
    for (int i = 0; i < 450; i++) {
        uint32_t current_time = get_next_time(); // 获取下一个时间值
        time_callback(current_time);            // 调用回调函数
    }

    // 打印最终的最长和最短时间间隔
    print_intervals();

    return 0;
}