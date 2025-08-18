# 2.7절 도전 문제

# 1
def sum_iter(n) :
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum

# 2
def sum_recur(n) :
    if n == 1 :
        return 1
    else :
        return n + sum_recur(n-1)

print("1~10까지의 합(반복) =", sum_iter(10))
print("1~10까지의 합(순환) =", sum_recur(10))