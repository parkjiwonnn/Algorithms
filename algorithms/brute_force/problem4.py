# 백준 2503번

n = int(input())
hint = [list(map(str, input().split())) for _ in range(n)]
answer = 0

for a in range(1, 10): # 100의 자리수
  for b in range(1, 10): # 10의 자리수
    for c in range(1, 10): # 1의 자리수
      
      # 숫자 야구 불가능한 조건은 패스
      if (a == b or b == c or c == a):
        continue
      
      # 숫자가 정해졌다면 abc와 number를 비교        
      cnt = 0    
      for arr in hint:
        number = list(arr[0])
        strike = int(arr[1])
        ball = int(arr[2])

        strike_count = 0
        if (a == int(number[0])):
          strike_count += 1
        if (b == int(number[1])):
          strike_count += 1
        if (c == int(number[2])):
          strike_count += 1
        
        ball_count = 0
        if (a == int(number[1]) or a == int(number[2])):
          ball_count += 1
        if (b == int(number[0]) or b == int(number[2])):
          ball_count += 1
        if (c == int(number[0]) or c == int(number[1])):
          ball_count += 1

        if ball != ball_count or strike != strike_count:
          break
        
        cnt += 1
          
      if cnt == n:
        answer += 1
        
print(answer)