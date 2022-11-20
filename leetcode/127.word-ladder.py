#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        if len(beginWord) != len(endWord):
            return 0
        if len(beginWord) == 1:
            return 2
        corr = { s: i for i, s in enumerate(wordList)}
        n = len(wordList)
        m = len(beginWord)
        edges = [set() for _ in range(n)]
        for key, index in corr.items():
            if m != len(key):
                continue
            for i in range(m):
                p, q = key[:i], key[i+1:]
                a = ord(key[i])
                for c in range(26):
                    if c == a:
                        continue
                    next_word = p + chr(c+ord("a")) + q
                    if next_word in corr:
                        edges[index].add(corr[next_word])
                        edges[corr[next_word]].add(index)
        M = 10**5
        dist = [M]*n
        start = corr[beginWord]
        dist[start] = 1
        goal = corr[endWord]
        queue = deque([start])
        while queue:
            v = queue.popleft()
            if v == goal:
                return dist[v]
            for w in edges[v]:
                if dist[w] == M:
                    dist[w] = dist[v]+1
                    queue.append(w)                    
        return 0

# @lc code=end

