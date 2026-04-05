import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) - 1
        
        heap = []

        for val in count:
            heapq.heappush(heap, (count[val], val))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res