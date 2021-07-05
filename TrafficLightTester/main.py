import re

f = open("Input/blink.txt", "r")
Lines = f.readlines()

data = []
decreasing = False
last = ""


for count,line in enumerate(Lines):
    #Regex which only allows numbers
    lin = re.sub("[^0-9]", "", line)
    #Skipping same values
    if (last == lin):
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
        last = element  

print(*data, sep = "\n")

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
            print("Invalid red light at {} transaction".format(i))
        decreasing = True
    elif(data[i] == '0100'):
        if(data[i-1] =='1000' and decreasing):
            continue
        elif(data[i-1] == '0010' and not decreasing):
            continue
        elif(data[i-1] == '0000' and not decreasing):
            continue
        else:
            print("Invalid yellow light at {} transaction".format(i))
    elif(data[i] == '0010'):
        if(data[i-1]=='0100' and decreasing): 
            pass
        elif(data[i-1]=='0000'): 
            pass
        elif(data[i-1]=='0001'): 
            pass
        else:
            print("Invalid green light at {} transaction".format(i))
        decreasing = False
    elif(data[i] == '0001'):
        if(data[i-1]=='0100'): 
            continue
        elif(data[i-1]=='0000' and decreasing): 
            continue
        else:
            print("Invalid green arrow light at {} transaction".format(i))
    elif(data[i] == '0000'):
        if(data[i-1]=='0001'): 
            continue
        elif(data[i-1]=='0010'): 
            continue
        elif(data[i-1]== '0100' and decreasing):  #ONLY IF IT IS POSSIBLE AFTER YELLOW TO SEE BLINKING IMMEDIATELY
            continue
        else:
            print("Invalid blinking at {} transaction".format(i))
    else:
        print("Error in data file, value: {} is not applicaple".format(data[i]))