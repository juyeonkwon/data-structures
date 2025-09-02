class SortedArraySet:
    def __init__( self, capacity=100 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty( self ):
       return self.size == 0

    def isFull( self ):
       return self.size == self.capacity

    def __str__( self ) :
        return str(self.array[0:self.size])

    # 이진탐색 사용 가능 ***
    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False

    def append(self, e) :
        self.array[self.size] = e
        self.size += 1


    # 코드 7.4: 정렬된 배열을 이용한 집합의 insert 연산
    # 요소들이 정렬된 상태를 유지해야 함
    def insert(self, e) :   # O(n) -> O(n)
        if self.contains(e) or self.isFull() :
            return

        self.array[self.size] = e
        self.size += 1

        for i in range(self.size-1, 0, -1) :
            if self.array[i-1] <= self.array[i] : break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    def delete(self, e) :   # O(n) -> O(n)
        if not self.contains(e) :
            return

        i = 0
        while self.array[i] < e : i += 1

        self.size -= 1
        while i < self.size :
            self.array[i] < self.array[i+1]
            i += 1

    # 코드 7.5: 정렬되지 않은 배열을 이용한 집합의 == 연산
    def __eq__( self, setB ): # O(mn) ---> O(n+m)
        if self.size != setB.size :
            return False

        for i in range(self.size) :
            if self.array[i] != setB.array[i] :
                return False
        return True

    # 코드 7.6: 정렬된 배열을 이용한 집합의 union 연산
    def union( self, setB ):  # O(mn) -> O(n+m)
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b: 
                setC.append(a)
                i += 1
            else :
                setC.append(b)
                j += 1

        while i < self.size :
            setC.append(self.array[i])
            i += 1
        while j < setB.size :
            setC.append(setB.array[j])
            j += 1

        return setC

    # 도전 코딩!
    def intersect( self, setB ):  # O(mn) -> O(n+m)
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a == b :
                setC.append(a)
                i += 1
                j += 1
            elif a < b: 
                i += 1
            else :
                j += 1

        return setC

    # 도전 코딩!
    def difference( self, setB ):  # O(mn) -> O(n+m)
        setC = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a == b :
                i += 1
                j += 1
            elif a < b: 
                setC.append(a)
                i += 1
            else :
                j += 1

        return setC


if __name__ == "__main__":
    import random
    setA = SortedArraySet()
    setB = SortedArraySet()
    for i in range(5): 
        setA.insert(random.randint(1,9))
        setB.insert(random.randint(1,9))

    print('Set A:', setA)
    print('Set B:', setB)
    print('A U B:', setA.union(setB))
    print('A ^ B:', setA.intersect(setB))
    print('A - B:', setA.difference(setB))

