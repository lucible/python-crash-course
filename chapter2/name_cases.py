# exercise 2-3
firstName = "Marco"
message = firstName + ", do you like to play tennis?"
print(message)

# exercise 2-4
fullName = "Kublai Khan"
print(fullName.upper())
print(fullName.lower())
print(fullName.title())

# exercise 2-5 & 2-6
poem = "If only those parakeets would settle\nA little nearer to where I'm \
sitting, instead of at the tops of far-off\n\ttrees, this morning\n\
Would be so much more remarkable."
author = "Jay Hopler"
title = "beauty is a real thing, i've seen it"
print("A poem by " + author + ", this is '" + title.title() + "':\n" + poem)

# exercise 2-7
name = " John \tD \nHopkins  \t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
# strip does not remove new lines or tabs, just spaces?

# testing out the f'' string concat
string1 = "The quick brown fox"
string2 = "jumped over"
string3 = "the lazy dog"
print(f'{string1} {string2} {string3}!!')
