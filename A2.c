#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
 
int A[100];

void * Sum(void *arg)
{
	int start = (int)arg, end = start + 10, tempSum = 0;
	
        for(int i=start; i<end; i++)
             tempSum = A[i] + tempSum;

	return ((void*)tempSum);
}

int main()
{
	int sum[10],finalSum = 0;
	pthread_t T[10];

        for( int i=0; i<100; i++ )
             A[i] = i; 

	for (int i = 0; i < 10; i++)
	{
		pthread_create(&T[i], NULL, Sum,(void*)(i*10));
	}

        for(int j = 0; j < 10; j++ )
        {
                pthread_join(T[j], (void**)& sum[j]); 
                finalSum = finalSum + sum[j];
        }        

	printf("\nSum ( 0 to 99 ) = %d\n", finalSum);

	return 0;
}
