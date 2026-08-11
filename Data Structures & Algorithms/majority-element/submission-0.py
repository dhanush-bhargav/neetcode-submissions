class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_counts = {}
        for el in nums:
            if el in element_counts.keys():
                element_counts[el] += 1
            else:
                element_counts[el] = 1
        
        for key in element_counts:
            if element_counts[key] >= len(nums) // 2:
                return key
        