name = "fredrick b thornsberry"
print(name.title())

# this does not work b/c title is not a defined function
# capsName = title(name)
capsName = name.title()
print(capsName)

# prints entirely uppercase
print(name.upper())
# prints entirely lowercase
print(name.lower())
# capitalizes the first character of the string
print(name.capitalize())

firstName = "frederick"
lastName = "thornsberry"
fullName = firstName + " " + lastName
print("Hello, " + fullName.title() + "!")

message = "Hello, my dear " + firstName.capitalize() + " " + lastName.capitalize() + "!"
print(message)

# oooo, you can add tabs with \t
print("\tPython Rocks!")
print("Languages:\n\tPython\n\tJavaScript\n\tHTML & CSS")
