class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_counts = {}
        l = 0
        r = 0
        result = 0
        maxf = 0

        for r in range(len(s)):
            character_counts[s[r]] = character_counts.get(s[r], 0) + 1
            maxf = max(maxf, character_counts[s[r]])

            while (r - l + 1) - maxf > k:
                character_counts[s[l]] -= 1
                l += 1
            result = max(result, (r - l + 1))
            

        return max(result, (r-l+1))
        