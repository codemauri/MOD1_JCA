def sum(N):
    if N <= 1:
        return 1
    else:
        return N + sum(N-1)


def sum2(N):
    sum  = 0
    for i in range(N+1):
        sum += i
    return sum

print(sum(5))
print(sum2(5))



