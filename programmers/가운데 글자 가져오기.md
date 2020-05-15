# programmers
### 문제: 가운데 글자 가져오기 
https://programmers.co.kr/learn/courses/30/lessons/12903

```javascript
function solution(s) {
  let answer = "";
  const len = s.length;
  const pos = Math.floor(len / 2);

  if (len % 2 === 0) {
    // even number
    answer = s[pos-1] + s[pos];
  } else {
    // odd number
    answer = s[pos];
  }
  return answer;
}
```
### 문제를 풀고 나서
문자열의 길이에 따라서 문자열 처리를 다르게 했다.
