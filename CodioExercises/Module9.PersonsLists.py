class Person:
    """Represents a generic Person."""

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

p1 = Person('Tom', 'Turner', 110, 70)
p2 = Person('Fred', 'Faulkner', 111, 71)
p3 = Person('George', 'Garcia', 112, 72)
p4 = Person('Tanya', 'Tan', 113, 73)
p5 = Person('Mary', 'McGee', 114, 75)

Persons = [p1, p2, p3, p4, p5]
for i in Persons:
    print(i.first_name)

# Reference:
# Google for Education(2023) Python Lists.
# Available from: https://developers.google.com/edu/python/lists
# [Accessed 22 November 2023]
