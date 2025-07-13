def header(text, surround):
    print(surround * (len(text) + 4) )  # display top line
    print(surround, text, surround)  # display middle line
    print(surround * (len(text) + 4) ) # display bottom line


def main():     # execution begins here
    header('Hello, World!', '*')
    header('Python Rocks', '!')
    header('Coders 4 EVER', '+')

main()