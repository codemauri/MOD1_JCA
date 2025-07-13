def add(x,y):
    return x + y

def multiply(x,y):
    return x*y


if __name__ == '__main__':
    nums = [float(input(f"Enter number {i + 1}: ")) for i in range(2)]
    print("SUM: ", add(*nums), "PRODUCT: ", multiply(*nums))



