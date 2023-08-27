# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, len(nums)):
            nums[i] = nums[i] * 1024 + nums[i-n]

        idx = 0
        for i in range(n, len(nums)):
            nums[idx] = nums[i] % 1024
            nums[idx + 1] = nums[i] // 1024
            idx += 2

        return nums    
