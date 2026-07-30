class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(beginWord)!=len(endWord):
            return 0
        queue=deque([(beginWord,1)])
        wordSet=set(wordList)
        while queue:
            word,dist=queue.popleft()
            if word==endWord:
                return dist
            letters=list(word)
            n=len(word)
            for i in range(n):
                original=letters[i]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if original==j:
                        continue
                    letters[i]=j
                    neww="".join(letters)
                    if neww in wordSet:
                        wordSet.remove(neww)
                        queue.append((neww,dist+1))
                letters[i]=original
        return 0
