string = input().strip()
if len(string) == 0: print(0)
else: print(string.count(' ') + 1)