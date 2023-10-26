#include<stdio.h>
#include<time.h>
int main()
{
    clock_t t;
    t = clock();

    int m, n, r;
    printf("Enter the bigger number : ");
    scanf("%d", &m);
    printf("Enter the smaller number : ");
    scanf("%d", &n);
    while(n!=0)
    {
        r = m % n;
        m = n;
        n = r;
    }
    printf("GCD is : %d", m);
    t = clock() - t;
    printf("\nExecution time in seconds : %f", ((double)t/CLOCKS_PER_SEC));
    return 0;
}