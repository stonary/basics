''' 0.3 dictionary '''

# ways to initialize dictionary
d1 = {0: '0', 1: 'a', 2:'b', 3:'c'}
d2 = dict(['0', 'a', 'b', 'c'].__iter__())
d3 = dict(d1)
#d4 = dict(one='0', two='a',three='b', four='c')

assert d1 == d2
assert d2 == d3
#assert d3 == d4