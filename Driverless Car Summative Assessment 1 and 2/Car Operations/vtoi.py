""" Third Operation: Vehicle to Infrastructure Communication"""
from dataclasses import dataclass


@dataclass
class V2I:
    def __init__(self):
        # list of stored traffic signs
        self.signs = ("to stop", "no u-turn", "you can u-turn", "no left turn", "no right turn")
        # dictionary of stop lights and their corresponding action
        self.lights = {
            "red": "stop",
            "yellow": "slow down",
            "green": "go"
        }

    def decipher_traffic_sign(self, sign):  # Camera processes traffic sign images and interprets their meanings
        assert sign in self.signs, "Traffic sign cannot be deciphered."  # checks if traffic sign is in the stored list
        return_value = f"This traffic sign says {sign}."  # interprets the traffic sign
        print(return_value)  # displays the deciphered traffic sign
        return return_value

    def decipher_traffic_light(self, color):  # Camera processes traffic light and their corresponding action
        assert color in self.lights, "Traffic light cannot be deciphered."  # checks if traffic light is in dictionary
        return_value = f"Car should {self.lights[color]}."  # interprets the traffic light
        print(return_value)  # displays the deciphered traffic light and tells the car what to do
        return return_value


v2i = V2I()
v2i.decipher_traffic_sign("no u-turn")
v2i.decipher_traffic_light("green")
