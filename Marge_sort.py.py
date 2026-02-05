#include <stdio.h>
void merge(int A[], int R, int B[], int S, int C[])
{
    int NA = 0, NB = 0, PTR = 0;

    /* Step 2: Compare */
    while (NA < R && NB < S)
    {
        if (A[NA] < B[NB])
        {
            C[PTR] = A[NA];
            PTR++;
            NA++;
        }
        else
        {
            C[PTR] = B[NB];
            PTR++;
            NB++;
        }
    }

    /* Step 3: Copy remaining elements */
    if (NA >= R)
    {
        while (NB < S)
        {
            C[PTR] = B[NB];
            PTR++;
            NB++;
        }
    }
    else
    {
        while (NA < R)
        {
            C[PTR] = A[NA];
            PTR++;
            NA++;
        }
    }
}

/* Merge Sort Function */
void mergeSort(int arr[], int n)
{
    if (n <= 1)
        return;

    int mid = n / 2;
    int A[mid], B[n - mid];

    /* Divide */
    for (int i = 0; i < mid; i++)
        A[i] = arr[i];

    for (int i = mid; i < n; i++)
        B[i - mid] = arr[i];

    /* Recursive calls */
    mergeSort(A, mid);
    mergeSort(B, n - mid);

    /* Merge */
    merge(A, mid, B, n - mid, arr);
}

/* Main Function */
int main()
{
    int arr[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(arr) / sizeof(arr[0]);

    mergeSort(arr, n);

    printf("Sorted Array:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}
