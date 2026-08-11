class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_counts = {}
        for i in range(len(t)):
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1

        if len(t_counts.keys()) == 0: return ""

        window = {}

        found, need = 0, len(t_counts)
        res, res_length = [-1,-1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in t_counts and window[c] == t_counts[c]:
                found += 1

            while found == need:
                if (r-l+1) < res_length:
                    res = [l,r]
                    res_length = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_counts and window[s[l]] < t_counts[s[l]]:
                    found -= 1
                l += 1

        l,r = res

        return s[l:r+1] if res_length != float("infinity") else ""