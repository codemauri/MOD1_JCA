def readfile():
    FILENAME="readfile.dat"
    dataFile = open(FILENAME, "r")
    line = dataFile.readline()
    while line != "":
        line = line.rstrip()
        print("-"+line)
        line = dataFile.readline()
    dataFile.close()

def writefile():
    prompt1 = "What is the name of the file ?: "
    prompt2 = "Please enter a number:"
    filename = input(prompt1)
    datafile = open(filename, "w")
    num = int(input(prompt2))
    while num != 0:
        print(num, file=datafile)
        num = int(input(prompt2))
    datafile.close()






def main():
    #readfile()
    writefile()

main()


