# exercise 4-1
pizzas = ['Pie5', 'Lou Malnati\'s', 'Giordano\'s']

for place in pizzas:
    print(place)

for place in pizzas:
    print(f'I like to eat pizza from {place}.')

print('Pizza is REALLY delicious!')


def yum(restaurant):
    return f'I like to eat at {restaurant}!'


print('\n'.join(map(yum, pizzas)))

# exercise 4-2
furbies = ['cat', 'giraffe', 'gorilla']

for animal in furbies:
    print(animal)

for animal in furbies:
    print(f'A {animal} has fur.')

print('All of these animals have fur!')


def hasFur(animal):
    return f'A {animal} has fur.'


print('\n'.join(map(hasFur, furbies)))
