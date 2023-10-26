#include<stdio.h>
#include<math.h>
int main()
{
    int size;
    printf("Enter size of array :");
    scanf("%d", &size);
    int arr[size];
    for(int i = 0; i < size; i++)
    {
        arr[i] = i*2; //filling array
    }
    int key;
    printf("Enter the key :");
    scanf("%d", &key);
    int pos = 0;
    int low = 0;
    int high = size-1;
    int mid = floor((low + high)/2);
    while(mid < size)
    {
        if(arr[mid] == key)
        {
            pos = mid;
            break; 
        }
        else if(arr[mid] < key)
        {
            low = mid+1;
        }
        else if(arr[mid] > key)
        {
            high = mid-1;
        }
        mid = floor((low + high)/2);

    }
    printf("Position is %d", pos+1);
}