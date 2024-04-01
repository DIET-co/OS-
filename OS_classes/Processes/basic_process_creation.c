/*Program to create a fork() and demonstrate execution of parent and child process */
#include <stdio.h>
void main() {
    int pid;
    pid = fork();
    int a;
    // fork();

    // printf("hello");
    if (pid == 0) {
        a = 100;
        printf("%d\n", a);
        printf("getpid()=%d\n", getpid());
        printf("This is being printed from the child process\n");
        printf("Inside child = %d\n", pid);
    } else if (pid > 0) {
        wait();
        a = 150;
        printf("%d\n", a);
        printf("getpid()=%d\n", getpid());
        printf("This is being printed from the parent process\n");
        printf("Inside parent = %d\n", pid);
    } else
        printf("fork failed\n");
}
