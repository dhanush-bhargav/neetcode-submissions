class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            char_dict = {}
            for i in range(len(s)):
                if s[i] in char_dict.keys():
                    char_dict[s[i]] += 1
                else:
                    char_dict[s[i]] = 1
            for j in range(len(s)):
                if t[j] in char_dict.keys():
                    char_dict[t[j]] -= 1
                    if char_dict[t[j]] == 0:
                        char_dict.pop(t[j])
                else:
                    return False
            if len(char_dict) == 0:
                return True