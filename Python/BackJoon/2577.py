import collections

A = int(input())
B = int(input())
C = int(input())

multiple = str(A * B * C)

counts = collections.Counter(multiple)

for i in range(10):
    print(counts[str(i)])
