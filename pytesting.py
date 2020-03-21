from sdk import meta

old = "this is a string"
print(meta("const new = old.substr(0, 2);", "javascript", {"old":old}, ["new"]))