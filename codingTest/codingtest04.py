# coding test link:https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AY_gm8_6NjcDFAVF&categoryId=AY_gm8_6NjcDFAVF&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A = list(input()) # 첫번째 리스트 입
    B = list(input()) # 두번째 리스트 입력

    while len(B) != len(A): #B의 길이와 A의 길이가 같을 시 멈춤
        if B[-1] == 'X':

            B.pop(-1)
            
        elif B[-1] =='Y':
            B = B[:-1][::-1]  # 마지막 문자 제거하고 뒤집기
     
     
    ## A와 B의 길이를 같게 맞춘뒤 비교
    if A==B:
        print("#%d " % test_case, end="")
        print('Yes')
    else:
        print("#%d " % test_case, end="")
        print('No')
        

    
