#coding test link: https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    from datetime import datetime # 데이터 타입 변환
    types = {type:int(period) for type, period in [term.split() for term in terms]}
    print(types) # 약관 종류와 유효기간
    # 결과를 저장할 딕셔너리 초기화
    privacy = {}

    # 리스트를 반복하면서 딕셔너리 생성
    for index, item in enumerate(privacies, start=1):
        date_str, code = item.split()  # 날짜와 코드를 분리
        date_obj = datetime.strptime(date_str, "%Y.%m.%d")  # 문자열을 datetime 객체로 변환
        privacy[index] = [date_obj, code]  # 딕셔너리에 저장

    today = datetime.strptime(today, "%Y.%m.%d") # 날짜 변환
    print(today)

    def add_month(date,month):
        year = date.year
        new_month = date.month +month
        day = date.day
          # 월이 12를 초과할 경우 연도 증가 및 월 조정
        while new_month > 12:
            year += 1
            new_month -= 12

        return year, new_month, day
    
    answer = []
    for i in range(1,len(privacies)+1):
        print(privacy[i])
        if privacy[i][1] in types.keys(): # 약관 종류 비교
            print(privacy[i][1])
            new_date = add_month(privacy[i][0],types[privacy[i][1]])
            print(new_date)
            if new_date[0]< today.year:
                answer.append(i)
            elif new_date[0] == today.year:
                if new_date[1] < today.month:
                    answer.append(i)
                elif new_date[1] == today.month:
                    if new_date[2] <= today.day:
                        answer.append(i)   
    return answer
