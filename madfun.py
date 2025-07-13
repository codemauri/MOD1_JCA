# Mauricio Florez
# Some math

from math import sqrt

def madfun():
    number = float(input("Please enter a decimal number: ")) # Converts input to float
    print("Absolute Value: ", abs(number))
    print("Rounded Number: ", round(number, 0))
    print("Sqrt: ", sqrt(abs(round(number))))




if __name__ == '__main__':
    madfun()