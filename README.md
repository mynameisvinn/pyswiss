# pyswiss
treat s3 as a python object store.

## install
```
git clone https://github.com/mynameisvinn/pyswiss
cd pyswiss
```

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

client = PySwiss(bucket="mynameisvinn-111")  # use your own bucket
client.put(v, "some_key")
```
to get an object, do
```python
my_object = client.get("some_key")
print(my_object.name)  # prints "vin"
```