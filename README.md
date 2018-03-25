# pyswiss
Easily put/get python objects in s3

## Usage
To save an object `v`
```python
class Person():
    def __init__(self, name):
        self.name = name
        
v = Person("vin")
```
Save it with pyswiss
```python
from pyswiss import Pyswiss
client = Pyswiss()
client.put(v, "mynameisvinn", "obj")  # use your own bucket/keys
```
Retrieve the object
```python
my_object = client.get("mynameisvinn", "obj")
print(my_object.name)  # prints "vin"
```
