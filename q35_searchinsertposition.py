class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if target < nums[i]:
                return i
            elif nums[i] >= target:
                return i
            if i == len(nums) - 1 and target > nums[i]:
                return i + 1