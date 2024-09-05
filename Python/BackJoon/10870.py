N = int(input())

def fibonachi(num_prev, num_now, counter):
    if counter == 0:
        return num_prev
    return fibonachi(num_now, num_now + num_prev, counter - 1)

print(fibonachi(0, 1, N))