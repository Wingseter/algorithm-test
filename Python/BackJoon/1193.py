X = int(input())

compare = 1
adder = 2
while X > compare:
    compare = compare + adder
    adder += 1
adder -= 1

if adder % 2 == 0:
    first = X - (compare - adder)
    second = adder + 1 - first
else:
    second = X - (compare - adder)
    first = adder + 1 - second

print("{0}/{1}".format(first, second))