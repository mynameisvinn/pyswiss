# pyswiss
easily put/get python objects in s3, no fuss.

## example
we want to save `v`, an object.
```python
class Person():
    def __init__(self, name):
        self.name = name
        
v = Person("vin")
```
lets save it with pyswiss.
```python
from pyswiss import Pyswiss
client = Pyswiss()
client.put(v, "mynameisvinn", "obj")  # use your own bucket/keys
```
retrieve python object.
```python
my_object = client.get("mynameisvinn", "obj")
print(my_object.name)  # prints "vin"
```