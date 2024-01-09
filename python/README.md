# Python fundamentals

## for loop
### 1. Use `range(start, stop[, step])` to loop within a certain range.
* `start`: the index the loop starts from. Defualt is `0`
* `stop`: range will loop till `stop` but not including `stop` value
* `step`: interval of the loop. Default is `1`

Forward looping from index `0` to `len(nums)-1`.
```python
# idx:  0, 1, 2, 3
nums = [1, 2, 3, 4]

for idx in range(len(nums)):
    print(idx)

# 0
# 1
# 2
# 3
```

Backward looping from index `len(nums)-1` to `0`.
```python
# idx:  0, 1, 2, 3
nums = [1, 2, 3, 4]

for idx in range(len(nums)-1, -1, -1):
    print(idx)

# 3
# 2
# 1
# 0
```

### 2. Use `enumerate(sequence, [start=0])` to loop with index as well as value.
* `sequence`: any object that supports iteration
* `start`: the starting index of the loop

```python
l1 = ["eat", "sleep", "repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

    # (0, 'eat')
    # (1, 'sleep')
    # (2, 'repeat')
 
# changing index and printing separately
for count, ele in enumerate(l1, 100):
    print (count, ele)

    # 100 eat
    # 101 sleep
    # 102 repeat
 
# getting desired output from tuple
for count, ele in enumerate(l1):
    print(count)
    print(ele)

    # 0
    # eat
    # 1
    # sleep
    # 2
    # repeat
```

## collections.defaultdict()
The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.
```python
# When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.
from collections import defaultdict

d = defaultdict(list)
  
for i in range(5):
    d[i].append(i)

print(d)
# defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

# print keys of the dict
print(d.keys())
# [0, 1, 2, 3, 4]

# print values of the dict
print(d.values())
# {[0], [1], [2], [3], [4]}
```

In Dictionary, the key must be unique and **immutable**. This means that a Python Tuple can be a key whereas a Python List can not.
```python
from collections import defaultdict
d = defaultdict(str)

# if we want to store a list coordinate as dict key & str as value: {[(0,1)]: "somevalue"}
coordinate = [0,1]

d[coordinate] = "somevalue" # return error: TypeError: unhashable type: 'list'

d[tuple(coordinate)] = "somevalue" # convert list to tuple works. b/c tuple is immutable

print(d)
# defaultdict(<class 'str'>, {[1, 0]: "somevalue"})

# print keys of the dict
print(d.keys())
# [[(1, 0)]]

# print values of the dict
print(d.values())
# {["somevalue"]}
```

## Alphabet Tricks
### alphabet char counter
```python
# count char with array
count = [0] * 26

for c in "apple":
    count[ord(c) - ord('a')] += 1
print(count)

#  a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z 
# [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0]
```
### reverse string
```python
ans = "apple"
ans[::-1] # "elppa"

# compare palindrome
return ans == ans[::-1]
```

### check if char is alphanumeric
```python
c = 'a'
return c.isalpha()
# True

n = '1'
return n.isdigit()
# True

c = 'A1'
return c.isalnum()
# True
```

## sort list
```python
nums = [1, 2, 3, 4]
nums.sort() # in-place sorting

res = sorted(nums) # returns a sorted list
```