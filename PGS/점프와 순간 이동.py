def solution(n):
    # k칸 점프 -> k 건전지량 감소
    # (현재 위치*2) 위치로 순간이동

    # 0 -> 1 -> 2 -> 4 -> 5
    # 0 -> 1 -> 2 -> 3 -> 6

    battery = 0
    while n != 0:
        if n % 2 == 0:
            n //= 2

        else:
            n -= 1
            battery += 1

    return battery
print(solution(6))
