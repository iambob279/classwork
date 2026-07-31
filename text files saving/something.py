# Files and exceptions

# Subroutine to write data to a text file
def WriteData():
    FileName = "program data.txt"
    TextFile = open(FileName,"w")
    for i in range(10):
        TextFile.write(str(i) + " An item of data\n")
    TextFile.close()

# Subroutine to read data from a text file
def ReadData():
    FileName = "program data.txt"
    TextFile = open(FileName,"r")
    Data = " "
    while Data:
        Data = TextFile.readline().strip()
        print(Data)
    TextFile.close()
    print(f'**{Data}***')

WriteData()
ReadData()