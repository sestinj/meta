from subprocess import run
from functools import reduce

delimiter = ":"
fileEndings = {'javascript':'js'}

def meta(code:str, lang:str, input:dict, output:list):
    #1) Make codefile
    codeFile = open("code." + fileEndings[lang], 'w')
    codeFile.write(code)
    codeFile.close()
    #2) Make transfer file
    makeTransferFile(input)
    #3) Run execute with run.py
    if output:
        #Can't reduce an empty array
        outputArgs = reduce(lambda a,b:a+b+" ",output)
    else:
        outputArgs = ""
    print(run("python3 run.py transfer.txt python3 %s code.%s %s" % (lang, fileEndings[lang], outputArgs), shell=True))
    #4) Parse output
    return parse(lang, "transfer.txt")

def convert(lang:str, typ:str, data:str):
    if lang == "javascript":
        if typ == "string":
            return data
        elif typ == "number":
            if "." in data:
                return float(data)
            else:
                return int(data)

def parse(lang:str, filename:str):
    #Takes input file and outputs dictionary of converted variables
    variables = {}

    input = open(filename, 'r')
    while True:
        line = input.readline()
        if not line:
            break

        components = line.split(delimiter)
        name = components[0]
        typ = components[1]
        data = components[2]
        if not name == '': #Don't make a ghost variable for extra blank lines
            variables[name] = convert(lang, typ, data)
    
    return variables #Need to figure out how to get this into the globals() of code.py

def makeTransferFile(variables):
    #variables is a dictionary
    out = open("transfer.txt", 'w')
    i=0
    for key in variables.keys():
        val = variables[key]
        if i != 0:
            out.write("\n")
        out.write(key + ":" + str(type(val)).strip("<class ").strip("'>") + ":" + str(val))
        i+=1
    out.close()