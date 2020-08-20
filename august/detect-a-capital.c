#include <string.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <assert.h>

bool detectCapitalUse(const char *word)
{
	size_t len = strlen(word);
	// Any string shorter than two characters is automatically valid.
	if (len < 2)
	{
		return true;
	}
	// Let's check immediately the validity of the first two characters.
	bool fstIsCapital = isupper(word[0]);
	bool sndIsCapital = isupper(word[1]);
	if (!fstIsCapital && sndIsCapital)
	{
		return false;
	}
	// Now we verify that all characters after the second one have its same case.
	for (size_t i = 2; i < len; i++)
	{
		if ((bool)isupper(word[i]) != sndIsCapital)
		{
			return false;
		}
	}
	return true;
}