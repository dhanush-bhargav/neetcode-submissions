class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for element in nums:
            if element in num_set:
                return True
            else:
                num_set.add(element)
        return False
         