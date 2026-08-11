class Solution:
    def trap(self, height: List[int]) -> int:
        left_heights = [0] * len(height)
        right_heights = [0] * len(height)
        local_max = 0
        for i in range(len(height)):
            left_heights[i] = local_max
            if height[i] > local_max:
                local_max = height[i]
        local_max = 0
        for k in range(len(height)-1, -1, -1):
            right_heights[k] = local_max
            if height[k] > local_max:
                local_max = height[k]
        
        result = 0
        for t in range(len(height)):
            water = min(left_heights[t], right_heights[t]) - height[t]
            result = result + max(water, 0)
        return result