class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        parents = defaultdict(list)

        queue = deque([beginWord])

        visited = {beginWord}

        found = False

        while queue and not found:

            levelVisited = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                letters = list(word)

                for i in range(len(word)):

                    original = letters[i]

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == original:
                            continue

                        letters[i] = ch
                        nxt = "".join(letters)

                        if nxt in wordSet:

                            if nxt not in visited:

                                if nxt not in levelVisited:
                                    queue.append(nxt)
                                    levelVisited.add(nxt)

                                parents[nxt].append(word)

                                if nxt == endWord:
                                    found = True

                    letters[i] = original

            visited |= levelVisited

        if not found:
            return []

        ans = []

        path = [endWord]

        def dfs(word):

            if word == beginWord:
                ans.append(path[::-1])
                return

            for p in parents[word]:

                path.append(p)

                dfs(p)

                path.pop()

        dfs(endWord)

        return ans
