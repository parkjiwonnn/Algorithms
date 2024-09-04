# 백준 14568번

# 방법 1
N = int(input())
answer = 0
for A in range(0, N+1):
  for B in range(0, N+1):
    for C in range(0, N+1):
      if A + B + C == N:
        if A >= B + 2:
          if A != 0 and B != 0 and C != 0:
            if C % 2 == 0:
              answer += 1
print(answer)


# 방법 2

# 택희 : A, 2 이상 짝수
# 영훈 : B, 1 이상
# 남규 : C, B 보다 2개 이상 많아야 함

N = int(input())
answer = 0
for A in range(2, N, 2):
  for B in range(1, N):
    C = N - A - B
    if C >= B + 2:
      answer += 1
print(answer)