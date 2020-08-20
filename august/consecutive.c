
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *numsSameConsecDiff(int N, int K, int *returnSize)
{
    *returnSize = 0;
    if (N == 1) {
        *returnSize = 10;
    } else {
        // TODO
    }
    int *values = malloc(sizeof(int) * N * K);
    if (!values)
    {
        exit(1);
    }
    return values;
}