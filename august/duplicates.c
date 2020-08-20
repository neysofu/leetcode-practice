#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

void
zeroOutOriginals(int *nums, int numsSize) {
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] == i + 1) {
            nums[i] = 0;
        }
    }
}

int
countAndRearrangeDuplicates(int *nums, int numsSize) {
    int count = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] > 0) {
            const int bucket = nums[i] - 1;
            if (nums[bucket] == 0) {
                count++;
            }
            nums[bucket] = -1;
            nums[i] = 0;
        }
    }
    return count;
}

void
initDuplicates(int *buffer, int *nums, int numsSize) {
    int j = 0;
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0) {
            buffer[j++] = i + 1;
        }
    }
}

// [4,3,2,7,8,2,3,1]
// [1,2,3,4,3,2,7,8]
//
// [0,0,0,0,3,2,0,0]

int *findDuplicates(int *nums, int numsSize, int *returnSize)
{
    {
        int i = 0;
        while (i < numsSize)
        {
            const int bucket = nums[i] - 1;
            if (nums[i] == nums[bucket]) {
                // Either the value has already been placed correctly or it is a
                // duplicate. There's nothing to do.
                i++;
            } else {
                // Place the current value at the right index; the next value
                // will be ready for the next iteration.
                int tmp = nums[i];
                nums[i] = nums[bucket];
                nums[bucket] = tmp;
            }
        }
    }
    zeroOutOriginals(nums, numsSize);
    *returnSize = countAndRearrangeDuplicates(nums, numsSize);
    int *duplicates = malloc(sizeof(int) * *returnSize);
    if (!duplicates)
    {
        exit(1);
    }
    initDuplicates(duplicates, nums, numsSize);
    return duplicates;
}

int main() {
    int arr[] = {2,2};
    int returnSize = 0;
    int *duplicates = findDuplicates(arr, 2, &returnSize);
    printf("%d\n", returnSize);
    printf("%d\n", duplicates[1]);
}