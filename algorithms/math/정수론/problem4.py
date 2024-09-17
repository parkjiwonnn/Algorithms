# 백준 14232번

N = int(input())

limit = int(N**0.5) + 1
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
primes = []

for i in range(2, limit+1):
  if is_prime[i]:
    primes.append(i)
    for j in range(i*2, limit+1, i):
      if is_prime[j]:
        is_prime[j] = False

answer = []
for prime in primes:
  while N % prime == 0:
    answer.append(prime)
    N //= prime

if N > 1:
  answer.append(N)

print(len(answer))
print(" ".join(map(str, answer)))