def main():
    out=open("test.txt","a")
    out.write(" \nname:sudha")
    out.write(" \nname:Ramya")
    out.close()
    readFile=open("test.txt","r")
    for line in readFile:
        print(line)
    readFile.close()



if __name__ == '__main__':main()
