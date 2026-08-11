class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(0, len(sorted_nums)):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]
            start = i+1
            end = len(sorted_nums) - 1
            while start < end:
                curr_sum = sorted_nums[start] + sorted_nums[end]
                if curr_sum == target:
                    result.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                    start += 1
                    end -= 1
                    while sorted_nums[start] == sorted_nums[start - 1] and start < end:
                        start += 1
                elif curr_sum > target:
                    end -= 1
                elif curr_sum < target:
                    start += 1
        return result