def solution(numbers, hand):
    phone = {
            1:(1,1), 2:(1,2), 3:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            7:(3,1), 8:(3,2), 9:(3,3),
            '*':(4,1), 0:(4,2), '#':(4,3)
        }
    # print(phone)
    
    # 초기 손 위치 설정
    left_thumb = phone['*']
    right_thumb = phone['#']


    result =[]
    for i in numbers:
        # 왼쪽 숫자: 1, 4, 7
        if i in [1, 4, 7]:
            result.append('L')
            left_thumb = phone[i]
        # 오른쪽 숫자: 3, 6, 9
        elif i in [3, 6, 9]:
            result.append('R')
            right_thumb = phone[i]
        else: # 이외 숫자 2,5,8,0
            left_distance = abs(left_thumb[0] - phone[i][0]) + abs(left_thumb[1] - phone[i][1])
            right_distance = abs(right_thumb[0] - phone[i][0]) + abs(right_thumb[1] - phone[i][1])
            if left_distance < right_distance:
                result.append('L')
                left_thumb = phone[i]
            elif left_distance > right_distance:
                result.append('R')
                right_thumb = phone[i]
            else:
                if hand =='right':
                    result.append('R')
                    right_thumb = phone[i]
                else:
                    result.append('L')
                    left_thumb = phone[i]
    return ''.join(result)
