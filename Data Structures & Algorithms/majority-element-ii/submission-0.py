class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
        result = []
        for key in counts:
            if counts[key] > (len(nums) // 3):
                result.append(key)
        return result