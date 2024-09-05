import collections

target = input().upper()
count = collections.Counter(target).most_common(n=2)

if len(count) == 1 or count[0][1] != count[1][1]:
    print(count[0][0])
else:
    print('?')