class TimeMap:

    def __init__(self):
        self.key_values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_values.keys():
            self.key_values[key].append((timestamp, value))
        else:
            self.key_values[key] = [(timestamp, value)]
        
    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.key_values) or (len(self.key_values[key]) == 0):
            return ""
        elif timestamp < self.key_values[key][0][0]:
            return ""
        else:
            l = 0
            r = len(self.key_values[key]) - 1
            while l<r:
                m = (l + r) // 2
                if self.key_values[key][m][0] == timestamp:
                    return self.key_values[key][m][1]
                elif self.key_values[key][m][0] > timestamp:
                    r = m -1
                elif self.key_values[key][m][0] < timestamp:
                    if (m+1 < len(self.key_values[key])) and (self.key_values[key][m+1][0] > timestamp):
                        return self.key_values[key][m][1]
                    else:
                        l = m + 1
            return self.key_values[key][l][1]
        
