#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<sys/types.h>
int main()
{
key_t k=456;
int shmid;
int i;
int *shmptr,*s;
shmid=shmget(k,30*sizeof(i),IPC_CREAT|0666);
printf("created");
shmptr=shmat(shmid,NULL,0);
printf("attached");
s=shmptr;
for(i=1;i<=10;i++)
*s++=i;
s=0;
printf("end");
while(*shmptr!=0)
sleep(1);
shmdt(shmptr);
shmctl(shmid,IPC_RMID,NULL);
return 1;
}
