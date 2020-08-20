LOWER_VOWELS = 'aeiou'

def goatify_word(word: str, index: int) -> str:
    if word[0].lower() not in LOWER_VOWELS:
        word = word[1:] + word[0]
    word += 'ma' + 'a' * index
    return word

class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        return ' '.join([goatify_word(word, i + 1) for (i, word) in enumerate(words)])
        

