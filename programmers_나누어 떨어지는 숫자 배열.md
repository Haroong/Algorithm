# programmers

### 문제: 나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910

``` javascript
function solution(arr, divisor) {
  let answer = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % divisor === 0) {
      answer.push(arr[i]);
    }
  }

  if (answer.length === 0) {
    answer.push(-1);
  } else {
    answer.sort(function(a, b) {
      return a - b;
    });
  }

  return answer;
}

console.log(solution([2, 36, 1, 3], 1));
```

### 문제를 풀고 나서
자기 전에 뭐 풀까 하다가 푼 문제.. 쉬웠다
