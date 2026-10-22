class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n):
            flag = 1
            for j in range(n):
                if i != j:
                    flag *= nums[j]
            result.append(flag)

        return result