class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        results = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sub_target = target - nums[i] - nums[j]
                l = j + 1
                r = len(nums) - 1
                while j < l < r < len(nums):
                    trial = nums[l] + nums[r]
                    if trial == sub_target:
                        if (nums[i], nums[j], nums[l], nums[r]) not in results:
                            results[(nums[i], nums[j], nums[l], nums[r])] = 1
                        l +=1
                        r -= 1
                    elif trial < sub_target:
                        l += 1
                    elif trial > sub_target:
                        r -= 1
                    
        return [list(r) for r in results.keys()]