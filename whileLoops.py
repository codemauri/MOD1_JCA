

def aWhile():
    i=1
    while i < 6:
        print(i)
        i += 1

def bWhile():
    i=2
    while i < 12:
        print(i)
        i += 3

def cWhile():
    i=-10
    accu = ""
    while i < 1:
        if i == 0:
            accu += str("-"+ str(i))
        else:
            accu += str(i)
        #print(i)
        i += 2
    print(accu)

def cSolution():
    y = -10
    while y <= 0:
        print(y, end=" ")
        y += 2
    print()

def dWhile():
    i=0
    while i < 4:
        print("****")
        i += 1

def divider():
    print("*"*10)


def while2():
    i = 0
    string = "CSI 150"
    while i < len(string):
        print(string[i])
        i += 1

def listNumbers():
    numbers = []
    prompt = "Please enter a number ('0' to finish): "
    response = eval(input(prompt))
    while response != 0:
        numbers.append(response)
        response = eval(input(prompt))
    print ("LIST: ", sorted(numbers))
    print("SUM is :", sum(numbers))
    print("AVG is: ", sum(numbers)/len(numbers))


def average_neg_evens(numbers):
    numbers_sorted = sorted(numbers)
    idx = 0
    sum = 0
    num = 0
    while numbers_sorted[idx] < 0:
        if numbers_sorted[idx] % 2 == 0:
            sum += numbers_sorted[idx]
            num += 1
        idx += 1
    return sum/num


def count_letter(strings, letter):
    idx = 0
    num = 0
    letter_base = letter.lower()
    while idx < len(strings):
        for letter in strings[idx].lower():
            if letter == letter_base:
                num += 1
        idx += 1
    return num

def count_letter2(strings, letter):
    num = 0
    letter = letter.lower()
    for string in strings:
        num += string.lower().count(letter)
    return num













def main():
        aWhile()
        divider()
        bWhile()
        divider()
        #cWhile()
        cSolution()
        dWhile()
        divider()
        while2()
        divider()
        #listNumbers()
        print(average_neg_evens([0, 1, 2, -2, -3, -4, 3, 4]) == -3)
        words = ["HELLO", "goodbye", "1234 Oooh!"]
        print(count_letter(words, "o") == 6)
        print(count_letter2(words, "o") == 6)


main()

