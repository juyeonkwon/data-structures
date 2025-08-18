def insert(bag, e) :
    bag.append(e)


# 코드 1.3: 실행시간 측정
import time

myBag = [ ]
start = time.time()

# Bag에 축구공을 100만번 삽입하는 코드
for _ in range(1000000) :
    insert(myBag, '축구공')

end = time.time()
print("실행시간 = ", end-start)


