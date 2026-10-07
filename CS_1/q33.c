#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int fun(int A[], int n) {
    int swaps = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (A[j] > A[j + 1]) {
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                swaps++;
            }
        }
    }

    return swaps;
}

int main() {
    int A[30];
    int duplicate;

    srand(time(NULL));

    // Generate 30 distinct random numbers from 0 to 99
    for (int i = 0; i < 30; i++) {
        do {
            A[i] = rand() % 100;
            duplicate = 0;

            for (int j = 0; j < i; j++) {
                if (A[i] == A[j]) {
                    duplicate = 1;
                    break;
                }
            }
        } while (duplicate);
    }

    printf("Original array:\n");
    for (int i = 0; i < 30; i++)
        printf("%d ", A[i]);

    printf("\n\nNumber of swaps = %d\n", fun(A, 30));

    printf("\nSorted array:\n");
    for (int i = 0; i < 30; i++)
        printf("%d ", A[i]);

    printf("\n");

    return 0;
}
