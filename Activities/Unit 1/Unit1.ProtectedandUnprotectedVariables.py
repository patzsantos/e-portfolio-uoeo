# Develop a Python program and apply protected and unprotected variables within it.

# with protected variables

class Athletes:
    # protected athletes
    _name = "Rafa"
    _athletenum = "01"

    # public (unprotected) athlete
    name = "Bjorn"
    athletenum = "02"

    def displayNameandAthleteNum(self):
    # gaining access to protected athletes
        print("Name", self._name)
        print("Athlete Num", self._athletenum)

obj = Athletes()
obj.displayNameandAthleteNum()

# Reference:
# GeeksforGeeks (2020) Protected Variable in Python.
# Available from: https://www.geeksforgeeks.org/protected-variable-in-python/
# [Accessed 22 November 2023].

###

#another method of making variables both private and protected
class Meal:
    def __init__(self):
        self._protected = 'protected'
        self._private = 'private'

    def dinner(self):
        print(self._protected)
        print(self._private)

meal = Meal()
print(meal._protected)

# Reference:
# Indently (2023) This is how you create private & protected variables in Python.
# Available from: https://www.youtube.com/shorts/QVpyicCLvKY
# [Accessed 22 November 2023].

###

# public variables

public class Salary:
{
    public String employee;
    public int balance;

    public salary (String name, int balance)
    {
        owner = name;

        if (balance >=0)
            salary = positive;
        else
            salary = negative;
    }
}

# Reference:
https://www.javacoffeebreak.com/faq/faq0002.html
