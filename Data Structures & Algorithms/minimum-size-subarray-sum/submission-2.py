class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sumation = 0
        result = 0
        
        for r in range(len(nums)):
            sumation += nums[r]
            while sumation >= target:
                if result==0:
                    result = (r-l+1)
                result = min(result, (r-l+1))
                sumation -= nums[l]
                l += 1
        return result


