class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1={}
        n=len(s)
        for i in range(n):
            if s[i] in d1:
                if d1[s[i]]!=t[i]:
                    return False
            elif t[i] in d1.values():
                return False
            d1[s[i]]=t[i]
        return True
