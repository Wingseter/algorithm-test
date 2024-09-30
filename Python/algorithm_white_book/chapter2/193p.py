MAX_SIZE = 1000
decompressed = [[None] * MAX_SIZE for _ in range(MAX_SIZE)]

def decompress(it, y, x, size):
   head = it[y][x]

   if head == 'b' or head == 'w':
       for dy in range(y):
           for dx in range(x):
               decompressed[y + dy][x + dx] = head
   else:
       half = size / 2
       decompress(it, y, x, half)
       decompress(it, y, x + half, half)
       decompress(it, y + half, x, half)
       decompress(it, y + half, x + half, half)

