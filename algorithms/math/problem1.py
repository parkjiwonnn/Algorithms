# 백준 15736번

#   1 2 3 4 5 6 7 8 9 10
#   b b b b b b b b b b
# 1 w w w w w w w w w w
# 2   b   b   b   b   b
# 3     b     w     b    
# 4       w       w     
# 5         b         w
# 6           b         
# 7             b       
# 8               b     
# 9                 w   
# 10                  b
# white => 1, 4, 9 (제곱수)


N = int(input())

answer = int(N**0.5)

print(answer)