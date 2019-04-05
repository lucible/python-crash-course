# removing items from a list #
farts = ['gooey', 'sticky', 'moist']
print(farts)

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
print(farts)

# insert() method
# exclusive to lists, inserts element at specified position
farts.insert(0, 'windy')
print(farts)
