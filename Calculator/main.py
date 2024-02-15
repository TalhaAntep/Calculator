
f = open("output.txt",'w') 

operatorList= ["**","*","//","/","%","+","-","<",">","==","!=","!"]
operatorParts= ["!","="]
numberList = ["0","1","2","3","4","5","6","7","8","9"]
breaks = [" ","\n"]

def main():
    file= open("input.txt", "r")
    
    for line in file:
        if(line.startswith("\n")):
            f.write("\n")
        else:
            whiteSpaceFlag=True
            for x in line:
                if(not(x==" " or x=="\n")):
                    parseAndEvaluate(line)
                    whiteSpaceFlag=False
                    break
            if(whiteSpaceFlag):
                f.write("\n")


def parseAndEvaluate(expression):
    elements=[]
    temp = ""
    numberFlag=False
    operatorFlag=False
    errorFlag=False
    for x in expression:

        

        if x in numberList:
            if(operatorFlag):
                elements.append(temp)
                temp=""
                operatorFlag=False
            temp=temp+x
            numberFlag=True
        elif x in operatorList or x in operatorParts:
            if(numberFlag):
                elements.append(int(temp))
                temp=""
                numberFlag=False
            temp=temp+x
            operatorFlag=True
        elif x in breaks:
            if(numberFlag):
                elements.append(int(temp))
                temp=""
                numberFlag=False
            if(operatorFlag):
                elements.append(temp)
                temp=""
                operatorFlag=False
        else:
            errorFlag=True
            break
    
    
    
    if(errorFlag):
        f.write("ERROR\n")
    else:
        for x in elements:
            if(not(x in operatorList or isinstance(x, int))):
                f.write("ERROR\n")
                return -1
        try:
            evaluate(elements)
        except:
            f.write("ERROR\n")

def evaluate(elements):
    if("**" in elements):
        i = elements.index("**")
        result = elements[i-1]**elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("*" in elements):
        i = elements.index("*")
        result = elements[i-1]*elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("//" in elements):
        i = elements.index("//")
        result = elements[i-1] // elements[i+1]
        if(elements[i+1]==0):
            f.write("ERROR\n")
            return -1
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("/" in elements):
        i = elements.index("/")
        if(elements[i+1]==0):
            f.write("ERROR\n")
            return -1
        result = elements[i-1] / elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("%" in elements):
        i = elements.index("%")
        result = elements[i-1] % elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("+" in elements):
        i = elements.index("+")
        result = elements[i-1]+elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("-" in elements):
        i = elements.index("-")
        result = elements[i-1]-elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("<" in elements):
        i = elements.index("<")
        result = elements[i-1]<elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif(">" in elements):
        i = elements.index(">")
        result = elements[i-1]>elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("==" in elements):
        i = elements.index("==")
        result = elements[i-1]==elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result
    elif("!=" in elements):
        i = elements.index("!=")
        result = elements[i-1]!=elements[i+1]
        elements.pop(i+1)
        elements.pop(i)
        elements[i-1] = result

    if(len(elements)>1):
        evaluate(elements) 
    else:
        f.write(str(elements[0]) + "\n")


def factorial(number):
    result = 1
    for x in range(1,number+1):
        result = result * x
    return result

main()