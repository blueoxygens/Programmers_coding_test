from collections import defaultdict

class Node:
    
    def __init__(self, cord, hash):
        self.x = cord[0]
        self.level = cord[1]
        self.value = hash[cord]
        self.right = None
        self.left = None
    
    def getValue(self):
        return self.value
    
    def getX(self):
        return self.x
    
    def getLevel(self):
        return self.level
    
    def getLeft(self):
        return self.left
        
    def getRight(self):
        return self.right
        
    def addLeft(self, node):
        self.left = node
        
    def addRight(self, node):
        self.right = node
        
def preorder(root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.value)
        if node.right:  stack.append(node.right)
        if node.left:   stack.append(node.left)
    return res

def postorder(root):
    stack, res = [root], []
    while stack:
        node = stack.pop()
        res.append(node.value)
        if node.left:   stack.append(node.left)
        if node.right:  stack.append(node.right)
    return res[::-1]
    
def solution(nodeinfo):
    answer = []
    
    if not nodeinfo:
        return [[], []]
    
    #hash table로 점의 번호를 저장
    hash_table = defaultdict(int)
    
    for k, v in enumerate(nodeinfo):
        hash_table[tuple(v)] = k+1
    
    #트리 구성을 위해 정렬
    sorted_nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    
    hash_table_x = defaultdict(list)
    
    for x, y in sorted_nodeinfo :
        hash_table_x[y].append(Node((x,y),hash_table)) 
    
    # print(hash_table_x)
    
    #트리 구성
    root = Node(tuple(sorted_nodeinfo[0]), hash_table)
    lvs = list(hash_table_x.keys())

    for i in lvs[1:]:
        for node in hash_table_x[i]:
            cn = root
            while True:
                if cn.getX() < node.getX():
                    if cn.getRight():
                        cn = cn.getRight()
                        continue
                    cn.addRight(node)
                    break
                if cn.getLeft():
                    cn = cn.getLeft()
                    continue
                cn.addLeft(node)
                break
    #전위 순회
    answer.append(preorder(root))
    #후위 순회
    answer.append(postorder(root))
    return answer