# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo, mid = 0, 0
        hi = len(nums) - 1
        while (mid <= hi):
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[hi] = nums[hi], nums[mid]
                hi -= 1
            else:
                mid += 1
