# Login code test using unittest

import unittest
from login import Car, login


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_start(self):
        self.car.start()
        self.assertTrue(self.car.on)  # car is running if it starts

    def test_stop(self):
        self.car.start()
        self.car.stop()
        self.assertFalse(self.car.on)  # car is not running if it is stopped


class TestLogin(unittest.TestCase):
    def test_login_authenticated(self):  # login should be authenticated in order to start and stop the car
        self.assertTrue(login())  # authorized user can start and stop the car from the front end


if __name__ == '__main__':
    unittest.main()
