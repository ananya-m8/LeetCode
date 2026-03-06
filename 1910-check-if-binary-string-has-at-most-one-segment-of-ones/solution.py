class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if "1" in s:
            cnt = s.count("1")
            ind = s.index("1")
            if(s[ind:ind+cnt]=="1"*cnt):
                return True
        return False
