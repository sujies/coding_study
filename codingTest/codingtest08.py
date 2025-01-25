# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3


def solution(nums):
    # 폰켓몬 종류의 개수
    unique_types = len(set(nums))
    # 가져갈 수 있는 최대 마리 수
    max_pick = len(nums) // 2
    # 가져갈 수 있는 종류의 최댓값은 두 값 중 작은 값
    return min(unique_types, max_pick)