class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_stack = []
        days = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(temperature_stack) == 0:
                temperature_stack.append((temperatures[i], i))
            else:
                while (len(temperature_stack) > 0) and (temperatures[i] > temperature_stack[-1][0]):
                    temp = temperature_stack.pop(-1)
                    days[temp[1]] = i - temp[1]
                temperature_stack.append((temperatures[i], i))
        return days