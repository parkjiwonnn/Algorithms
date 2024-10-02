# 백준 2961번

def recur(idx, sin, sun, use):
    global answer

    if idx == n:
        if use > 0:
            answer = min(answer, abs(sin - sun))
        return

    recur(idx + 1, sin * foods[idx][0], sun + foods[idx][1], use+1)
    recur(idx + 1, sin, sun, use)


n = int(input())

foods = [() for _ in range(n)]

for i in range(n):
    a, b = map(int, input().split())
    foods[i] = (a, b)

answer = 1e9

recur(0, 1, 0, 0)

print(answer)
