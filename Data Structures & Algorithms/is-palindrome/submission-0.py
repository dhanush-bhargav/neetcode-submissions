class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_without_spaces = "".join(s.split(" "))
        start = 0
        end = len(s_without_spaces) - 1

        while start < end:
            if s_without_spaces[start].isalnum() and s_without_spaces[end].isalnum():
                if s_without_spaces[start].lower() != s_without_spaces[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            elif not s_without_spaces[start].isalnum():
                start += 1
            elif not s_without_spaces[end].isalnum():
                end -= 1
        return True