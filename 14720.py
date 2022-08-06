n =  int(input())
list_ = list(map(int, input().split()))
select_ = 0
count = 0
for i in range(n):
	if select_ == 3:
		select_ = 0
	if list_[i] == select_:
		count += 1
		select_ += 1
print(count)