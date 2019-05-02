# Open the file
with open("mydata2.txt", encoding="utf-8") as myFile:
    lineNum = 1

    # We'll use a while loop that loops until the data
    # read is empty
    while True:
        line = myFile.readline()

        # line is empty so exit
        if not line:
            break
        print('Line', lineNum)
        wordList = line.split()
        print('Number of words: ', len(wordList))


        #print("Line", lineNum, " :", line, end='')


        lineNum += 1

