import unittest
import math
from control import Control


class TestControl(unittest.TestCase):

    def setUp(self):
        self.car_control = Control()

    def tearDown(self):  # if resetting the state of the car is necessary
        pass

    def test_left_steer(self):  # tests that the car is steering to the left
        steering_direction = self.car_control.steer(math.radians(100))
        self.assertEqual(steering_direction, "Car is steering to the left.")

    def test_right_steer(self):  # tess that the car is steering to the right
        steering_direction = self.car_control.steer(math.radians(20))
        self.assertEqual(steering_direction, "Car is steering to the right.")

    def test_update_speed(self):  # tests that the speed is being updated correctly
        new_speed = self.car_control.accelerate(110)
        self.assertEqual(new_speed, 110)

    def test_max_speed(self):  # tests if the car has reached the maximum speed allowed
        self.car_control.speed = 50  # starting speed
        self.car_control.accelerate(70)  # increase in velocity
        self.assertEqual(self.car_control.speed, 120)  # maximum speed allowed has been reached

    def test_brake(self):  # tests successful car braking if speed falls to 0 km/h
        self.car_control.brake()
        self.assertEqual(self.car_control.speed, 0)


if __name__ == '__main__':
    unittest.main()
