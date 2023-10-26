#include <stdio.h>
#include<time.h>
#define SIZE 100

int num1[SIZE];
int num2[SIZE];
int idx1 = 0; 
int idx2 = 0; 

int factors(int num[], int m, int index)
{
    while (m % 2 == 0)
    {
        num[index++] = 2;
        m = m / 2;
    }

    for (int i = 3; i * i <= m; i = i + 2)
    {
        while (m % i == 0)
        {
            num[index++] = i;
            m = m / i;
        }
    }

    if (m > 2)
        num[index++] = m;

    return index;
}

int main()
{
    clock_t t;
    t = clock();

    int m, n;
    printf("Enter the value for m (bigger number): ");
    scanf("%d", &m);
    printf("Enter the value of n (smaller number): ");
    scanf("%d", &n);

    idx1 = factors(num1, m, idx1);
    idx2 = factors(num2, n, idx2);

    printf("Prime factors of m: ");
    for (int i = 0; i < idx1; i++)
    {
        printf("%d ", num1[i]);
    }
    printf("\n");

    printf("Prime factors of n: ");
    for (int i = 0; i < idx2; i++)
    {
        printf("%d ", num2[i]);
    }
    printf("\n");

    int gcd = 1;
    int i = 0;
    int j = 0;
    while (i < idx1 && j < idx2) 
    {
        if (num1[i] == num2[j])
        {
            gcd *= num1[i];
            i++; 
            j++;
        }
        else if (num1[i] < num2[j])
        {
            i++;
        }
        else
        {
            j++;
        }
    }
    printf("gcd is given by : %d\n", gcd);

    t = clock() - t;
    printf("Execution time in seconds : %f", ((double)t/CLOCKS_PER_SEC));

    return 0;
}