class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j] == nums[i]:
                    return True
        return False