#include<stdio.h>
#include<math.h>

void main()
{
  int T;
  scanf("%d",&T);
  long int total_sum[100000];
  for(int i=0; i<T; i++)
  {
    long int N;
    scanf("%lf",N);
    
    long int sum = 0;
    long int numbers[1000000000]
    for(int j=0;j<N;j++)
    {
      scanf("%lf",N[j]);
    }
    
    for(j=0;j<N-1;j++)
      for(k=j+1;j<N;k++)
        sum = sum + (numbers[j]*numbers[k]*(2**(N+1-k)));
      
  total_sum[i]=sum;
    
  }
  
  for(int i=0;i<T;i++)
  {
    printf("%lf",total_sum[i]);
  }
}


  
