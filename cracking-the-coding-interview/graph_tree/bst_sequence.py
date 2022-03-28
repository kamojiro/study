import sys
from copy import deepcopy


class Node:
    def __init__(self, name=None, parent=None, left=None, right=None):
        self.name = name
        self.parent = parent
        self.left = left
        self.right = right
    def add_left_child(self, node):
        node.parent = self
        self.left = node
    def add_right_child(self, node):
        node.parent = self
        self.right = node

def bst_sequence(node):
    if node == None:
        return [[]]
    if not node.left and not node.right:
        return [[node.name]]
    left_bst_sequence_list = bst_sequence(node.left)
    right_bst_sequence_list = bst_sequence(node.right)
    ret = []
    for left_bst_sequence in left_bst_sequence_list:
        for right_bst_sequence in right_bst_sequence_list:
            ret.extend(weave_within_sequences(node.name, left_bst_sequence, right_bst_sequence))
    return ret

def weave_within_sequences(head, sequence1, sequence2):
    global count
    count = 0
    n1 = len(sequence1)
    n2 = len(sequence2)
    ret = []
    def recursive_weave(seq, index1, index2):
        global count
        if index1 == n1 and index2 == n2:
            count += 1
            print(count, " ".join(map(str, seq)), file=sys.stderr)
            ret.append(deepcopy(seq))
        if index1 < n1:
            seq.append(sequence1[index1])
            recursive_weave(seq, index1+1, index2)
            seq.pop()
        if index2 < n2:
            seq.append(sequence2[index2])
            recursive_weave(seq, index1, index2+1)
            seq.pop()
    recursive_weave([head], 0, 0)
    return ret

def test():
    node5 = Node(5)
    node10 = Node(10)
    node15 = Node(15)
    node20 = Node(20)
    node25 = Node(25)
    node50 = Node(50)
    node60 = Node(60)
    node70 = Node(70)
    node65 = Node(65)
    node80 = Node(80)
    node10.add_left_child(node5)
    node10.add_right_child(node15)
    node20.add_left_child(node10)
    node20.add_right_child(node25)
    node70.add_left_child(node65)
    node70.add_right_child(node80)
    node60.add_right_child(node70)
    node50.add_left_child(node20)
    node50.add_right_child(node60)
    sequences = bst_sequence(node50)
    for s in sequences:
        print(" ".join(map(str, s)))

def small_test():
    node5 = Node(5)
    node10 = Node(10)
    node15 = Node(15)
    node20 = Node(20)
    node25 = Node(25)
    node20.add_left_child(node10)
    node20.add_right_child(node25)
    node10.add_left_child(node5)
    node10.add_right_child(node15)
    sequences = bst_sequence(node20)
    for s in sequences:
        print(" ".join(map(str, s)))


if __name__=='__main__':
    test()
    # small_test()
    
    
    
