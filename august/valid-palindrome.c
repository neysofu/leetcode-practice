#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <assert.h>

bool isPalindrome(const char *s)
{
	int i = 0;
	int j = strlen(s) - 1;
	while (i <= j) {
		if (!isalnum(s[i])) {
			i++;
		} else if (!isalnum(s[j])) {
			j--;
		} else if (tolower(s[i++]) != tolower(s[j--])) {
			return false;
		}
	}
	return true;
}

int main(void) {
	assert(isPalindrome("race a car"));
}