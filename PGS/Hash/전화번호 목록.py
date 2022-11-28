phone_book = ["12", "123", "1235", "567", "88"]


def solution(phone_book):
    answer = 0
    phone_book.sort()

    find = phone_book[0]

    v = []
    for i in range(1, len(phone_book)):
        v.append(phone_book[i][:len(phone_book[0])])

    for idx, value in enumerate(v):
        if value == find:
            i = phone_book[idx + 1]
            phone_book.remove(i)
            answer += 1

        else:
            answer += 0

    phone_book.remove(find)

    if answer != 0:
        return False

    return True


def solution2(phone_book):
    ans = True
    hash = {}

    for i in phone_book:  # 모든 요소를 (전화번호) {'전화번호' : 1} 형식으로 담는다
        hash[i] = 1

    for i in phone_book:
        tmp = ''
        for j in i:
            tmp += j
            if tmp in phone_book and tmp != i:
                ans = False

    return ans


def sol3(phone_book):
    phone_book.sort(key=lambda x: len(x))  # 길이로 정렬
    print(phone_book)

    for a in range(len(phone_book)):  # 리스트 기준요소를 반복문 돌리기
        for b in range(a + 1, len(phone_book)):  # 기준 요소의 다음 요소부터 반복문 돌리기
            # 다음 요소가 기준요소의 길이로 잘랐을때 값이 같으면 false
            if phone_book[b][:len(phone_book[a])] == phone_book[a]:
                return False

    return True


def sol4(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
    return True


print(sol4(phone_book))
# print(sol3(phone_book))
# print(solution2(phone_book))
# solution(phone_book)
# print(solution(phone_book))
