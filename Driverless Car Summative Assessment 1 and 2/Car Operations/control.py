"""First operation: Car Control"""

import math  # used for getting pi in order to compute the steering angle


class Control:
    MAX_SPEED_ALLOWED = 120  # maximum speed before automatic braking

    def __init__(self):
        self.speed = 0  # initial speed of the carin km/h

    def steer(self, steering_angle):  # car cruising while driving
        """Angle of steering will determine the steering direction.
        Arguments:
            steering_angle(float): Steering angle in radians
        Returns:
            str: Steering direction('left' or 'right')"""
        assert 0 <= steering_angle < math.pi, "Steering angle should be between 0 and pi radians"  # 1-179 degrees only
        if math.pi / 2 <= steering_angle <= 3 * math.pi / 2:
            return "Car is steering to the left."  # angle is between 90-179 degrees
        else:
            return "Car is steering to the right."  # angle is between 1-89 degrees

    def accelerate(self, speed_increase):  # increase in car velocity
        """Speed increases during acceleration.
        Arguments:
            speed_increase (float): Increasing speed measured in km/h.
        Returns:
            float: Current speed after acceleration."""
        new_speed = self.speed + speed_increase  # adds initial speed and acceleration to get the new speed
        if new_speed > self.MAX_SPEED_ALLOWED:  # new speed
            print("Warning: Car is braking because maximum speed limit has been reached.")  # display warning message
            self.brake()  # car automatically brakes
            return "Speed limit reached."
        else:
            self.speed = new_speed  # car is informed of its new speed and car is driving within speed limit
            print(f"Your current driving speed is: {self.speed} km/h")  # display current speed
            return self.speed

    def brake(self):  # car decreases speed until it slows down
        """Brake system on."""
        print("Car is braking.")  # braking system is in effect
        if self.speed != 0:  # car is not yet braking
            raise ValueError("After braking, speed should be 0.")
        self.speed = 0  # car is now stopped


# try to run the code
if __name__ == "__main__":

    # indicate steering angle and direction
    car_control = Control()
    steering_angle = car_control.steer(math.radians(178))
    print(f"{steering_angle}")

    # accelerate and update new speed
    new_speed = car_control.accelerate(14)

    # check driving speed
    new_speed = car_control.accelerate(102)  # increase in speed
    if new_speed == "Speed limit reached":  # if driving speed exceeds 120 km/h
        car_control.brake()  # car should automatically brake because it is driving too fast




