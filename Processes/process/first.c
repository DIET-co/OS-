#include<stdio.h>

int main(){
    int n[5];
    for (i=0;i<5;i++){
        scanf("%d",&n[i]);
    }
    int pid=fork();

    if(pid==0){
        print("Smallest element is %d",n[0]);
        print("Largest element is %d",n[4]);
    }
    else{
        wait();
        for(i=0;i<4;i++){
            for(j=i+1;j<5;j++){
                if(n[i]<n[j]){
                    int a=n[i];
                    n[i]=n[j];
                    n[j]=a;
                }
            }
        }

    }
}