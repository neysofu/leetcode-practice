def calculateWordVariants(word):
    variants = []
    for i in range(len(word)):
        variants.append(word[:i] + '?' + word[i + 1:])
    return variants


class WordLadder:

    def __init__(self, words):
        variantsToWords = {}
        variants = {}
        for word in words:
            variants[word] = calculateWordVariants(word)
            for variant in variants[word]:
                if variant not in variantsToWords:
                    variantsToWords[variant] = []
                variantsToWords[variant].append(word)
        self.graph = {}
        for word in words:
            self.graph[word] = []
            for variant in variants[word]:
                self.graph[word] += variantsToWords[variant]
            self.graph[word] = set(self.graph[word])
            self.graph[word].remove(word)

    def search(self, beginWord, endWord):
        explored = {beginWord: None}
        queue = [beginWord]
        while len(queue) > 0 and endWord not in explored:
            word = queue.pop(0)
            for neighbor in self.graph[word]:
                if neighbor not in explored:
                    queue.append(neighbor)
                    explored[neighbor] = word
        if endWord not in explored:
            return 0
        # Find shortest path via backtracking.
        depth = 1
        word = endWord
        while word != beginWord and word is not None:
            word = explored[word]
            depth += 1
        return depth


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        graph = WordLadder(wordList + [beginWord])
        return graph.search(beginWord, endWord)


print(Solution.ladderLength(None, "hit", "cog", ["hot","dot","dog","lot","log"]))
