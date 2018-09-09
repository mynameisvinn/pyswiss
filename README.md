# pyswiss
treat s3 as a python object store.

## example
we want to save `v`, an object.
```python
class Person():
    def __init__(self, name):
        self.name = name
        
v = Person("vin")
```
to put an object, do
```python
from pyswiss import PySwiss

client = PySwiss(bucket="mynameisvinn-111")
client.put(v, "some_key")
```
to get an object, do
```python
my_object = client.get("some_key")
print(my_object.name)  # prints "vin"
```