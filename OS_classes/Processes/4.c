#include <stdio.h>

void main() {
    int pid;
    pid = fork();
    if (pid == 0)
        printf("Child");
    else
        printf("Parent");
}