# 백준 14252번

import math

N = int(input())  
A = list(map(int, input().split()))  
    
A.sort() 
    
answer = 0
    
for i in range(N - 1):
  if math.gcd(A[i], A[i+1]) != 1:
    answer += 1
    
print(answer)