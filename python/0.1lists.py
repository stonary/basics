'''0.1 lists'''

# creation
l1 = list()
l2 = []

if l1 == l2:
    print "comparision by value"
else:
    print "comparision by address"
    

# answer: comparision by value

if l1 is l2:
    print "comparision by value"
else:
    print "comparision by address"
    

# list operations:
help(list)

l1.append(1)
l1.append('a')
l1.append(l2)

assert l1.count(l2) == 1
l2.append('a')
l1.extend(l2)

assert l1.count('a') == 2
# notice the append is by pointer
assert l1.count(l2) == 1 

l1.append(l2)
assert l1.index(l2) == 2 # first index

l1.insert(0, l2)
assert l1.index(l2) == 0 # insert before index

assert l1.pop() == l2
assert l1.pop(0) == l2

l1.remove(l2)
assert l1.count(l2) == 0

try:
    l1.remove('b')
except ValueError:
    print "I said there was no b"
    
# reverse in place
assert  l1.reverse() == None 
assert l1[-1] == 1

assert l1.sort() == None # in place again

assert str(l1) == l1.__repr__()

# iterator 
iterator = l1.__iter__()
for i in l1:
    assert i == iterator.next()

try:
    iterator.next()
except StopIteration:
    print "no more..."

# reverse iterator    
reverse_iterator = l1.__reversed__()

for i in range(len(l1)):
    assert reverse_iterator.next() == l1[-i - 1]
try:
    reverse_iterator.next()
except StopIteration:
    print "yeah, no more.."
finally:
    print "I always get executed"

### map, filter, reduce ##
l = [1, 2, 3, 4, 5]
 

assert map(lambda x: x**2, l) == [ i**2 for i in l]
assert filter(lambda x: x%2==0, l) == [2, 4]

def add_two(x, y):
    return x + y

assert reduce(add_two, l) == sum(l)

# list comprehensions #
print [(x, y, z) for x in l for y in l for z in l if x + y == z]





