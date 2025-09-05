from collections import deque

# -------------------------------
# 노드 클래스
# -------------------------------
class TNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None


# -------------------------------
# 순회 함수들 (전역 함수)
# -------------------------------
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    """deque를 이용한 레벨 순회"""
    if root is None:
        return
    q = deque([root])
    while q:
        n = q.popleft()
        if n is not None:
            print(n.data, end=' ')
            if n.left:  q.append(n.left)
            if n.right: q.append(n.right)


# -------------------------------
# 트리 계산/평가 함수들
# -------------------------------
def count_node(n):
    if n is None:
        return 0
    return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    if n.isLeaf():
        return 1
    return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hL = calc_height(n.left)
    hR = calc_height(n.right)
    return (hL + 1) if hL > hR else (hR + 1)

def evaluate(n):
    """수식 트리 평가: 단말은 피연산자(숫자), 내부노드는 연산자(+, -, *, /)"""
    if n is None:
        return 0
    if n.left is None and n.right is None:
        return n.data
    op1 = evaluate(n.left)
    op2 = evaluate(n.right)
    if n.data == '+': return op1 + op2
    if n.data == '-': return op1 - op2
    if n.data == '*': return op1 * op2
    if n.data == '/': return op1 / op2
    raise ValueError(f'지원하지 않는 연산자: {n.data}')

def calc_size(n):
    """폴더 크기 누적 예제: 각 노드 data를 숫자로 가정하여 합산"""
    if n is None:
        return 0
    return n.data + calc_size(n.left) + calc_size(n.right)


# -------------------------------
# BinaryTree 클래스 (추가)
# -------------------------------
class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def printPreOrder(self, msg='Pre-Order : '):
        print(msg, end='')
        preorder(self.root)
        print()

    def printInOrder(self, msg='In-Order : '):
        print(msg, end='')
        inorder(self.root)
        print()

    def printPostOrder(self, msg='Post-Order : '):
        print(msg, end='')
        postorder(self.root)
        print()

    def printLevelOrder(self, msg='Level-Order : '):
        print(msg, end='')
        levelorder(self.root)
        print()


# -------------------------------
# 테스트 함수들
# -------------------------------
def testBinaryTree():
    d = TNode('D')
    e = TNode('E')
    b = TNode('B', d, e)
    f = TNode('F')
    c = TNode('C', f, None)
    root = TNode('A', b, c)

    tree = BinaryTree(root)
    tree.printInOrder()
    tree.printPreOrder()
    tree.printPostOrder()
    tree.printLevelOrder()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))

def testExprTree():
    # (3 * 2) + (5 - 6) = 6 + (-1) = 5
    n1 = TNode(3)
    n2 = TNode(2)
    n3 = TNode('*', n1, n2)
    n4 = TNode(5)
    n5 = TNode(6)
    n6 = TNode('-', n4, n5)
    root = TNode('+', n3, n6)

    tree = BinaryTree(root)
    tree.printInOrder('식(중위표기) : ')
    print('Evaluate =>', evaluate(root))

def testFolderSize():
    # 리프: 파일 크기(단위 KB), 내부: 폴더(0)라고 가정
    m4 = TNode(200)
    m5 = TNode(500)
    m3 = TNode(100, m4, m5)  # 폴더 크기 누적 예를 위해 중간 노드도 숫자 가능
    m2 = TNode(50)
    root = TNode(0, m2, m3)
    tree = BinaryTree(root)
    tree.printInOrder('폴더 트리 중위 : ')
    print("Total Size =", calc_size(root), "KB")


# -------------------------------
# 실행부
# -------------------------------
if __name__ == '__main__':
    print("\n======= 이진트리 기본 테스트 =======")
    testBinaryTree()

    print("\n======= 수식 트리 테스트 =======")
    testExprTree()

    print("\n======= 폴더 크기 테스트 =======")
    testFolderSize()
