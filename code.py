from sdk import parse, makeTransferFile
d = parse(javascript, 'input.txt')
for key in d.keys():
    vars()[key] = d[key]

makeTransferFile({'c':vars()['c']})