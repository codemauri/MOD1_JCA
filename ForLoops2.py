# Mauricio Florez
# Writing Loops2

import math

#1
def multiples(low,high, base):
    lower = int(low/base)
    upper = int((high/base) + 1)
    for factor in range (lower,upper):
        print(base*factor, end=" ")
    print()

def commaSpace(low,high, base):
    lower = int(low/base)
    upper = int((high/base) + 1)
    for factor in range (lower,upper):
        if factor == upper-1:
            print(base*factor)
            return
        print(base*factor, end=", ")
    print()

def avg(numbers):
    tab = 0 #aggregator variable
    for i in range(numbers):
        tab += eval(input("Please enter number:" ))
    avg = tab/numbers
    print("AVERAGE: ", round(avg,2))





if __name__ == '__main__':
    multiples(10,25,5)
    commaSpace(-3,21,3)
    avg(10)

