#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

size_t sizeOfTranslation(const char *S) {
    size_t len = strlen(S);
    size_t numWords = 1;
    for (size_t i = 0; i < len; i++) {
        if (S[i] == ' ') {
            numWords++;
        }
    }
    size_t numAdditionalLetters = numWords * (numWords + 1) / 2;
    return len + numAdditionalLetters;
}

const char LOWER_VOWELS[] = "aeiou";

bool isVowel(const char c) {
    return strchr(LOWER_VOWELS, tolower(c));
}

char *toGoatLatin(char *S)
{
    char *const translation = malloc(sizeOfTranslation(S));
    if (!translation) {
        exit(1);
    }
    int wordIndex = 1;
    char *buffer = translation;
    char *nextWord = NULL;
    do {
        nextWord = strchr(S, ' ');
        int wordLen = nextWord ? nextWord - S : strlen(S);
        printf("word is %d\n", wordLen);
        printf("word is %s\n", S);
        *buffer = '\0';
        printf("buf is %s\n", buffer);
        if (isVowel(S[0])) {
            // First rule.
            for (int i = 0; i < wordLen; i++) {
                *buffer++ = S[i];
            }
        } else {
            // Second rule.
            for (int i = 1; i < wordLen; i++) {
                *buffer++ = S[i];
            }
            *buffer++ = S[0];
        }
        *buffer++ = 'm';
        *buffer++ = 'a';
        // Third rule.
        for (int i = 0; i < wordIndex; i++) {
            *buffer++ = 'a';
        }
        wordIndex++;
    } while ((S = nextWord + 1));
    *buffer = '\0';
    return translation;
}

int main() {
    printf("%s\n", toGoatLatin("I speak Goat latin"));
}