class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0:0, 1:0, 2:0}
        for num in nums:
            colors[num] += 1
        
        k = 0
        while k<colors[0]:
            nums[k] = 0
            k += 1
        while k<colors[0] + colors[1]:
            nums[k] = 1
            k +=1 
        while k<colors[0] + colors[1] + colors[2]:
            nums[k] = 2
            k += 1