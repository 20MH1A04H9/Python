import  re
def main():

    readFile=open("regFile.txt","r")
    for line in readFile:
        if re.search("(Sai|R)na",line):
         print(line)
    readFile.close()



if __name__ == '__main__':main()
