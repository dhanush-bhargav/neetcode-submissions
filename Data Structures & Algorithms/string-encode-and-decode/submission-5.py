class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            n = len(s)
            result += str(n) + "#" + s
        return result
        

    def decode(self, s: str) -> List[str]:
        num_stack = ""
        result = []
        t = 0
        while t < len(s):
            if s[t].isnumeric():
                num_stack += s[t]
                t += 1
            elif s[t] == "#" and num_stack != "":
                str_len = int(num_stack)
                num_stack = ""
                result.append(s[t+1:t+str_len+1])
                t += (str_len+1)
        return result

        
