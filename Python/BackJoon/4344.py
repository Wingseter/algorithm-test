N = int(input())
datas = []

for i in range(N):
    datas.append(list(map(int, input().split())))

averages = [sum(data[1:]) / data[0] for data in datas]

percentages = []
for index, data in enumerate(datas):
    percentages.append(len([num for num in data[1:] \
        if num > averages[index]]) / data[0] * 100)

for percent in percentages:
    print("{:.3f}%".format(percent))