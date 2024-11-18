#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void 
setup(int64_t N, uint64_t A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);
   for (int i = 0; i < N; i++){
      A[i]= lrand48() % N;
   }
}

int64_t
sum(int64_t N, uint64_t A[])
{
   int64_t sum = 0;
   int indx = A[0];

   printf(" inside sum_indirect perform_sum, N=%lld \n", N);
   for (int64_t i=0; i < N; i++){
      sum += A[indx];
      indx += A[indx];
   }
   return sum;
}

