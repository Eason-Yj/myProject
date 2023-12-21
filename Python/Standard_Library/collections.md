# collections

## defaultdict
```pytho1
from collections import defaultdict
 
d1 = defaultdict(list) #list backed multidict
d1['key1'].append(1)
d1['key2'].append(2)
defaultdict(<class 'list'>, {'c1': [1], 'c2': [2]})
 
d2 = defaultdict(set) #set backed multidict
d2['key1'].add(1) 
d2['key2'].add(2)
defaultdict(<class 'set'>, {'c1': {1}, 'c2': {2}})

```