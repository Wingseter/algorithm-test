num_list = set()

check = 1
for check in range(10000):
    check = sum(list(map(int, str(check)))) + check

    if check <= 10000:
        num_list.add(check)

for i in range(10000):
    if i not in num_list:
        print(i)