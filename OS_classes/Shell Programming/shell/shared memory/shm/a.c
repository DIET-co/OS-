#include<stdio.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<stdlib.h>
#include<sys/shm.h>
#define SHMSZ 27
main()
{
char c;
int shmid;
key_t key;
char *shm,*s;
key=5678;
printf("Done");
if((shmid=shmget(key,SHMSZ,IPC_CREAT|0666))<0)
{
perror("shmget failed");
exit(1);
}
if((shm=shmat(shmid,NULL,0))==(char *)-1)
{
perror("shmat failed");
exit(1);
}
printf("Done");
s=shm;
for(c='a';c<='z';c++)
*s++=c;
*s=NULL;
printf("Done");
while(*shm!='*')
sleep(1);
exit(0);
}
