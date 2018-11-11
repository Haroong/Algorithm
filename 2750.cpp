//  main.cpp
//  Baekjoon no.2750

#include <iostream>
using namespace std;

void sort(int arr[], int n);

int main(){
    int maxNum = 0;
    
    cin >> maxNum;
    
    int inputArr[maxNum]; // n까지의 정수를 저장하는 배열
    for (int i = 0; i < maxNum; i++){
        cin >> inputArr[i];
    }
    
    sort(inputArr, maxNum);
    
    for (int m = 0; m < maxNum; m++){
        cout << inputArr[m] << "\n";
    }
    return 0;
}

void sort(int arr[], int n){
    int temp = 0, k;
    
    // sorting (by bubble sort)
    for (int j = n; j > 0; j--){
        for (k = 0; k < n-1; k++){
            // swap
            if (arr[k] > arr[k+1]){
                temp = arr[k];
                arr[k] = arr[k+1];
                arr[k+1] = temp;
            }
        }
        temp = 0;
    }
}
