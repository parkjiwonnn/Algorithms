# 백준 14501번

def recur(idx, result):
    global answer

    if idx > n:
        if idx > n+1: return
        answer = max(answer, result)
        return

    recur(idx + table[idx][0], result + table[idx][1])
    recur(idx + 1, result)


n = int(input())
table = [[] for _ in range(n+1)]
for i in range(n):
    a, b = map(int, input().split())
    table[i+1] = [a, b]

# print(table)

answer = 0

recur(1, 0)

print(answer)
