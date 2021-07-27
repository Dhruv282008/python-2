f = open("text.txt")
f.read()

fileLines = f.readlines()

for line in fileLines:
    print(line)

def greet(name):
    print("Hello"+name)

greet("dhruv")

def countwordsfromfile():
    fileName = input("Enter the file name : ")
    file = open(fileName, "r")
    noOfwords = 0
    for i in file:
        words = i.split()
        noOfwords = noOfwords + len(words)
    print(noOfwords)

countwordsfromfile()