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

# exercise 4-11
friend_pizzas = pizzas[:]

pizzas.append('Spin! Pizza')
friend_pizzas.append('Dominio\'s')

for x in friend_pizzas:
    print(f'My friend likes to eat pizza at {x}!')

for x in pizzas:
    print(f'I like to eat pizza at {x}.')

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

# exercise 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

for x in my_foods:
    print(f'I like to eat {x}.')

for x in friend_foods:
    print(f'My friend likes to eat {x}.')

# exercise 4-13
buffet = ('mashed potatoes', 'steak', 'french fries',
          'cheeseburger', 'milkshake')
print('The buffet currently serves:')
for x in buffet:
    print(x)

buffet = ('steak', 'green beans', 'french fries',
          'cheeseburger', 'ice cream sundae')
print('The menu has changed!')
for x in buffet:
    print(x)
