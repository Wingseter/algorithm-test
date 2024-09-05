target = input()
table = str.maketrans('\
ABCDEFGHIJKLMNOPQRSTUVWXYZ', '\
22233344455566677778889999')
print(sum(list(map(int, target.translate(table))))+len(target))