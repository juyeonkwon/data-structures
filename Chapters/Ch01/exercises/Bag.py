# 코드 1.1: Bag의 주요 연산을 일반함수로 구현 예.  
def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append(e)

def remove(bag, e) :
    bag.remove(e)

def count(bag):
    return len(bag)


# 코드 1.2: Bag을 활용한 테스트 프로그램 
myBag = [ ]
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
print('내 가방속의 물건:', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('내 가방속의 물건:', myBag)



# 1.2절 도전코딩!: Bag의 추가 연산 numOf 구현
def numOf(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e :
            count = count + 1
    return count

# 추가 연산 테스트
print('빗 의 개수', numOf(myBag, '빗'))
print('빛 의 개수', numOf(myBag, '빛'))

