//  main.cpp
//  Baekjoon no.1924

#include <iostream>
using namespace std;

void calc(int mon, int day); // 1/1부터로의 차이 계산
void whichDay(int n); // 요일 판별

int main(){
    int month, day;
    cin >> month >> day;
    
    calc(month, day);
    
    return 0;
}

void calc(int mon, int day){
    int tempMonth = 1, tempDay = 0, sum = 0, result = 0;
    while (tempMonth < mon){
        switch (tempMonth) {
            case 2:
                tempDay = 28;
                sum += tempDay;
                tempMonth++;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                tempDay = 30;
                sum += tempDay;
                tempMonth++;
                break;
            default: // 1, 3, 5, 6, 7, 10, 12월
                tempDay = 31;
                sum += tempDay;
                tempMonth++;
        } // switch
    } // while
    sum += day;
    result = sum % 7;
    
    whichDay(result);
}

void whichDay(int n){
    if (n == 0) {
        cout << "SUN \n";
    }
    else if (n == 1){
        cout << "MON \n";
    }
    else if (n == 2){
        cout << "TUE \n";
    }
    else if (n == 3){
        cout << "WED \n";
    }
    else if (n == 4){
        cout << "THU \n";
    }
    else if (n == 5){
        cout << "FRI \n";
    }
    else {
        cout << "SAT \n";
    }
}
