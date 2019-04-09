from chap5_resources import furbies
from chap5_resources import buffets
from chap5_resources import cubes

# exercise 5-1
print('Is furbies[3] a lion? I predict True.')
print(furbies[3] == 'lion')

print('Is furbies[1] a cat? I predict False.')
print(furbies[1] == 'cat')

print('Is buffets[4] a milkshake? I predict True.')
print(buffets[4] == 'milkshake')

print('Is buffets[0] a cheeseburger? I predict False.')
print(buffets[0] == 'cheeseburger')

print('Is buffets[-3] french fries? I predict True.')
print(buffets[-3] == 'french fries')

# exercise 5-2
print('Is furbies[-1] not a lemur? I predict False.')
print(furbies[-1] != 'lemur')

print('Is cubes[-1] equal to 1000? I predict True.')
print(cubes[-1] == 1000)

print('Is cubes[0] different than cubes[-1]? I predict True')
print(cubes[0] != cubes[-1])

print('Is cubes[2] less than cubes[0]? I predict False.')
print(cubes[2] < cubes[0])

print('Is cubes[5] greater than or equal to cubes[4]? I predict True.')
print(cubes[5] >= cubes[4])

friend = 'Lauren'
print('Is my friend named Lauren? I predict True.')
print(friend.lower() == 'lauren')

print('Do cats and lions both have fur? I predict True.')
print('cat' in furbies and 'lion' in furbies)

print('Lizards do not have fur - I predict True.')
print('lizard' not in furbies)

print('Does the buffet serve cheeseburgers or pie? I predict True.')
print('cheeseburger' in buffets or 'pie' in buffets)

print('Does the buffet serve both cheeseburgers and pie? I predict False.')
print('cheeseburger' in buffets and 'pie' in buffets)
