//
//  new.c
//  
//
//  Created by Hugh O'Reilly on 10/6/18.
//

#include "fib.h"
#include <time.h>
#include <stdlib.h>

int fac(int i) {
    if (i == 0) {
        return 1;
    } else {
        return i * fac(i-1);
    }
}

long long fib(long long i) {
    return (i == 0 || i == 1) ? 1 : fib(i-1) + fib(i-2);
}

int fibdp(int i) {
    int dp[i+1];
    dp[0] = 1;
    dp[1] = 1;
    for(int j = 2; j <= i; j++) {
        dp[j] = dp[j-1] + dp[j-2];
    }
    return dp[i];
}

int main(int argc, char *argv[])
{
    clock_t begin = clock();
    
    int arg = atoi(argv[1]);
    fib(arg);
    
    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    
    printf("%f\n", time_spent);
    return 0;
}
