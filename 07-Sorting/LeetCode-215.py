# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            pi = random.randint(l, r)
            nums[pi], nums[r] = nums[r], nums[pi]
            pivot = nums[r]
            p = lz
            for i in range(l, r):
                if nums[i] > pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k - 1:
                return quickSelect(l, p - 1)
            elif p < k - 1:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)
