//  main.cpp
//  Baekjoon no.10872

#include <iostream>
using namespace std;

int main(){
    int num, result = 1;
    cin >> num;
    
    for (int i = num; i > 1; i--){
        result *= i;
    }
    cout << result;
    
    return 0;
}
