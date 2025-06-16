#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                left_ok = (i == 0) or (flowerbed[i-1] == 0)
                right_ok = (i == length - 1) or (flowerbed[i+1] == 0)
                if left_ok and right_ok:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
# @lc code=end

