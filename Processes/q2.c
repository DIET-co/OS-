#include <stdio.h>

void main() {
    int arr[10];

    printf("Enter 10 numbers: ");
    for (int i = 0; i < 10; i++)
        scanf("%d", &arr[i]);

    int pid = fork();

    // parent
    if (pid > 0) {
        for (int i = 0; i < 10; i++) {
            for (int j = i + 1; j < 10; j++) {
                if (arr[j] < arr[i]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        printf("Sorted: ");
        for (int i = 0; i < 10; i++) {
            printf("%d ", arr[i]);
        }
    }

    // child
    if (pid == 0) {
        int min = arr[0];
        int max = arr[0];

        for (int i = 1; i < 10; i++) {
            if (arr[i] < min)
                min = arr[i];
            if (arr[i] > max)
                max = arr[i];
        }

        printf("Max: %d\tMin: %d", max, min);
    }
}