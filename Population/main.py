import csv
import random
from person import *

# Create a list of names by reading them from a file
names = []
with open('names.csv', 'r') as f:
    for line in f:
        names.append(line.strip())
names = names[1:]  # Remove the header

# Create a list of eye colors
eye_colors = ['amber', 'blue', 'brown', 'gray', 'green', 'hazel']

# Create a list of colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black', 'white']

# Create a list of people
population = []


def generate_random_person():
    name = random.choice(names)
    age = random.randint(1, 65)
    eye_color = random.choice(eye_colors)
    favorite_color = random.choice(colors)
    return Person(name, age, eye_color, favorite_color)


for i in range(0, 200):
    person = generate_random_person()
    population.append(person)
random.shuffle(population)

# Write the population to a file
with open('population.csv', 'w') as csvfile:
    fieldnames = ['name', 'age', 'eye_color', 'favorite_color']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for person in population:
        writer.writerow({'name': person.name, 'age': person.age, 'eye_color': person.eye_color,
                         'favorite_color': person.favorite_color})
