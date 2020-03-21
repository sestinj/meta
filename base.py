#Imports
import sys
import os
import subprocess

#Variables
fileExtensions = {'python3':'.py', 'python2':'.py', 'javascript':'.js', 'java':'.java', 'c':'.c', 'c++':'.cpp'}

#Functions
#Create a file with all data to be read by target language
def makeInputFile()

#Convert params from lang1 (source) to lang2 (target)
#Whenever switching between languages, create a variables text file formatted with each line like [type]: [value] e.g. string: "I am a string."
def convert(params, source, target):
    #The code to do this will be in the target language always
    if target=="python3":
        if source=="javascript":
            
    elif target=="javascript":
        if source=="python3":

def executeFile(name, lang):
    if lang=="python3":
        subprocess.getoutput("python3 " + name)
    elif lang=="python2":
        subprocess.getoutput("python2 " + name)
    elif lang=="c":
        subprocess.getoutput("gcc " + name)
    elif lang=="c++":
        subprocess.getoutput("g++ " + name)
    else:
        print("Unsupported language: " + lang)

#Run
fileName = sys.argv[1]
read = open(fileName, 'r')

fileNumber = 0
currentLang = "python"
currentFile = open(currentLang+str(fileNumber)+fileExtensions[currentLang], "w")

while True:
    line = read.readline()
    if not line:
        break
    
    if "#" == line.strip()[0] and ">" == line[len(line)]:
        line = line.strip()
        lang = line[2:line.index("(")]
        params = line[line.index("(")+1:line.index(")")].split(",")
        
        convert(params, )
        currentLang = lang
        fileNumber += 1
        currentFile = open(currentLang+str(fileNumber)+".txt", "w")

    elif "<" == line.strip()[0] and "#" == line[len(line)]:
        currentFile.close()
        #Run the current file.
        executeFile(currentFile.name, lang)

    else:
        currentFile.write(line + "\n")

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