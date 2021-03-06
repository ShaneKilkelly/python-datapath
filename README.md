# python-datapath

Use [JSONPath](http://goessner.net/articles/JsonPath/)
like strings  to **get and set** values in a deeply nested data structure 
with graceful retrieval if the structure does not exist and
[autovivification](https://en.wikipedia.org/wiki/Autovivification) when setting
values.

Inspired by, but not completely compliant with the [JSONPath specification]
(http://goessner.net/articles/JsonPath/)

Why should I use this library?
------------------------------

**YOU REALLY SHOULDN'T** - This is nowhere near ready to be used yet!

`datapath` lets you:

 * Get values from deeply nested structures without caring if any of the 
 intermediate keys exist
 * Set values into data structures and have all intermediate values created 
 for you
 * Turn deeply nested structures into flat dicts and back
 

Compact paths
-------------

The `datapath` library supports compact paths which cut a small amount of the 
verboseness of the full JSONPath spec. A number of simplifying assumptions 
are made:
  
 * All paths are local
 * 'Naked' paths without a prefix are assumed to be dict keys
 * Bracked paths are assumed to be on the local object
 
Examples:

| JSONPath | `datapath` equivalents |
| -------- | -----------------------|
| $.a      | a, .a, ["a"], ['a']    |
| $.[7]    | [7]                    |
| $.*      | *, .*                  |
| $..a     | ..a                    |
| @..a     | ..a                    |
| @.a      | a, .a, ["a"], ['a']    |

The JSONPath spec suggest `'@.'` for local anchoring and `'$.'` for root 
anchoring. Where anchoring is not specified or relevant datapath allows the 
omission of the leading identifiers for example:

| JSONPath | `datapath` compact  |
| -------- | ------------------- |
| $.a, | a |                     |
| @.a | a  |                     |
| $.['a']  | a                   |
| @.['a']  | a                   |
| $.["a"]  | a                   |
| @.["a"]  | a                   |

**NOTE!** - Currently `datapath` doesn't allow anchoring markers

Escaping
--------

You can set a key with a dot, or any other reserved character by escaping it:

```python
from datapath.crud import get_path
 
print get_path('a\\.b', {'a.b' : 5})  # 5!
```

Compliance levels
-----------------

The `datapath` library does not support the following parts of JSONPath at the
moment:

 * List slices
 * Selectors beyond `'*'` - no ability to do things like `book[author='lily']`
 * Anchoring specifications: `'@.'`, `'$.'`

Enough talking!
---------------

```python
from datapath.crud import get_path, find_path, set_path

data = {
    'a': ['hello', 'world'],
    'b': 5
}
    
print get_path(data, 'a')     # ['hello', 'world']
print get_path(data, 'a[0]')  # 'hello'

find_path(data, '*.*')      # [['hello', 'world'], 5]

set_path({}, 'not_there[4].more', 'value')
# {'not_there': [None, None, None, {'more': 'value'}]}
```
    
Known issues
------------

 * This library doesn't work, and using it is a fools errand
 * Attempting to set recursive paths (e.g. 'a..b') doesn't work
 * Recursive paths in general are likely to have undefined behavior
  
