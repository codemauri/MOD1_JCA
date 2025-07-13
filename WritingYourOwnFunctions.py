#Write a function, pyramid,
# that takes a single character and a number as parameters and displays an ASCII art pyramid to the screen with number rows:

def pyramid(char,rows):
    for i in range(rows+1):
        print(char*i)

# def pyramid2(char,rows):
#     if rows <= 0:
#         return
#     print(char*(rows-))
#     print(pyramid2(char,rows-1))


def absolute_difference(num1, num2):
    return abs(num1 - num2)


def is_even(number):
    return number%2 == 0

def calculate_total(meal,tax_rate,tip_rate):
    tip = meal*tip_rate
    tax = meal*tax_rate
    return meal+tip+tax

def calculate_total2(meal,tax_rate,tip_rate):
    return meal +  sum(factor*meal for factor in [tax_rate,tip_rate])

def hey(num):
    return num**2

def there(n):
    if n < 0:
        return 0
    return 2**n

def are_we(num,word):
    for time in range(num):
        print("Are we " + word + " yet ?")




def main():
    pyramid("*",2)
    pyramid("+",5)
    pyramid("X",10)

    print(absolute_difference(5,10) == 5)
    print(absolute_difference(10,5) == 5)
    print(absolute_difference(200, -200) == 400)
    print("*"*10)

    print("Is even: ", is_even(97))
    print("Total cost of meal: ", calculate_total2(53.48,.07,.18))

    print(hey(5))
    print(hey(0))
    print(hey(-3))
    print("*" * 10)

    print(there(5))
    print(there(0))
    print(there(3))
    print(there(-2))
    print(there(-6))

    are_we(2, "there")
    are_we(3, "50")
    are_we(1, "")
    are_we(0, "hey")


    list = ['h','e','l','l','o','!']
    print(list[:4])





main()