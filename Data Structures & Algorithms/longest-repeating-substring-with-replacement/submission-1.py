class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        l=result=maxf=0

        for r in range (len(s)):
            char_counts[s[r]] = char_counts.get(s[r],0) + 1
            maxf = max(maxf, char_counts[s[r]])
            while (r-l+1) - maxf > k:
                char_counts[s[l]] = char_counts[s[l]] - 1
                l += 1
            result = max(result, (r-l+1))

        return max(result, (r-l+1))
        