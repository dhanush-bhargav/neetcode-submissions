class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left_boundaries = [-1] * len(heights)
        right_boundaries = [len(heights)] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_boundaries[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for j in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[j]:
                stack.pop()
            if stack:
                right_boundaries[j] = stack[-1]
            stack.append(j)
        
        max_area = 0
        print(left_boundaries)
        print(right_boundaries)
        for i in range(len(heights)):
            left_boundaries[i] += 1
            right_boundaries[i] -= 1
            max_area = max(max_area, heights[i] * (right_boundaries[i] - left_boundaries[i] + 1))
        return max_area

