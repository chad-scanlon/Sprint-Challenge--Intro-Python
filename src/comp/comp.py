# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = []
a.extend([humans])
a = [human.name for human in humans if human.name[0] == "D"]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = []
b.extend([humans])
b = [human.name for human in humans if human.name[-1] == "e"]
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = []

c = [human.name for human in humans if human.name[0] == "C"]
d = [human.name for human in humans if human.name[0] == "D"]
e = [human.name for human in humans if human.name[0] == "E"]
f = [human.name for human in humans if human.name[0] == "F"]
g = [human.name for human in humans if human.name[0] == "G"]

c.append([d,e,f,g])
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = []
d.extend([humans])
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
ee = []
ee.extend([humans])
ee = [human.name for human in humans]
age = []
age.extend([humans])
age = [human.age for human in humans]

e = list(zip(ee, age))
print(e)
# amount = "32.054,23"
# maketrans = amount.maketrans
# amount = amount.translate(maketrans(',.', '.,'))
# print(amount)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = []
x = []
x.extend([humans])
x = [human.name for human in humans]
y = []
# y.extend([humans])
y = [human.age for human in humans if human.age < 32 and human.age > 27]
# if y < 32 and y > 27:
#     print(y)

f = list(zip(x, y))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
g = []
x.extend([humans])
x = [human.name for human in humans]
x = [word.upper() for word in x]
y.extend([humans])
y = [human.age + 5 for human in humans]
y.extend(x)
g.extend(x)
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = []
h.extend([humans])
h = [math.sqrt(human.age) for human in humans]
print(h)


# python3 src/comp/test_comp.py
# python3 src/comp/comp.py