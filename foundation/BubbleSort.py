# -*- coding: utf-8 -*-
def bubble_sort(nums):
    if nums == None or len(nums) == 1:
        return nums
    i = 0
    j = 0
    tmp = 0
    while i < len(nums) - 1:
        while j < len(nums) - i - 1:
            if (nums[j] > nums[j+1]):
                nums[j],nums[j+1] = nums[j+1],nums[j]
            j += 1
        i += 1
    return nums

nums = input('请输入数字，用逗号分隔：').split(',')
nums = bubble_sort(nums)
print(nums)