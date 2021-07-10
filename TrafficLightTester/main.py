import re
import sys

##########################################################################################################################################################

def openFile(file):
    try:
        f = open("{}".format(file), "r")
        Lines = f.readlines()
        return Lines
    except IOError:
        exit("File not found!")

##########################################################################################################################################################

def getFileName():
    if (len(sys.argv) != 2):
        file = input("Specify the data file \n")
        Lines = openFile(file)
    else:
        Lines = openFile(sys.argv[1])
    return Lines

##########################################################################################################################################################

def fixInput(Lines):
    data = []
    amount = []
    last = ""
    counter = 1
    # - Jei buvo seka, kurios pabaigoje šviesoforas tiesiog pradėjo šviesti viena spalva, programa neidentifikuoja klaidos

    for count,line in enumerate(Lines):
        #Regex which only allows numbers
        lin = re.sub("[^0-9]", "", line)
        #Skipping same values
        if (last == lin):
            counter = counter + 1
            continue
        #Skiping empty lines
        elif (lin == ""):
            print("Empty line in file at index {}".format(count))
            continue
        #Skiping different lenght values
        elif (len(lin) != 4):
            print("Bad input length at line {}".format(count))
            continue
        else:
            element = lin
            data.append(element)
            # print(counter)
            amount.append(counter)
            counter = 1
            last = element
    if (len(data) == 1):
        exit("Single light color present in file")
    if (len(data) == 0):
        exit("File is Empty")
    del amount[0]
    return data, amount 

##########################################################################################################################################################

def getErrorLine(j, amount):
    errorLine = 1
    i = 0
    while (i < j):
        errorLine= errorLine + amount[i]
        i = i + 1
    return errorLine

##########################################################################################################################################################

def CheckErrors(data, amount):
    decreasing = False

    #Check if the values starts decreasing 
    if (int(data[0]) > int(data[1])):
        if (data[1] == '0000'):
            decreasing = False
        else:
            decreasing = True

    for i in range(1, len(data)):
        if (data[i]  == '1000'):
            if(data[i-1]=='0100' and not decreasing):
                pass
            else:
                print("Invalid red light at {} transaction".format(getErrorLine(i,amount)))
            decreasing = True
        elif(data[i] == '0100'):
            if(data[i-1] =='1000' and decreasing):
                continue
            elif(data[i-1] == '0010' and not decreasing):
                continue
            elif(data[i-1] == '0000' and not decreasing):
                continue
            else:
                print("Invalid yellow light at {} transaction".format(getErrorLine(i,amount)))
        elif(data[i] == '0010'):
            if(data[i-1]=='0100' and decreasing): 
                pass
            elif(data[i-1]=='0000'): 
                pass
            elif(data[i-1]=='0001'): 
                pass
            else:
                print("Invalid green light at {} transaction".format(getErrorLine(i,amount)))
            decreasing = False
        elif(data[i] == '0001'):
            if(data[i-1]=='0100'): 
                continue
            elif(data[i-1]=='0000' and decreasing): 
                continue
            else:
                print("Invalid green arrow light at {} transaction".format(getErrorLine(i,amount)))
        elif(data[i] == '0000'):
            if(data[i-1]=='0001'): 
                continue
            elif(data[i-1]=='0010'): 
                continue
            elif(data[i-1]== '0100' and decreasing):  #ONLY IF IT IS POSSIBLE AFTER YELLOW TO SEE BLINKING IMMEDIATELY
                continue
            else:
                print("Invalid blinking at {} transaction".format(getErrorLine(i,amount)))
        else:
            print("Error in data file, value: {} is not applicaple".format(getErrorLine(i,amount)))

##########################################################################################################################################################

Lines = getFileName()
data, amount = fixInput(Lines)
CheckErrors(data, amount)

# print(*Lines, sep = "")
# print(*amount, sep = "\n")
# print(*data, sep = "\n")
