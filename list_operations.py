farts = ['gooey', 'sticky', 'moist']
print(farts)

# removing items from a list #

# del keyword
# this goes //before// the list, and operates on objects, not just lists
del farts[1]
print(farts)

# pop() method
# exclusive to lists, removes & returns specified element, default -1
x = farts.pop()
print(farts)
print(x)

# remove() method
# exclusive to lists, removes first occurrence of specified value
farts.remove("gooey")
print(farts)

# adding items to a list #

# append() method
# exclusive to lists, adds element to end of list
farts.append('dry')
farts.append('mossy')
print(farts, 'this is appended')

# insert() method
# exclusive to lists, inserts element at specified position
farts.insert(1, 'windy')
farts.insert(2, 'smelly')
print(farts, 'this is inserted\n')

# list organization #

# sort() method
# exclusive to lists, sorts the list in-place, default ascending
fartsOrig = farts[:]
farts.sort()
print(farts, 'this is sorted')
farts.sort(reverse=True)
print(farts, 'this is reverse sorted\n')

# sorted() function
# returns a sorted list of the specified iterable object, default ascending
print(fartsOrig, 'this is the original list')
print(sorted(fartsOrig), 'this is sorted...')
print(fartsOrig, 'but the original list doesn\'t change')
print(sorted(fartsOrig, reverse=True), 'reverse sorted impermanently\n')

# other operations #

# reverse() method
# reverses the order of list elements
print(fartsOrig, 'this is the original list')
fartsOrig.reverse()
print(fartsOrig, 'this is reversed\n')

# len() function
# returns the number of items in an object (including lists)
print(len(farts), 'this is the length of the farts list')
