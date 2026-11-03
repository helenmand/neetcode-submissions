class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        pairs = sorted(counts.items(), key=lambda item: item[1], reverse=True)
        
        return [num for num, _ in pairs[:k]]