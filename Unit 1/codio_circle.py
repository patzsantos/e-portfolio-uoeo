from __future__ import print_function, division

import copy

from Point1 import Point, Rectangle, print_point
from Point1_soln import distance_between_points


class Circle:
    """Represents a circle.

    Attributes: center, radius
    """


class Point:
    """Represents a point.

    Attributes: x,y
    """


def point_in_circle(point, circle):
    """True if the Point lies in or on the boundary of the circle.

    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


class Rectangle:
    """Represents a rectangle:

    Attributes: width, height, corner
    """


def rect_in_circle(rect, circle):
    """True if the Rectangle lies entirely in or on the boundary of the circle.

    rect: Rectangle object
    circle: Circle object
    """

    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y._ = rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """ True if any of the corners of the Rectangle fall inside the circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y._ = rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x._ = rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()


"""References

AbhishekMali21 (2019) CHAPTER 15- exercises.ipynb. Available from:
https://github.com/AbhishekMali21/PYTHON-FOR-EVERYBODY/blob/master/CHAPTER%2015%20-%20exercises.ipynb
[Accessed 21 November 2023].

R-D-View (2022) Point1.py. Available from:
https://github.com/R-D-Vie/PythonPractice_OOIS/blob/main/Classes_Objects/Point1.py
[Accessed 21 November 2023]."""

