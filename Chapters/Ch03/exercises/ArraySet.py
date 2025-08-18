class ArraySet:
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

    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                return True
        return False

    def insert(self, e) :
        if not self.contains(e) and not self.isFull() :
            self.array[self.size] = e
            self.size += 1
        else : pass

    def delete(self, e) :
        for i in range(self.size) :
            if self.array[i] == e :
                self.array[i] = self.array[self.size-1]
                self.size -= 1

    def union( self, setB ):
        setC = ArraySet()
        for i in range(self.size) :
            setC.insert(self.array[i])

        for i in range(setB.size) :
            if not setC.contains(setB.array[i]) :
                setC.insert(setB.array[i])

        return setC

    def intersect( self, setB ):            
        setC = ArraySet()
        for i in range(setB.size) :
            if self.contains(setB.array[i]) :
                setC.insert(setB.array[i])
        return setC

    def difference( self, setB ):            
        setC = ArraySet()
        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                setC.insert(self.array[i])
        return setC

    # 도전 코딩!
    def __eq__( self, setB ):
        if self.size != setB.size :
            return False

        for i in range(self.size) :
            if not setB.contains(self.array[i]) :
                return False
        return True




'''
class ArraySet:
    def __init__( self ):
        self.items = []

    def size( self ): return len(self.items)
    def isEmpty( self ): return self.size() == 0

    def contains(self, item) :
        return item in self.items
        
        #for i in range(len(self.items)) :
        #    if self.items[i] == item :
        #        return True
        #return False


    def insert(self, elem) :
        if self.contains(elem) == False :
            self.items.append(elem)

    def delete(self, elem) :
        if self.contains(elem) :
            self.items.remove(elem)

    def union( self, setB ):                # C = self U  B
        newSet = ArraySet()
        newSet.items = list(self.items)
        for elem in setB.items :
            # if elem not in self.items :
            if not self.contains(elem) :
                newSet.items.append( elem)
        return newSet

    def intersect( self, setB ):            # C = self ^ B
        setC = ArraySet()
        for elem in setB.items :
            # if elem in self.items :
            if self.contains(elem) :
                setC.items.append(elem)
        return setC

    def difference( self, setB ):           # C = self - B
        setC = ArraySet()
        for elem in self.items:
            # if elem not in setB.items:
            if not setB.contains(elem) :
                setC.items.append(elem)
        return setC

    def display(self, msg):
        print(msg, self.items)

    def isProperSubsetOf( self, setB ):
        for elem in self.items :
            if elem not in setB : return False

        if self.size() == setB.size() : return False
        else: return True


#    def __eq__( self, setB ):
#        if self.size() != setB.size() :
#            return False
#        else :
#            return self.isSubsetOf( setB )

#    def isSubsetOf( self, setB ):
#        for elem in self.items :
#           if elem not in setB : return False
#       return True


#    def __iter__( self ):
#        return _SetIterator( self.items )
'''