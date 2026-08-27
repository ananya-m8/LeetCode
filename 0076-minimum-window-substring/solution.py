class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=Counter(t)
        window=Counter()
        req=len(need)
        left=0
        formed=0
        start=0
        min_len=float('inf')
        m=len(s)
        for right in range(m):
            char=s[right]
            window[char]+=1
            if char in need and window[char]==need[char]:
                formed+=1
            while formed==req:
                if right-left+1<min_len:
                    min_len=right-left+1
                    start=left
                left_char=s[left]
                window[left_char]-=1
                if left_char in need and window[left_char]<need[left_char]:
                    formed-=1
                left+=1
        if min_len==float('inf'):
            return ''
        return s[start:start+min_len]
