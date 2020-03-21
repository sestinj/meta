from sys import argv
from os import rename
import subprocess


#e.g.) python3 run.py transfer.txt javascript python code.py c d e
inputFileName = argv[1]
source = argv[2]
target = argv[3]
codeFile = open(argv[4], 'r')
outputs = argv[5:]

code = open("new.txt", "w")

#This puts together all of the code to parse the input, add the vars to the scope, run the given code, the make an output file.
if target == "python3":
    code.write("from sdk import parse, makeTransferFile\n")
    code.write("d = parse("+source + ", '" + inputFileName + "')\n")
    code.write("for key in d.keys():\n")
    code.write("    vars()[key] = d[key]\n")
    code.write(codeFile.read())
    codeFile.close()
    outputDict = "{"
    for name in outputs:
        outputDict += "'%s':vars()['%s']," % (name, name)
    outputDict = outputDict[:len(outputDict)-1] + '}' #Replaces extra last comma with closing bracket
    code.write("\nmakeTransferFile(" + outputDict + ")")
    code.close()
    rename(code.name, codeFile.name)

    subprocess.run("python3 " + codeFile.name, shell=True)

elif target == "javascript":
    code.write("""const sdk = require('./sdk');
    var d = sdk.parse('%s', '%s');
    for (key of Object.keys(d)) {
        eval(`${key} = d['${key}'];`);
    }
    """ % (source, inputFileName))

    code.write(codeFile.read())
    codeFile.close()

    outputDict = "{"
    for name in outputs:
        outputDict += "'%s':%s," % (name, name)
    outputDict = outputDict[:len(outputDict)-1] + '}' #Replaces extra last comma with closing bracket
    code.write("\nsdk.makeTransferFile(" + outputDict + ");")
    code.close()
    rename(code.name, codeFile.name)

    subprocess.run("node " + codeFile.name, shell=True)
    #THIS IS WHERE I LEFT OFF. SHOULD PROBABLY SWITCH THE ABOVE TO MULTILINE STRINGS.