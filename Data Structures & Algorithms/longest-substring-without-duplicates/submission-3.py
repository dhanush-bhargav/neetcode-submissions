class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        character_set = set()
        l = 0
        r = 0
        max_len = 0

        while r < len(s):
            if s[r] not in character_set:
                character_set.add(s[r])
                r += 1
            else:
                max_len = max(max_len, len(character_set))
                while (l<r) and (s[r] in character_set):
                    character_set.remove(s[l])
                    l += 1
        return max(max_len, len(character_set))
