# 백준 1407번

A, B = map(int, input().split())

answer = 0
for i in range(A, B+1):
  cnt = 0
  while i % 2 == 0:
    cnt += 1
    i /= 2
  answer += 2**cnt

print(answer)