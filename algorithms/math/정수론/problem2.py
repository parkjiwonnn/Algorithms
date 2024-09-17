# 백준 1978번

N = int(input())
list = input().split()

answer = 0
for i in list:
  int_i = int(i)
  
  if i == 1:
    continue
  
  result = []
  for j in range(1, int_i+1):
    if int_i % j == 0:
      result.append(j)
      
  if len(result) == 2:
    answer += 1

print(answer)



