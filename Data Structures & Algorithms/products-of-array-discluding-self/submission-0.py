class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_products = [0] * len(nums)
        backward_products = [0] * len(nums)
        running_prod = 1
        for i in range(len(nums)):
            forward_products[i] = running_prod
            running_prod *= nums[i]
        running_prod = 1
        for k in range(len(nums)-1, -1, -1):
            backward_products[k] = running_prod
            running_prod *= nums[k]
        result = [0] * len(nums)
        for t in range(len(nums)):
            result[t] = forward_products[t] * backward_products[t]
        return result