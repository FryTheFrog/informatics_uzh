#include <stdio.h>

// modified morge sort algo
// (1) parameter for sorting order (ascending / descending)
// (2) check if array is already sorted
// (3) if partial array size <= 6, use insertion sort algo

void merge(int arr[], int p, int q, int r) {

    int n1 = q - p + 1;
    int n2 = r - q;

    int L[n1], M[n2];

    for (int i = 0; i < n1; i++)
        L[i] = arr[p + i];
    for (int j = 0; j < n2; j++)
        M[j] = arr[q + 1 + j];

    int i, j, k;
    i = 0;
    j = 0;
    k = p;

    while (i < n1 && j < n2) {
        if (L[i] <= M[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = M[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = M[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);

        merge(arr, l, m, r);
    }
}

void insertionSort(int arr[], int size) {
    for (int step = 1; step < size; step++) {
        int key = arr[step];
        int j = step - 1;

        while (key < arr[j] && j >= 0) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = key;
    }
}

int isSortedAsc(int arr[], int size) {
    for (int i = 0; i < size-1; i++)
        if (arr[i] > arr[i+1]) {
            return 0;
        }
    return 1;
}

int isSortedDesc(int arr[], int size) {
    for (int i = 0; i < size-1; i++)
        if (arr[i] < arr[i+1]) {
            return 0;
        }
    return 1;
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
        printf("\n");
}

int main() {
    int arr[] = {6, 5, 12, 10, 9, 1};
    int size = sizeof(arr) / sizeof(arr[0]);

    // asc = True -> Ascending order
    int asc = 1;

    mergeSort(arr, 0, size - 1);

    printf("sorted array:\n");
    printArray(arr, size);
    
    return 0;
}
