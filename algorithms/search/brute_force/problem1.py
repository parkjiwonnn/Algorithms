# 백준 1816번

# 2 이상 1000000 미만 약수 O -> 잘못된 암호
TC = int(input())
for _ in range(TC):
  num = int(input())
  for i in range(2, 1000001):
    if num % i == 0: # 1000000 이하의 약수 O
      print("NO")
      break
    if i == 1000000: # 1000000 이하의 약수 X
      print("YES")
