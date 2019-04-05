# exercise 3-8
locations = ['vienna', 'amsterdam', 'prague', 'edinburgh', 'istanbul']
locations = [x.title() for x in locations]
print(locations, '\n')

print(sorted(locations))
print(locations, '\n')

print(sorted(locations, reverse=True))
print(locations, '\n')

locations.reverse()
print(locations)
locations.reverse()
print(locations, '\n')

locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
