class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        sett = set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[i])
                i += 1
            sett.add(s[r])
            w = (r - i) + 1
            longest = max(longest, w)
        return longest