x, y, w, h = map(int, input().split())
available_list = [x, w - x, y, h - y]
print(min(available_list))