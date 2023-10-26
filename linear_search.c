#include<stdio.h>
int main()
{
    int size;
    printf("Enter size of array :");
    scanf("%d", &size);
    int arr[size];
    for(int i = 0; i < size; i++)
    {
        arr[i] = i * 2; //filling array
    }
    int key;
    printf("Enter the key :");
    scanf("%d", &key);
    int pos = 0;
    for(int j = 0; j < size; j++)
    {
        if(arr[j] == key)
        {
            pos = j;
            break;
        }
    }
    printf("Element found at %d position in array", pos+1);
}