# 912. Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merging(nums: List[int], lo: int, mid: int, hi: int):
            L = nums[lo: mid + 1]
            R = nums[mid + 1: hi + 1]

            i = j = 0
            idx = lo

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[idx] = L[i]
                    i += 1
                else:
                    nums[idx] = R[j]
                    j += 1
                idx += 1

            while i < len(L):
                nums[idx] = L[i]
                i += 1   
                idx += 1

            while j < len(R):
                nums[idx] = R[j]
                j += 1
                idx += 1

        def mergeSort(nums: List[int], lo: int, hi: int):
            if lo < hi:
                mid = (lo + hi) // 2
                mergeSort(nums, lo, mid)
                mergeSort(nums, mid + 1, hi)
                merging(nums, lo, mid, hi)
            return nums

        return mergeSort(nums, 0, len(nums)-1)
