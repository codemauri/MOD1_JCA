def poem():
    noun = input("Please enter a plural noun: ")
    adjective = input("Please enter an adjective: ")
    print(noun.title(), "are red,", "violets are blue")
    print("Monty Python is", adjective.lower(), ", woo hoo!")



if __name__ == '__main__':
    poem()