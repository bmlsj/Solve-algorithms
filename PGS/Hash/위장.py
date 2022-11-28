clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]


def solution(clothes):
    hash = {}
    for n, t in clothes:
        hash[t] = 0

    for key in hash.keys():
        cnt = 0
        for n, t in clothes:
            if key == t:
                cnt += 1

        hash[key] = cnt

    print(hash)
    value = list(hash.values())
    ans = 1
    for i in value:
        ans *= (i + 1)

    return ans - 1


print(solution(clothes))

