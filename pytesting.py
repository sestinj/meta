from sdk import meta

old = "this is a string"
print(meta("const neww = old.substr(0, 2);", "javascript", {"old":old}, ["neww"]))