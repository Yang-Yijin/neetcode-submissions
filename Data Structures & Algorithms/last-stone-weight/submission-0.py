import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)   
        while len(stones) > 1:
            firstbig = -heapq.heappop(stones)
            secbig = -heapq.heappop(stones)
            if firstbig != secbig:
                heapq.heappush(stones, -(firstbig - secbig))

        return -stones[0] if stones else 0