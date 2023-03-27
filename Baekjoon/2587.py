list_ = []
for i in range(5):
    list_.append(int(input()))
list_.sort()

average = sum(list_) // 5
midian = list_[2]
print(average, midian, sep='\n')