#include <stdio.h>

void main() {
    int pid;
    pid = fork();
    printf("Process ID:%d", pid);
}