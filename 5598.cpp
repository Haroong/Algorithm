// Baekjoon no.5598

#include <iostream>
#include <string>
using namespace std;

string decode (string s);

int main() {
    string str;
    
    cin >> str;
    cout << decode(str) << endl;
    
    return 0;
}

string decode (string s) {
    int len = (int) s.length();
    string answer = "";
    
    for (int i = 0; i < len; i++){
        if (s.at(i) >= 68) {
            s.at(i) -= 3;
            answer += s.at(i);
        }
        else {
            s.at(i) += 23; // A, B, C
            answer += s.at(i);
        }
    }
    return answer;
}
