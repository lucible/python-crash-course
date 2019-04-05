# exercise 3-4
guests = ['plato', 'socrates', 'descartes']


def invite(name):
    return f'Dear {name.title()}, you are cordially invited to dinner!'


invited = list(map(invite, guests))
print(invited)

# exercise 3-5
print(f'Oh no, {guests[-1].title()} can\'t make it!')
del guests[-1]
guests.append('kant')
print(guests[-1].title())

print(list(map(invite, guests)))

print('We found a bigger dinner table, hooray!')
guests.insert(0, 'nietzsche')
guests.insert(2, 'adorno')
guests.append('durkheim')

print(list(map(invite, guests)))

# aha, I googled a better way to print out the list!
print('\n'.join(map(invite, guests)))

# exercise 3-7

print('Oh NO, the table won\'t arrive in time!\nOnly two people\
     can come to dinner now.')


def sorry(name):
    return f'I\'m sorry, {name.title()}, you aren\'t invited.'


# there's gotta be a better way to do this, right?
# I could do a while loop here...
print(sorry(guests.pop()))
print(sorry(guests.pop()))
print(sorry(guests.pop()))
print(sorry(guests.pop()))

print('\n'.join(map(invite, guests)))

del guests[1]
del guests[0]

print(guests)
