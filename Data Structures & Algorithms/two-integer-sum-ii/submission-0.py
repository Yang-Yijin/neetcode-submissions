class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n < 2:
            return False
        l = 0
        r = n - 1
        while l < r:
            flag = numbers[l] + numbers[r]
            if flag > target:
                r -= 1
            elif flag < target:
                l += 1
            else:
                return [l+1,r+1]
        