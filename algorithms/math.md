# 유클리드 호제법

호제법 : 두 수가 서로 상대방 수를 나누어 원하는 수를 구하는 것을 의미

두 자연수 a, b에 대해서(a>b) a를 b로 나눈 나머지를 r이라 하면, a와 b의 최대공약수는 b와 r의 최대 공약수와 동일

b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여, 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수

```
Q. 1071과 1029의 최대 공약수 구하기

1071 = 1029*1 + 42
1029 = 42*24 + 21
42 =  21*2 + 0
=> 21

def GCD(a, b):
  while b:
    a, b = b, a % b
  return a
```

어떠한 두 수의 곱은, 그 두 수의 최대공약수와 최소공배수의 곱과 같음

```
GCD : 최대공약수, LCM : 최소공배수
A = GCD * Q
B = GCD * W

LCM = GCD * Q * W
A * B = GCD * Q * GCD * W = GCD * LCM

def LCM(a, b):
  gcd = GCD(a, b):
  return (a * b) / gcd
```

Python math 모듈의 gcd, lcm 함수 사용 가능  
=> gcd : python 3.5, lcm : python 3.9 이상 지원

# 에라토스테네스의 체(소수 판별법)

1. 2부터 N까지 모든 정수를 적는다.
2. 아직 지우지 않은 소수 중 가장 작은 소수를 찾고 이 수를 P라고 한다.
3. 아직 지우지 않은 수들 중, P의 배수를 크기 순서대로 지운다.
4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

시간복잡도 : O(nlog(logn))

```
is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, N+1):
  # 아직 지우지 않은 수 중 가장 작은 소수 찾기
  if is_prime[i]:
    for j in range(i*2, N+1, i):
      # j가 소수가 아님을 is_prime 배열에 체크
      if is_prime[j]:
        is_prime[j] = False
```

## 참고

엘리스코딩 알고리즘의 정석 초급
