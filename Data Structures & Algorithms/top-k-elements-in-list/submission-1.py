class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            mp[num] = 1 + mp.get(num, 0)

        heap = []
        for num in mp.keys():
            heapq.heappush(heap, (mp[num], num))

        # Extract top k frequent elements
        return [num for freq, num in heapq.nlargest(k, heap)]