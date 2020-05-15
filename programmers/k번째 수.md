# programmers
### 문제: k번째 수
https://programmers.co.kr/learn/courses/30/lessons/42748

```javascript
function solution(array, commands) {
  let answer = [];

  for (let i = 0; i < commands.length; i++) {
    let temp = [];
    let startPoint = commands[i][0];
    let endPoint = commands[i][1];
    let rep = endPoint - startPoint + 1;
    let goalPoint = commands[i][2];
    for (let j = 0; j < rep; j++) {
      temp[j] = array[startPoint - 1];
      startPoint++;
    }
    temp.sort(function(a, b) {
      return a - b;
    });

    answer.push(temp[goalPoint - 1]);
  }
  return answer;
}
```
### 문제를 풀고 나서
javascript의 sort()가 일반적으로 생각하는 숫자 정렬이 아닌 문자열 유니코드를 따라서 정렬해준다.<br />
이걸 몰라서 처음에 정렬이 이상하게 됐다.
