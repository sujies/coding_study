def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }
    
    # choices에 따른 점수 계산
    for i in range(len(survey)):
        first_type = survey[i][0]  # 비동의 시 점수를 받는 성격 유형
        second_type = survey[i][1]  # 동의 시 점수를 받는 성격 유형
        choice = choices[i]

        if choice < 4:  # 비동의 선택지 (1, 2, 3)
            scores[first_type] += 4 - choice
        elif choice > 4:  # 동의 선택지 (5, 6, 7)
            scores[second_type] += choice - 4

    # 각 지표에서 점수를 비교하고 성격 유형 결정
    result = []
    result.append('R' if scores['R'] >= scores['T'] else 'T')
    result.append('C' if scores['C'] >= scores['F'] else 'F')
    result.append('J' if scores['J'] >= scores['M'] else 'M')
    result.append('A' if scores['A'] >= scores['N'] else 'N')

    return ''.join(result)
