class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            char_key = [0] * 26
            for c in s:
                char_key[ord(c) - ord('a')] += 1
            result[tuple(char_key)].append(s)
        return list(result.values())