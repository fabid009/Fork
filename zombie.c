#include<stdio.h>
int main()
{
   int cpid;
   cpid = fork();

   if (cpid == -1)
   {
       printf("\nFork Failed\n");
       exit(1);
   }

   if(cpid > 0)
   {
      printf("\nHello I am Parent\n");
      sleep(10); //Parent sleeps for 10s and cannot read childs exit status although child has completed execution.So,child will become zombie.
      printf("\nExiting\n");
   }

   else   
   {
      printf("\nHello I am child\n");
      printf("\nWaiting for parent to read exit status\n");
   }
}
