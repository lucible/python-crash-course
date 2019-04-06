# exercise 3-1
names = ['Marco', 'Mathias', 'Reed', 'Emily', 'Josh', 'Brendon']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

# exercise 3-2
friend = "testing"
message = f'You are a very good friend, {friend}!'
friend = names[0]
# note that this will print "testing" and not "marco"
print(message)

# introduced a loop cause writing prints by hand sucks
i = 0
while i < 6:
    friend = names[i]
    message = f'{friend} is super nice!'
    print(message)
    i += 1


# can I do this without a while?
def message(name):
    return f'{name} is super nice!'


results = list(map(message, names))
print(results)

# exercise 3-3
vehicles = ['bicycle', 'taxi', 'car', 'train']
print(f'I like to ride my {vehicles[0]}!')
print(f'Some think the {vehicles[1]} is becoming obsolete.')
print(f'There are lots of {vehicles[-1]}s in Japan!')
print(f'Lots of people own a {vehicles[-2]}.')
