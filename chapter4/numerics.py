# exercise 4-3
for x in range(1, 21):
    print(x)

# exercise 4-5
millions = range(1, 1000001)
print(min(millions))
print(max(millions))
print(sum(millions))

# exercise 4-6
odds = list(range(1, 20, 2))
for x in odds:
    print(x)

# exercise 4-7
triples = list(range(3, 31, 3))
for x in triples:
    print(x)

# exercise 4-8
cubes = []
for x in range(1, 11):
    cubes.append(x**3)

print(cubes)

# exercise 4-9
cubes2 = [x**3 for x in range(1, 11)]
print(cubes2)

# exercise 4-10
print('The first three items in the list are:', cubes2[:3])
print('Three items from the middle of the list are:', cubes2[3:6])
print('The last three items from the list are:', cubes2[-3:])
