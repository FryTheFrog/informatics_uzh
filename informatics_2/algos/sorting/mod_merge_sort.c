#include <stdio.h>

// modified morge sort algo
// (1) parameter for sorting order (ascending / descending)
// (2) check if array is already sorted
// (3) if partial array size <= 6, use insertion sort algo

// trash code, but seems to be working (?)

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

void reverseArray(int arr[], int size) {
    for (int i = 0; i < size/2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - 1 -i];
        arr[size - 1 - i] = temp;
    }
}

void insertionSort(int arr[], int size) {
    for (int step = 1; step < size; step++) {
        int key = arr[step];
        int j = step - 1;

        while (key < arr[j] && j >= 0) {
            arr[j + 1] = arr[j];
            j--;
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

int isSorted(int arr[], int size, int asc) {
    if (isSortedAsc(arr, size)) {
        if (asc) {
            return 1;
        } else {
            reverseArray(arr, size);
            return 1;
        }
    }
    if (isSortedDesc(arr, size)) {
        if (!asc) {
            return 1;
        } else {
            reverseArray(arr, size);
            return 1;
        }
    }
    return 0;
}

void mergeSort(int arr[], int l, int r, int asc) {
    if (isSorted(arr, r + 1, asc)) {
        return;
    }

    if (r < 6) {
        insertionSort(arr, r + 1);
    }

    if (l < r) {

        int m = l + (r - l) / 2;

        mergeSort(arr, l, m, asc);
        mergeSort(arr, m + 1, r, asc);

        merge(arr, l, m, r);
    }
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
    // asc = False -> Descending order
    int asc = 0;

    mergeSort(arr, 0, size - 1, asc);
    if (!asc) {
        reverseArray(arr, size);
    }

    printf("sorted array:\n");
    printArray(arr, size);
    
    return 0;
}
