T = int(input()) #테스트 케이스 개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
i = [0,1,0,-1] # row 위치 오른쪽, 아래, 왼쪽, 위
j = [1,0,-1,0] # col 위치 오른쪽, 아래, 왼쪽, 위
for test_case in range(1, T + 1):
    N = int(input()) # N*N 행렬 의 N값 입력
    arr = [[0]*N for _ in range(N)] # N*N행렬

    num =1 # 첫 시작 숫자
    row, col = 0,0 # 첫 시작 위치
    x=0
    arr[row][col]= num # 첫번째 위치 값
    while num<=N*N:
        
        nr = row+i[x] # 행렬의 행 위치
        nc = col+j[x] # 행렬의 열 위치
        if 0<=nr<N and 0<=nc<N and arr[nr][nc] == 0:
            row, col = nr, nc
            arr[i][j]=num
            num+=1
        else:
            x = (x+1)%4
    print(f'#{test_case}')
    for lst in arr:
        print(*lst)
        
    
    
