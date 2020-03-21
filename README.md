# meta
Meta is a compiler that allows code from any language to be combined. This could be all together in a single .meta file or natively, using the meta SDK.

Using a .meta file:
```
#javascript()>

const f = (a, b) => {
    #>python(a, b)
    c = a + b
    <(c)#
    return c;
}
<()#
```


Using the SDK in Python:
```python
from sdk import meta

old = "this is a string"
print(meta("const new = old.substr(0, 2);", "javascript", {"old":old}, ["new"]))
```