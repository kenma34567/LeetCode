class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        """
            1) Make Combination Dict to find all the words can be converted into with diff = 1, in which the words are in wordList
            2) Use BFS to find the shortest path for each word in the combination dict

        """

        if endWord not in wordList:
            return 0

        def getComDictKey(word: str, i: int):
            return word[:i] + "*" + word[i + 1:]

        def bfs(word: str, comDict: dict, res: int):
            q = collections.deque()
            q.append(word)

            visited = set()
            while q:
                for i in range(len(q)):
                    current = q.popleft()
                    # print("current", current, res)
                    if current == endWord:
                        return res

                    for j in range(len(current)):
                        key = getComDictKey(current, j)
                        for comWord in comDict[key]:
                            if comWord in visited:
                                continue
                            q.append(comWord)
                            visited.add(comWord)
                    # print("new q", q)
                res += 1

            return 0

        # combination dict
        comDict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = getComDictKey(word, i)
                comDict[key].append(word)
                # print("C", comDict)

        return bfs(beginWord, comDict, 1)
