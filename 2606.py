from pprint import pprint
# 인접 리스트
pc_count = int(input())
list_ = [[] for _ in range(pc_count + 1)]
n = int(input())
for _ in range(n):
    u, v = map(int, input().split())
    list_[u].append(v)
    # list_[v].append(u)
pprint(list_)
total_list = []
total = 0
i = 1
while list_.count(list_[i]):
    for j in list_[i]:
        list_[j].count()
        # total_list.append[j]
print(total)

# from pprint import pprint
# # 인접 행렬
# pc_count = int(input())
# graph = [[0 for _ in range(pc_count + 1)] for _ in range(pc_count + 1)]
# # pprint(graph)
# n = int(input())
# for _ in range(n):
#     u, v = map(int, input().split())
#     graph[u][v] = 1
#     graph[v][u] = 1
# total = 0

# pprint(graph)