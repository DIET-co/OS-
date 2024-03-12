#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/ipc.h>
#include<sys/shm.h>
void main()
{
key_t k=456;
int shmid;
int i;
int * shmptr,*t;
shmid=shmget(k,20*sizeof(i),0666);
shmptr=shmat(shmid,NULL,0);
t=shmptr;
printf("receving");
while(*t!=0)
{
printf("%d",*t);
t++;
}

printf("recived successful");
*shmptr=0;
shmdt(shmptr);
printf("end");
}
