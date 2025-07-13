#Wriring Lists
#Mauricio Florez

def  numbers_avg():
    numbers = []
    for i in range(20):
        numbers.append(float(input("Please enter 20 numbers: ")))
    return sum(numbers)/len(numbers)


def mangle(string):
    phrase = []
    for letter in string:
        phrase.append(letter)
    del phrase[2]
    del phrase[-3]
    return "".join(phrase).upper()


def count_e(strings):
    count = 0
    for string in strings:
        string = string.lower()
        if "e" in string:
            count = count + string.count("e")
    return count


def count_vowels(strings):
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for string in strings:
        string = string.lower()
        for ch in vowels:
            count = count + string.count(ch)
    return count








def main():
    #print(numbers_avg())
    # print(mangle("hellothere"))
    # print(mangle("42 degrees Celsius"))
    # print(mangle("eeeeeee"))
    print(count_e(["hi", "hello", "EEK!"]))
    print(count_vowels(["hi", "hello", "OOF!"]))




main()



