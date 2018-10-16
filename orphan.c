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

   if(cpid == 0)
   {
      printf("\nHello I am Child\n");
      sleep(5);  //Child will sleep while parent exits So, Child process becomes orphan
      printf("\nChild Exiting\n");
   }

   else   
   {
      printf("\nHello I am Parent\n");
      printf("\nParent terminating\n");
   }
}
