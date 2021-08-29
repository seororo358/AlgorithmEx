def solution(enroll, referral, seller, amount):

    money = {}
    for i in enroll:
        money[i] = 0

    for i in range(0,len(amount)):
        amount[i] *= 100



    answer = list(money.values())
    return answer