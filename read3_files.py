def numberLinesFile():
    filenames = ["text1.txt","text2.txt","text3.txt"]
    writefile = "counts1.txt"
    datafile = open(writefile, "w")
    for file in filenames:
        dataFile = open(file, "r")
        line = dataFile.readline()
        count = 0
        words = 0
        while line != "":
            words += len(line.split())
            count += 1
            line = dataFile.readline()
        dataFile.close()
        print(file, ":", count, file=datafile)
    datafile.close()

def numberLinesFile2():
    filenames = ["text1.txt","text2.txt","text3.txt"]
    writefile = "counts2.txt"
    datafile = open(writefile, "w")
    totalwords = 0
    totalines = 0
    for file in filenames:
        dataFile = open(file, "r")
        line = dataFile.readline()
        count = 0
        words = 0
        while line != "":
            words += len(line.split())
            count += 1
            line = dataFile.readline()
        totalwords += words
        totalines += count
        dataFile.close()
        print(file, ":", count, "lines,", words, "words",file=datafile)
    print("TOTAl:",totalines,"lines,",totalwords,"words",file=datafile)
    datafile.close()

def main():
    numberLinesFile()
    numberLinesFile2()

main()




