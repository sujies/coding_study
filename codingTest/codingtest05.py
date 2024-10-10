#coding test link: https://school.programmers.co.kr/learn/courses/30/lessons/258712
def solution(friends, gifts):
    # 각 친구가 준 선물과 받은 선물을 기록할 딕셔너리 초기화
    given = {friend: 0 for friend in friends}
    received = {friend: 0 for friend in friends}
    gift_count_between = {friend: {f: 0 for f in friends} for friend in friends}
    
    for gift in gifts:
        giver, receiver = gift.split()
        given[giver] += 1
        received[receiver] += 1
        gift_count_between[giver][receiver] += 1

    # 각 친구의 선물 지수 계산
    gift_index = {friend: given[friend] - received[friend] for friend in friends}
    # print("gift_count:\n", gift_count_between)


    next_month={friend:0 for friend in friends}
    for giver in friends:
        for receiver in friends[friends.index(giver)+1:]:
            # print("선물 준사람:{}, 선물 받은사람:{}".format(giver, receiver))
            if gift_count_between[giver][receiver]< gift_count_between[receiver][giver]:
                next_month[receiver]+=1
            elif gift_count_between[giver][receiver]> gift_count_between[receiver][giver]:
                next_month[giver]+=1
            else:
                if gift_index[giver]>gift_index[receiver]:
                    next_month[giver]+=1
                elif gift_index[giver]<gift_index[receiver]:
                    next_month[receiver]+=1
                
    return max(next_month.values())
