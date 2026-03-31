class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        l=set(s)
        for i in l:
            if s.count(i)!=t.count(i):
                return False
        return True
