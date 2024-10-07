
def bruteForce(h):
    ret = 0

    N = len(h)

    for left in range(N):
        minHeight = h[left]

        for right in N:
            minHeight = min(minHeight, h[right])
            ret = max(ret, (right - left + 1) * minHeight)

    return ret
