# 코드 8.10: 모스 코드 표와 인코딩 알고리즘
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

def encode(ch):
    idx = ord(ch)-ord('A')
    return table[idx][1]

# 코드 8.11: 모스코드 디코딩(순차탐색)
def decode_slow(code):
    for e in table:
        if code == e[1] :
            return e[0]
    return None


class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

# 코드 8.12: 모스 코드 결정 트리 만들기 
def make_morse_tree():
    root = TNode( None, None, None )
    for tp in table :
        code = tp[1]                    # 모스 코드
        node = root
        for c in code :                 # 맨 마지막 문자 이전까지 --> 이동
            if c == '.' :               # 왼쪽으로 이동
                if node.left == None :  # 비었으면 빈 노드 만들기
                    node.left = TNode (None, None, None)
                node = node.left        # 그쪽으로 이동
            elif c == '-' :             # 오른쪽으로 이동
                if node.right == None : # 비었으면 빈 노드 만들기
                    node.right = TNode (None, None, None)
                node = node.right     # 그쪽으로 이동

        node.data = tp[0]               # 코드의 알파벳
    return root

def decode(root, code):
    node = root
    for c in code :                 # 맨 마지막 문자 이전까지 --> 이동
        if c == '.' :               # 왼쪽으로 이동
            node = node.left
        elif c=='-' :
            node = node.right
    return node.data


# 코드 8.13: 모르스 코드 테스트 프로그램
if __name__ == "__main__":
    morseCodeTree = make_morse_tree()
    str = input("입력 문장 : ")
    mlist = []
    for ch in str:
        code = encode(ch)
        mlist.append(code)
    print("Morse Code: ", mlist)
    print("Decoding  : ", end='')
    for code in mlist:
        ch = decode(morseCodeTree, code)
        print(ch, end='')
    print()

    for code in mlist:
        ch = decode_slow(code)
        print(ch, end='')
    print()

