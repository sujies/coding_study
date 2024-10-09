T = int(input())
for test_case in range(1, T + 1): #테스트 케이스 개수
    A = int(input()) #상품 개수
    B = list(map(int, input().split())) # 상품 금액 입력(정상가+할인가)
    result =[] #할인된 가격 넣기
    while len(result) !=A:
        for i in range(1,len(B)):
            if B[0] ==B[i]*3//4: # 할인된 가격 찾기
                result.append(B[0]) # 찾으면 결과 리스트에 넣기
               	B.pop(0) # 할인된 가격 빼기
                B.pop(i) #정상 가격 빼기
                break #for 문에서 빠지기
    print("#"+str(test_case), " ".join(map(str, result)))
