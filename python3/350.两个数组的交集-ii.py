#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        result = []
        
        for num in nums1:
            # count.get(num,0): Get value for key 'num', return 0 if key doesn't exist
            # Add 1 to create/update the count for this number
            count[num] = count.get(num,0) + 1
        
        for num in nums2:
            if num in count and count[num] > 0:  # 修复：先检查键是否存在
                result.append(num)
                count[num] -= 1
        
        return result
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    
    print("=== LeetCode 350. 两个数组的交集 II 测试用例 ===")
    
    # 测试用例1：标准情况
    print("\n测试用例1：标准情况")
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [2,2] (顺序可能不同)")
    
    # 测试用例2：部分交集，包含不存在的元素
    print("\n测试用例2：部分交集，包含不存在的元素")
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [9,4] (顺序可能不同)")
    
    # 测试用例3：无交集
    print("\n测试用例3：无交集")
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: []")
    
    # 测试用例4：空数组
    print("\n测试用例4：空数组")
    nums1 = []
    nums2 = [1,2,3]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: []")
    
    # 测试用例5：完全相同的数组
    print("\n测试用例5：完全相同的数组")
    nums1 = [1,2,3,4]
    nums2 = [1,2,3,4]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [1,2,3,4] (顺序可能不同)")
    
    # 测试用例6：一个数组是另一个的子集
    print("\n测试用例6：一个数组是另一个的子集")
    nums1 = [1,1,2,2,3,3]
    nums2 = [1,2,3]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [1,2,3] (顺序可能不同)")
    
    # 测试用例7：重复元素较多
    print("\n测试用例7：重复元素较多")
    nums1 = [1,1,1,2,2]
    nums2 = [1,1,2,2,2]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [1,1,2,2] (顺序可能不同)")
    
    # 测试用例8：单个元素
    print("\n测试用例8：单个元素")
    nums1 = [1]
    nums2 = [1]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [1]")
    
    # 测试用例9：大数组测试
    print("\n测试用例9：大数组测试")
    nums1 = [1,2,2,1,3,4,5,6,7,8,9,10]
    nums2 = [2,2,3,4,11,12,13]
    result = s.intersect(nums1, nums2)
    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"结果: {result}")
    print(f"期望: [2,2,3,4] (顺序可能不同)")
    
    print("\n=== 所有测试用例执行完毕 ===")

