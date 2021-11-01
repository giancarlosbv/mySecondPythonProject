print("Hello World")
print('Single quotes should work the same?')
greeting = "Hello World"
recipient = "and all who inhabit it"
year = 2021
introduction = [greeting, recipient, year]
print(introduction + ["introduction"])
# print concatenation relies on same data types
print(greeting + " this is a string")
print(type(greeting), type(recipient), type(introduction))
#data types
# str
# int
# list(like an array)
# set(), takes a list, and returns the unique elements within.
# tuple - subclass set, that can't be added onto it.
# float (int)
# dictionary
# objects
print(greeting, recipient)

numbers = [1,1,2,3,4,4,5]
unique_numbers=set(numbers)
tuple_numbers=(2,2,3,4)

print(unique_numbers)
print(type(unique_numbers))
print(tuple_numbers)
print(set(tuple_numbers))
print()
#escape sequences
print("\nGiancarlos\tBlanco")
#\n - creates a new line

x = 3
print(x, x +   x  , x * x)