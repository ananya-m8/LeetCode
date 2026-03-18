class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        for i in range(len(l)):
            l[i]=l[i].strip()
        return " ".join(l[-1:-(len(l)+1):-1])

