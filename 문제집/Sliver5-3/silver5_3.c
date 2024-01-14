#include <stdio.h>
#include <stdlib.h>

void quickSort(int arr[], int L, int R) {
    int left = L, right = R;
    int pivot = arr[(L + R) / 2];    // pivot 설정 (가운데)
    int temp;
    do
    {
        while (arr[left] < pivot)    // left가 pivot보다 큰 값을 만나거나 pivot을 만날 때까지
            left++;
        while (arr[right] > pivot)    // right가 pivot보다 작은 값을 만나거나 pivot을 만날 때까지
            right--;
        if (left<= right)    // left가 right보다 왼쪽에 있다면 교환
        {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            /*left 오른쪽으로 한칸, right 왼쪽으로 한칸 이동*/
            left++;
            right--;
        }
    } while (left<= right);    // left가 right 보다 오른쪽에 있을 때까지 반복

    /* recursion */
    if (L < right)
        quickSort(arr, L, right);    // 왼쪽 배열 재귀적으로 반복

    if (left < R)
        quickSort(arr, left, R);    // 오른쪽 배열 재귀적으로 반복
}

int binary_search_tree(int*A, int s, int e, int key){
    if(s <= e){
        int mid = (s+e)/2;
        if (key == A[mid])
            return 1;
        else if(key > A[mid])
            return binary_search_tree(A, mid+1, e, key);
        else if(key < A[mid])
            return binary_search_tree(A, s, mid-1, key);
    }
    return 0;
}

int main(void){
    int N, M;

    scanf("%d", &N);
    int* A= (int*)malloc(sizeof(int) * N);
    for(int i = 0; i < N; i++){
        scanf("%d", &A[i]);
    }

    quickSort(A, 0, N-1);

    scanf("%d", &M);
    int* B= (int*)malloc(sizeof(int) * M);
    for(int i = 0; i < M; i++){
        scanf("%d", &B[i]);
    }

    for(int i = 0; i < M; i++){
        printf("%d\n", binary_search_tree(A, 0, N-1, B[i]));
    }

    free(A); free(B);
    return 0;
}



