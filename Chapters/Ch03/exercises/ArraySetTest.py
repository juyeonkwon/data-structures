from ArraySet import ArraySet

setA = ArraySet()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
print('Set A:', setA)

setB = ArraySet()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
print('Set B:', setB)

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
print('Set A:', setA)
print('Set B:', setB)

print('A U B:', setA.union(setB))
print('A ^ B:', setA.intersect(setB))
print('A - B:', setA.difference(setB))

'''
s1 = { 1,2,3 }
s2 = { 2,3,4,5 }
s3 = s1.union(s2)
s4 = s1.intersection(s2)
print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s4:", s4)
print("range(1,9):", range(1,9))
c1 = 1 + 2j
#c1 = complex(1,2)
c2 = complex(3,4)
c3 = c1 + c2
print("c1:",c1)
print("c2:",c2)
print("c3:",c3)
'''