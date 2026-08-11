class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums) == 0:
            return 0
        minimum = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            minimum = min(nums[i], minimum)
            maximum = max(nums[i], maximum)

        longest_seq = 1
        current_seq = 1

        curr = minimum + 1
        while curr <= maximum:
            if curr in nums_set:
                current_seq += 1
            else:
                longest_seq = max(current_seq, longest_seq)
                current_seq = 0
            curr += 1
        return max(longest_seq, current_seq)
