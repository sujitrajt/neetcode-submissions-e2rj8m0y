class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_freq = 0 
        window_length = 0 

        for end in range(len(s)):
            count[s[end]] = count.get(s[end],0) + 1 
            max_freq = max(max_freq,count[s[end]])

            while (end-start+1) - max_freq > k:
                count[s[start]] -= 1 
                start += 1 
        
            window_length = max(window_length, end-start+1)
        return window_length