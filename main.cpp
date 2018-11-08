//
//  main.cpp
//  Baekjoon no.2490

#include <iostream>
using namespace std;

void judge(int arr[3][4]);

int main(){
    int array[3][4] = { 0 };
   
    // 윷을 던짐
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 4; j++){
            cin >> array[i][j];
        }
    }
    
    judge(array);
    
    return 0;
}

void judge(int arr[3][4]){
    int resultArr[3] = {0}; // 각 행의 sum 결과를 저장할 배열
    int sum = 0;
    
    // 각 행의 sum 결과를 계산
    for (int k = 0; k < 3; k++){
        for (int m = 0; m < 4; m++){
            sum += arr[k][m];
        }
        resultArr[k] = sum;
        sum = 0;
    }
    
    // 윷 판단
    for (int n = 0; n < 3; n++){
        if (resultArr[n] == 3)      { cout << "A" << endl; }
        else if (resultArr[n] == 2) { cout << "B" << endl; }
        else if (resultArr[n] == 1) { cout << "C" << endl; }
        else if (resultArr[n] == 0) { cout << "D" << endl; }
        else                        { cout << "E" << endl; }
    }
}
