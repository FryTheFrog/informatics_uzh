#include <stdio.h>

void reverseArray(int arr[], int size) {
    for (int i = 0; i < size/2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - 1 -i];
        arr[size - 1 - i] = temp;
    }
}

int main() {
    int arr[] = {1,2,3,4,5};
    int size = sizeof(arr) / sizeof(arr[0]);

    reverseArray(arr,size);
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
        printf("\n");
}
