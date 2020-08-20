#include <stdbool.h>
#include <assert.h>

bool isPowerOfFour(int num)
{
    if (num < 0) {
        return false;
    }
    bool isPowerOfTwo = (num & (num - 1)) == 0;
    unsigned long long allPowersOfFour = 0x5555555555555555ULL;
    return isPowerOfTwo && (num & allPowersOfFour);
}

int main() {
    assert(isPowerOfFour(1));
    assert(isPowerOfFour(4));
    assert(isPowerOfFour(16));
}