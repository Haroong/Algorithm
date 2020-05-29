# ✔️ [문제](https://programmers.co.kr/learn/courses/30/lessons/12954)
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

제한 조건

- x는 -10000000 이상, 10000000 이하인 정수입니다.
- n은 1000 이하인 자연수입니다.

# 😎 소스 코드
```javascript
function solution(x, n) {
  let answer = [], temp = x;

  for (let i = 0; i < n; i++) {
    answer.push(x);
    x += temp;
  }

  return answer;
}
```

# ✊ 문제를 풀고 나서
힐링이 필요해서 푼 문제..
그리고 BOJ에서 문제 풀고 싶은데 Node.js로 입력받는게 상당히 까다로워 보였다. 검색해서 봐도 이해가 안 되더라. 자바스크립트 입력 받기 넘 어렵다 ㅠㅠ

