class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        output = []
        for i in range(k):
            most_frequent = max(frequency, key=frequency.get)
            output.append(most_frequent)
            del frequency[most_frequent]
        
        return output
