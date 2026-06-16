class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        length = 0
        count = {}
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            while (r - i + 1) - max(count.values()) > k:
                count[s[i]] -= 1
                i += 1
            
            length = max(length, (r - i) + 1)
        return length
