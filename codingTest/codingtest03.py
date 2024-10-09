T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    x, y, N = map(int,input().split())
    num = 0
    if x+y < N :
        num+=1
        x += y
    elif y + x < N:
        num+=1
        y += x

    else:
        print(num)
        
