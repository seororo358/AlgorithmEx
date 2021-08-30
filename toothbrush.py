def solution(enroll, referral, seller, amount):
    money = {}
    en_refer = {}

    def tracking(child, per):
        if child == "-" or per == 0:
            return
        else:
            money[child] += per - per//10
            tracking(en_refer[child], per//10)

    for i in enroll:
        money[i] = 0

    for i,j in zip(enroll,referral):
        en_refer[i] = j

    for i in range(0,len(amount)):
        amount[i] *= 100

    for i in range(len(seller)):
        mon = amount[i]//10
        money[seller[i]] += amount[i] - mon
        tracking(en_refer[seller[i]], mon)

    answer = list(money.values())

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))