# meta
Meta is a compiler that allows code from any language to be combined. This could be all together in a single .meta file or natively, using the meta SDK.

```python
from sdk import meta

old = "this is a string"
print(meta("const new = old.substr(0, 2);", "javascript", {"old":old}, ["new"]))
```