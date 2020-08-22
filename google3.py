class Solution:
    def totalFruit(self, trees) -> int:
        fruits = []
        pivot = 0
        i = 0
        maxSoFar = 0
        current = 0
        for (i, tree) in enumerate(trees):
            if tree in fruits or len(fruits) < 2:
                current += 1
            if tree not in fruits:
                if len(fruits) > 0:
                    fruits.pop(0)
                fruits.append(tree)
                current = i - pivot
            if tree == fruits[0]:
                pivot = i
            maxSoFar = max(current, maxSoFar)
        return maxSoFar
