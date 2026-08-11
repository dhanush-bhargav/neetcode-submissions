class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_dict = {}
        for t in range(len(strs[0])):
            first_dict[t] = strs[0][t]
        result = ""
        k=0
        while k < len(strs[0]):
            add = True
            for i in range(1,len(strs)):
                if k >= len(strs[i]):
                    return result
                else:
                    if strs[i][k] != first_dict[k]:
                        add = False

            if add:
                result += first_dict[k]
            else:
                break
            k +=1
        return result