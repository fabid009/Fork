#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<string.h>
#include<sys/wait.h>

int main()
{
   int fd1[2],A[100],i,j;
   for(i=0; i<100; i++)
   {  
      A[i] = i;
   }

   pipe(fd1);
   int sum1 = 0;
   int cpid = fork();
  
   if(cpid == 0)
   {
       for(j=0; j<10; j++)
       {        
            sum1 = sum1 + A[j];
       }

        write(fd1[1], &sum1, sizeof(sum1));
        close(fd1[1]); 
   }

   else
   {
       int fd2[2], sum2 = 0;
       pipe(fd2);

       int cpid2 = fork();
       
       if(cpid2 == 0)
       {
          for(j=10; j<20; j++)
          {
               sum2 = sum2 + A[j];
          }

          write(fd2[1], &sum2, sizeof(sum2));
          close(fd2[1]); 
       }
       
       else
       { 
          int fd3[2], sum3 = 0;
          pipe(fd3);
        
          int cpid3 = fork();
       
          if(cpid3 == 0)
          {
              for(j=20; j<30; j++)
              {
                  sum3 = sum3 + A[j];
              }

              write(fd3[1], &sum3, sizeof(sum3));
              close(fd3[1]); 
          }
          
          else
          { 
              int fd4[2], sum4 = 0;
              pipe(fd4);
        
              int cpid4 = fork();
       
              if(cpid4 == 0)
              {
                  for(j=30; j<40; j++)
                  {
                      sum4 = sum4 + A[j];
                  }

                  write(fd4[1], &sum4, sizeof(sum4));
                  close(fd4[1]); 
              }
              
              else
              { 
                  int fd5[2], sum5 = 0;
                  pipe(fd5);
        
                  int cpid5 = fork();
       
                  if(cpid5 == 0)
                  {
                  for(j=40; j<50; j++)
                  {
                      sum5 = sum5 + A[j];
                  }

                  write(fd5[1], &sum5, sizeof(sum5));
                  close(fd5[1]); 
                  }
                  else
                  { 
                        int fd6[2], sum6 = 0;
                        pipe(fd6);
         
                        int cpid6 = fork();
       
                        if(cpid6 == 0)
                        {
                              for(j=50; j<60; j++)
                              {
                                   sum6 = sum6 + A[j];
                              }

                              write(fd6[1], &sum6, sizeof(sum6));
                              close(fd6[1]); 
                        }
                        
                        else
                        { 
                            int fd7[2], sum7 = 0;
                            pipe(fd7);
         
                            int cpid7 = fork();
       
                            if(cpid7 == 0)
                            {
                                 for(j=60; j<70; j++)
                                 {
                                     sum7 = sum7 + A[j];
                                 }

                                 write(fd7[1], &sum7, sizeof(sum7));
                                 close(fd7[1]); 
                            }
                             
                            else
                            { 
                                 int fd8[2], sum8 = 0;
                                 pipe(fd8);
         
                                 int cpid8 = fork();
         
                                 if(cpid8 == 0)
                                 {
                                     for(j=70; j<80; j++)
                                     {
                                         sum8 = sum8 + A[j];
                                     }

                                     write(fd8[1], &sum8, sizeof(sum8));
                                     close(fd8[1]); 
                                 }
      
                                 else
                                 { 
                                     int fd9[2], sum9 = 0;
                                     pipe(fd9);
         
                                     int cpid9 = fork();
       
                                     if(cpid9 == 0)
                                     {
                                        for(j=80; j<90; j++)
                                        {
                                           sum9 = sum9 + A[j];
                                        }

                                        write(fd9[1], &sum9, sizeof(sum9));
                                        close(fd9[1]); 
                                      }

                                      else
                                      { 
                                        int fd10[2], sum10 = 0;
                                        pipe(fd10);
         
                                        int cpid10 = fork();
           
                                        if(cpid10 == 0)
                                        {
                                           for(j=90; j<100; j++)
                                           {
                                                sum10 = sum10 + A[j];
                                           }

                                           write(fd10[1], &sum10, sizeof(sum10));
                                           close(fd10[1]); 
                                         }
 
                                         else
                                         {
                                              wait(NULL);
                                              read(fd1[0], &sum1, sizeof(sum1));
                                              read(fd2[0], &sum2, sizeof(sum2));
                                              read(fd3[0], &sum3, sizeof(sum3));
                                              read(fd4[0], &sum4, sizeof(sum4));
                                              read(fd5[0], &sum5, sizeof(sum5));
                                              read(fd6[0], &sum6, sizeof(sum6));
                                              read(fd7[0], &sum7, sizeof(sum7));
                                              read(fd8[0], &sum8, sizeof(sum8));
                                              read(fd9[0], &sum9, sizeof(sum9));
                                              read(fd10[0], &sum10, sizeof(sum10));
                                              int sum  = sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10;
                                              
                                              printf("Sum of numbers from 0 to 99 = %d \n", sum);
                                              close (fd1[0]);
                                              close (fd2[0]);
                                              close (fd3[0]);
                                              close (fd4[0]);
                                              close (fd5[0]);
                                              close (fd6[0]);
                                              close (fd7[0]);
                                              close (fd8[0]);
                                              close (fd9[0]);
                                              close (fd10[0]);
                                              exit(0);
                                   }
                              }
                           }
                        }
                     }
                  }
              }
          }   
       }
   }
   return 0;
}
