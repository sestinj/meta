from sdk import parse_javascript, makeTransferFile
d = parse_javascript('input.txt')
for key in d.keys():
    vars()[key] = d[key]
c = a + b
makeTransferFile({'c':vars()['c']})