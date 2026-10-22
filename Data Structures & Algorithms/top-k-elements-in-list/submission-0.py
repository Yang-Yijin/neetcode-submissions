class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = {}
        for x in nums:
            if x not in n:
                n[x] = 1
            else:
                n[x] += 1
        dict_sort = sorted(n.items(), key=lambda x: x[1])
        last_two = dict_sort[-k:]
        keys = [k for k, v in last_two]
        return keys