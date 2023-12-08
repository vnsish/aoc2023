import math

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.right = right
        self.left = left

    def __str__(self):
        return f'{self.name} = ({self.left}, {self.right})'
    
def findnode(name, nodetree):
    for node in nodetree:
        if node.name == name:
            return node
    return None

def partone(input):
    with open(input, 'r') as fp:
        data = fp.read()
    
    path = data.split('\nx\n')[0]
    nodes = data.split('\nx\n')[1]

    nodetree = []

    for node in nodes.split('\n'):
        nodetree.append(Node(node[0:3], node[7:10], node[12:15]))
    
    AAA = findnode('AAA', nodetree)
    curnode = AAA
    found = False
    movements = 0

    while not found:
        for instruction in path:
            movements += 1
            if instruction == 'R':
                curnode = findnode(curnode.right, nodetree)
            elif instruction == 'L':
                curnode = findnode(curnode.left, nodetree)
            if curnode.name == 'ZZZ':
                found = True
                break
    
    print(movements)

def parttwo(input):
    with open(input, 'r') as fp:
        data = fp.read()
    
    path = data.split('\nx\n')[0]
    nodes = data.split('\nx\n')[1]

    nodetree = {}
    starting_nodes = []

    for node in nodes.split('\n'):
        nodetree[node[0:3]] = (node[7:10], node[12:15])
        if node[2] == 'A':
            starting_nodes.append(node[0:3])

    min_steps = []

    for node in starting_nodes:
        found = False
        movements = 0
        while not found:
            for instruction in path:
                movements += 1
                if instruction == 'R':
                    node = nodetree[node][1]
                elif instruction == 'L':
                    node = nodetree[node][0]
                if node[2] == 'Z':
                    found = True
                    min_steps.append(movements)

    print(min_steps)
    print(math.lcm(*min_steps))

partone('input')
parttwo('input')