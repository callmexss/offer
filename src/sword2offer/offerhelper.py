import random
import string


# Class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


# Functions
def gen_random_list(size=10, l=0, r=10):
    assert l <= r
    return [random.randint(l, r) for i in range(size)] 


def create_linked_list(li):
    head = ListNode(0) 
    cur = head
    for each in li:
        tmp = ListNode(each)
        cur.next = tmp
        cur = cur.next
    return head.next

def convert_linked_list_to_list(list_node):
    li = []
    while list_node:
        li.append(list_node.val)
        list_node = list_node.next
    return li

def gen_totally_random_str(n=10, l=10):
    li = []
    for i in range(n):
        li.append([random.choice(string.ascii_lowercase) for i in range(random.randint(1, l))])
    return [''.join(x) for x in li]


# Tree traverse
def pre_order(root):
    ret = []
    __pre_order(root, ret)
    return ret

def __pre_order(root, ret):
    if root:
        ret.append(root.val)
        __pre_order(root.left, ret)
        __pre_order(root.right, ret)

def in_order(root):
    ret = []
    __in_order(root, ret)
    return ret

def __in_order(root, ret):
    if root:
        __in_order(root.left, ret)
        ret.append(root.val)
        __in_order(root.right, ret)

def post_order(root):
    ret = []
    __post_order(root, ret)
    return ret

def __post_order(root, ret):
    if root:
        __post_order(root.left, ret)
        __post_order(root.right, ret)
        ret.append(root.val)


if __name__ == '__main__':
    li = gen_random_list()
    print(li)
    head = create_linked_list([1, 2, 3])
    li = convert_linked_list_to_list(head)
    print(li)
    str_list = gen_totally_random_str(20, 10)
    for s in sorted(str_list):
        print(s)

