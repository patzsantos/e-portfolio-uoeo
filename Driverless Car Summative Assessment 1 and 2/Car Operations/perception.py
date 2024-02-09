"""Second Operation: Environment Perception"""


from collections import deque
from dataclasses import dataclass

@dataclass
class Perception:
    location: str  # GPS tells the city and street name as a string
    object_queue: deque[str]  # LiDAR detects objects to avoid and places them in a queue
    distance: float  # LiDAR measures object distance in meters
    lane_mark: bool  # LiDAR detects whether lane marking is present or not

    def __init__(self, location: str, object_queue:deque(), distance: float, lane_mark:bool):
        self.location = location
        self.object_queue = deque(object_queue)
        self.distance = distance
        self.lane_mark = lane_mark

    def location_update(self, city: str, country: str):  # GPS updates current location
        assert isinstance(city, str) and isinstance(country, str), "Strings should represent the city and country."
        self.location = f"{city}, {country}"  # states the city and country where the car currently is
        print(f"According to the GPS, you are currently in {self.location}.")  # displays you present location

    def queue_object_to_avoid(self, object:str, distance:float): # LiDAR detects objects to avoid to prevent collision
        assert isinstance(object, str), "String should represent an object."
        assert isinstance(distance, float), "Distance should be a float."
        if distance <= 10:  # warning system will initiate to tell the car that an object is within collision range
            self.object_queue.append(object)  # the objects will be queued in order of detection
            print(f"Warning: {object} detected {distance} meters away. Avoid possible collison.")
        else:
            print(f"The road is clear. Continue driving safely.")  # no object in the car surroundings

    def remove_object_avoided(self):  # removes objects that have been avoided
        if self.object_queue:
            removed_object = self.object_queue.popleft()  # object avoided is removed following 'first in first out'
            print(f"{removed_object} has been avoided. It is now removed from the queue.")
        else:
            print("No objects to avoid.")

    def lane_mark_detection(self, lane_detected: bool):  # LiDAR detects if car is driving within the lanes
        assert isinstance(lane_detected, bool), "Line marking should be a boolean value."
        self.lane_mark = lane_detected  # lane marking is present
        if self.lane_mark:
            print("Car is driving over the lane. Get back within the lane.")  # car must not cross or drive over lanes
        else:
            print("Continue driving within the lane.")  # car is driving safely if it is driving within the lanes


# try to run the code
perception = Perception(location="Current Location", object_queue=[], distance=11.0, lane_mark=True)

# to update present location
perception.location_update(city="Kobe", country="Japan")

# detect objects to avoid possible collision
perception.queue_object_to_avoid("Another car", 6.2)
perception.queue_object_to_avoid("Human", 3.0)
perception.queue_object_to_avoid("Barricade", 8.9)
perception.queue_object_to_avoid("Animal", 4.0)

# once avoided, remove from the queue
perception.remove_object_avoided()
perception.remove_object_avoided()

# continue checking objects to avoid to prevent collision
detected_object = perception.object_queue[0] if perception.object_queue else "No object detected."

# check lane marking
perception.lane_mark_detection(lane_detected=False)
