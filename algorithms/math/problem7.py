# 백준 2436번

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def find_numbers(g, l):
  if l % g != 0:
    return -1
    
  target = l // g
    
  min_sum = float('inf')
  result = (-1, -1)
    
  for i in range(1, int(target**0.5) + 1):
    if target % i == 0:  
      a, b = i, target // i
      if gcd(a, b) == 1:
        x, y = g * a, g * b
        if x + y < min_sum:
          min_sum = x + y
          result = (min(x, y), max(x, y))
    
  return result if result != (-1, -1) else -1

g, l = map(int, input().split())

result = find_numbers(g, l)

if result == -1:
    print(result)
else:
    print(result[0], result[1])
