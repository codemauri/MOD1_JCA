# Mauricio Florez
# Writing Loops1


def oneToFiveLoop():
    for number in range (1,6):
        print(number)

def twoToEleven():
    for number in range (2,12,3):
        print(number)

def minusTenToZero():
    for number in range (-10,1,2):
        print(number, end=" ")
    print()

def asterisk():
     for r in range(4):
            print("****", end="\n")

def csi():
    for char in "CSI":
        print(char)
    print("150")

def oneToTen():
    for number in range(1,11):
        print(number)




if __name__ == '__main__':
    oneToFiveLoop()
    print("twoToEleven")
    twoToEleven()
    print("minusTenToZero")
    minusTenToZero()
    print("asterisk")
    asterisk()
    print("CSI")
    csi()
    print("OneToTen")
    oneToTen()

