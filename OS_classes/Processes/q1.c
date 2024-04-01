// write a c program to read two strings and to create a child process the parent process should reverse
// the second string and append it to the first string.the child process should compare the first 5
// characters of both the strings and display the results

#include <stdio.h>
#include <string.h>

void main() {
    char str1[10], str2[10];
    printf("Enter string 1: ");
    scanf("%s", str1);
    printf("Enter string 2: ");
    scanf("%s", str2);

    int pid = fork();

    // parent
    if (pid > 0) {
        int counter = 0;
        char result[20];

        for (; counter < strlen(str1); counter++) {
            result[counter] = str1[counter];
        }

        for (int i = 0; i < strlen(str2); i++) {
            result[counter++] = str2[strlen(str2) - i - 1];
        }

        printf("%s", result);
    }

    // child
    if (pid == 0) {
        if (strlen(str1) < 5 || strlen(str2) < 5)
            printf("Minimum length of strings must be 5");
        else {
            for (int i = 0; i < 5; i++) {
                if (str1[i] != str2[i]) {
                    printf("First 5 characters are not equal");
                    return;
                }
            }
            printf("First 5 characters are equal");
        }
    }
}