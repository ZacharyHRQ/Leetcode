class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1