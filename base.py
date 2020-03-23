#Imports
from sys import argv
from os import rename

#Utility Functions
def replaceLines(file, start:int, end:int, replacement:str):
    if not file.closed:
        file.close()
    file = open(file.name, "r")
    newFile = open("newFile"+file.name.split('.').pop(), 'w')
    
    i=0
    while True:
        line = file.readline()
        if i < start:
            newFile.write(line)
        elif i == start:
            newFile.write(replacement)
        elif i > end:
            if not line:
                break
            else:
                newFile.write(line)
        i+=1
    
    file.close()
    newFile.close()
    rename(newFile.name, file.name)

def createSDKCall(code:str, source:str, target:str, inputs:list, outputs:list):
    inputDict = "{"
    for i in inputs:
        i=i.strip() #remove extra spaces before variables
        inputDict += "'%s':%s, " % (i, i)
    if len(inputs):
        inputDict = inputDict[:len(inputDict)-1] + "}"
    else:
        inputDict += "}"
    
    if source == "python3":
        #Call meta, then retrieve the variables called by it
        return """from sdk import meta
__d__=meta('''%s''', '%s', %s, %s)
for key in __d__.keys(): exec(key + ' = __d__[' + key + ']')
""" % (code, target, inputDict, str(outputs))
    
    elif source == "javascript":
        return """const meta = require('./sdk').meta
__d__=meta(`%s`, '%s', %s, %s);
for (key of Object.keys(__d__)) { eval(key + ' = __d__[' + key + ']'); }
""" % (code, target, inputDict, str(outputs))


#Recursively replaces meta blocks with SDK code
def replaceMETA(metaFile):
    #Close and reopen to be sure you are at the first line of the file (even though it should always be closed from the replaceLines function right before replaceMETA is recursively called)
    if not metaFile.closed:
        metaFile.close()
    metaFile = open(metaFile.name, 'r')

    lastLang = "python3"
    currentLang = "python3"
    codeLines = ""
    beginningLine = 0
    endingLine = 0
    inputs = []
    outputs = []


    i=0
    while True:
        line = metaFile.readline()
        if not line:
            metaFile.close()
            break #When the last line of the file is reached, we know that no more blocks are left unreplaced and the function is left to return
        
        if line.strip().startswith("#") and line.strip().endswith(">"):
            line = line.strip()
            lastLang = currentLang
            currentLang = line[1:line.index("(")]
            codeLines = ""
            inputs = line[line.index("(")+1:line.index(")")].split(",")
            if '' in inputs: inputs.remove('') #This remove is for when there are no specified inputs so it is [] instead of [''] which causes other problems
            beginningLine = i
            

        elif line.strip().startswith("<") and line.strip().endswith("#"):
            line = line.strip()
            outputs = line[line.index("(")+1:line.index(")")].split(",")
            if '' in outputs: outputs.remove('')
            endingLine = i

            sdkCall = createSDKCall(codeLines, lastLang, currentLang, inputs, outputs)
            replaceLines(metaFile, beginningLine, endingLine, sdkCall)
            replaceMETA(metaFile)
            break

        else:
            codeLines += line
        
        i+=1


fileName = argv[1]
metaFile = open(fileName, 'r')
replaceMETA(metaFile)
#For nested language tags, there doesn't need to be a totally separate implementation
#of this parser, but there needs to be a way to run any other language inside of each
#other language, which basically just means there needs to be a way to get os like in
#python. So like in node.js, it would make a new child process for the python sub-tag
#and run it with this same parser.


#Scope (global, dir())
#Output (console.log, print)
#async
#keywords like return inside a function of another language

#In the file, the input and output values of each tagged section need to be specified

#Should also be able to just specify a file, so this can be more module instead of
#encouraging massive files