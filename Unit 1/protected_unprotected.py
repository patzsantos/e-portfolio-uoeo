"""Develop a Python program and apply protected and unprotected variables within it."""


class Athletes:
    # protected athletes use the underscore to indicate that they are private
    _name = "Rafa"
    _athlete_num = "01"

    # public (unprotected) athlete
    name = "Bjorn"
    athlete_num = "02"

    def display_info(self):
        # gaining access to protected athletes
        print("Protected Name:", self._name)
        print("Protected Athlete Number:", self._athlete_num)

        # gaining access to unprotected athletes
        print("Public Name", self.name)
        print("Public Athlete Num", self.athlete_num)


obj = Athletes()
obj.display_info()


"""
Reference:
GeeksforGeeks (2020) Protected Variable in Python. 
Available from: https://www.geeksforgeeks.org/protected-variable-in-python/ [Accessed 22 November 2023].
"""
