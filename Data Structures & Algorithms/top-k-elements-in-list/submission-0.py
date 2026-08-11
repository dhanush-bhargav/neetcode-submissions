class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for i in range(len(nums)):
            if nums[i] in num_freq:
                num_freq[nums[i]] += 1
            else:
                num_freq[nums[i]] = 1
        num_freq_sorted = dict(sorted(num_freq.items(), key = lambda item: item[1]))
        
        return list(num_freq_sorted.keys())[-k:]
        