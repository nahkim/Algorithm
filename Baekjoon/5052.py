import sys

# 방법 1

# t = int(sys.stdin.readline())

# for i in range(t):
#     n = int(sys.stdin.readline())

#     phone_list = [sys.stdin.readline().strip() for i in range(n)]
#     phone_list.sort()

#     index = 0
#     check = 0
    
#     while index < n - 1:
#         phone_num = phone_list[index]
#         phone_len = len(phone_num)

#         if phone_num == phone_list[index + 1][:phone_len]:
#             print("NO")
#             check = 1
#             break
#         else:
#             index += 1

#     if check == 0:
#         print("YES")

# 방법 2

class Node:

    def __init__(self, data=None): 
        self.child = {}
        self.data = data
        self.is_end = True

class Trie:

    def __init__(self):
        self.root = Node(None)
    
    def insert(self, data):

        curr_node = self.root

        for i in data:
            if i not in curr_node.child:
                new_ = Node(i)
                curr_node.child[i] = new_
                curr_node.is_end = False
            curr_node = curr_node.child[i]

    def search(self, data):

        curr_node = self.root

        for w in data:
            curr_node = curr_node.child[w]
        if curr_node.child:
            return False
        return True



t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    phone_list = [sys.stdin.readline().strip() for i in range(n)]

    trie = Trie()

    for phone_num in phone_list:
        trie.insert(phone_num)

    check = False
    for phone_num in phone_list:
        if not trie.search(phone_num):
            print("NO")
            check = True
            break
    if check == False:
        print("YES")