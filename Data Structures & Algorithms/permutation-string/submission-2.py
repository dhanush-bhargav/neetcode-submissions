class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_counts = {}
        for i in range(len(s1)):
            s1_char_counts[s1[i]] = s1_char_counts.get(s1[i], 0) + 1
        
        l = r = 0

        while r < len(s2):
            while (l<len(s2)) and (s2[l] not in s1_char_counts):
                l += 1
                r = l
           
            if r >= len(s2):
                break

            if s2[r] in s1_char_counts:
                if s1_char_counts[s2[r]] > 0:
                    s1_char_counts[s2[r]] -= 1
                    r += 1
                else:
                    flag = False
                    for key in s1_char_counts.keys():
                        if s1_char_counts[key] == 0:
                            flag = True
                        else:
                            flag = False
                            break
                    if flag:
                        return True
                    else:
                        while s1_char_counts[s2[r]] == 0:
                            s1_char_counts[s2[l]] += 1
                            l += 1
            else:
                flag = False
                for key in s1_char_counts.keys():
                    if s1_char_counts[key] == 0:
                        flag = True
                    else:
                        flag = False
                        break
                if flag:
                    return True
                else:
                    while l<r:
                        s1_char_counts[s2[l]] += 1
                        l += 1


        flag = False
        for key in s1_char_counts.keys():
            if s1_char_counts[key] == 0:
                flag = True
            else:
                flag = False
                break
        return flag

            
            