import os

with open("mydata.txt", 'w', encoding='utf-8') as myFile:
    myFile.write("Some random text\nMore random text\nAnd some more")


with open("mydata.txt", encoding='utf-8') as myFile:
     print(myFile.read())


os.rename('mydata.txt', 'mydata2.txt')

