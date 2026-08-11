class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i<=j:
            if nums[i] == val:
                if nums[j] == val:
                    j -= 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j -= 1
                    i += 1
            else:
                i += 1
        return i