class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # result = []
        # for i in range(n):
        #     flag = 1
        #     for j in range(n):
        #         if i != j:
        #             flag *= nums[j]
        #     result.append(flag)

        # return result
        # 1  2  4  8
        # 1  1  2  8 
        # 64 32 8  1
        n = len(nums)
        pre = [1] * n
        suf = [1] * n
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        for j in range(n-2,-1,-1):
            suf[j] = suf[j+1] * nums[j+1]
        result = [1] * n
        for i in range(n):
            result[i] = pre[i] * suf[i]
        return result  