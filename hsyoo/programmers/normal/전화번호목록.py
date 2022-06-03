from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x), reverse = True)
    db = defaultdict(int)
    for phone_num in phone_book:
        if db.get(phone_num):
            return False
        else:
            temp = ''
            for case in phone_num:
                temp += case
                db[temp] += 1
    return True

print(solution(["119", "97674223", "1195524421"]))