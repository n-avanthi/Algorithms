#include <stdio.h>
#include <math.h>
#include <string.h>
void len(char str1[]);
void ucase(char str1[]);
void lc(char str1[], char str2[]);
void rev(char str1[]);
void ec(char str1[], char str2[]);
void lcase(char str1[]);
void concat(char str1[], char str2[]);

void main()
{
    int i, length, count = 1, choice, n, n1;
    char str1[100], str2[100];
    printf("\n1.Length\n2.ucase\n3.lcase\n4.conactenate\n5.length comapre\n6.compare elements\n7.reverse\n");
    scanf("%d", &choice);
    printf("\n Enter the string1 length :");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%s", &str1[i]);
    }
    if (choice == 1)
    {
        len(str1);
    }
    else if (choice == 2)
    {
        ucase(str1);
    }
    else if (choice == 3)
    {
        lcase(str1);
    }
    else if (choice == 4)
    {

        scanf("%d", &n1);
        printf("enter string2:");
        for (int i = 0; i < n1; i++)
        {
            scanf("%s", &str2[i]);
        }
        concat(str1, str2);
    }

    else if (choice == 5)
    {
        printf("enter string2:");
        scanf("%d", &n1);
        for (int i = 0; i < n; i++)
        {
            scanf("%s", &str2[i]);
        }
        lc(str1, str2);
    }
    else if (choice == 6)
    {
        printf("enter string2:");
        scanf("%d", &n1);
        for (int i = 0; i < n; i++)
        {
            scanf("%s", &str2[i]);
        }
        ec(str1, str2);
    }
    else
    {
        rev(str1);
    }
}

void len(char str1[])
{
    int count = 0;
    for (int i = 0; str1[i] != '\0'; i++)
    {
        count++;
    }
    printf("length:%d", count);
}

void ucase(char str1[])
{

    char ucase[100];
    for (int i = 0; str1[i] != '\0'; i++)
    {
        if (str1[i] >= 'A' && str1[i] <= 'Z')
        {
            ucase[i] = str1[i];
        }
        else
        {
            ucase[i] = (str1[i] + 32);
        }
    }
    for (int i = 0; str1[i] != '\0'; i++)
    {
        printf("%s", str1[i]);
    }
}

void lcase(char str1[])
{
    char lcase[30];

    for (int i = 0; str1[i] != '\0'; i++)
    {
        if (str1[i] >= 'a' && str1[i] <= 'z')
        {
            lcase[i] = str1[i];
        }
        else
        {
            lcase[i] = (str1[i] - 32);
        }
    }
    for (int i = 0; str1[i] != '\0'; i++)
    {
        printf("%s", str1[i]);
    }
}
void concat(char str1[], char str2[])
{
    int str3[100], count = 0;
    for (int i = 0; str1[i] != '\0'; i++)
    {
        str3[i] = str1[i];
        count++;
    }
    for (int i = 0; str1[i] != '\0'; i++)
    {
        str3[count] = str2[i];
    }
    printf("\n The concatenated string is:");
    for (int i = 0; str3[i] != '\0'; i++)
    {
        printf("%s", str3[i]);
    }
}
void lc(char str1[], char str2[])
{
    int count1 = 0, count2 = 0;
    for (int i = 0; str1[i] != '\0'; i++)
    {
        count1++;
    }
    for (int i = 0; str2[i] != '\0'; i++)
    {
        count2++;
    }
    if (count1 == count2)
    {
        printf("equal length");
    }
    else
    {
        printf("uneual lenth");
    }
}
void rev(char str1[])
{
    int str3[100];
    int j = strlen(str1);
    for (int i = 0; str1[i] != '\0'; i++)
    {
        str3[j - 1] = str1[i];
        j--;
    }
    for (int i = 0; str3[i] != '\0'; i++)
    {
        printf("%s", str3[i]);
    }
}
void ec(char str1[], char str2[])
{
    int l1 = strlen(str1);
    int l2 = strlen(str2);
    if (l1 == l2)
    {
        for (int i = 0; str1[i] != '\0'; i++)
        {
            if (str1[i] != str2[i])
            {
                printf("unequal strings");
            }
            else
                printf("equal strings");
        }
    }
    else
        printf("unequal strings");
}