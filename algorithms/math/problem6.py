# 백준 2247번

def csod(n):
  total_sum = 0
    
  for i in range(2, n + 1):
    total_sum += i * (n // i - 1) * (n // i) // 2
    
  return total_sum

n = int(input())
print(csod(n) % 1000000)
