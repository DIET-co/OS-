#include <stdio.h>

void main() {
    int num, pid, square, half;
    printf("Enter a number");
    scanf("%d", &num);
    pid = fork();
    if (pid == 0) {
        square = num * num;
        printf("The square of the number is %d", square);
    } else  // parent task
    {
        half = num / 2;
        printf("The half of the number is %d", half);
    }
}