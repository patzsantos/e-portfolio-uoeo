from collections import deque
import unittest
from perception import Perception


class TestPerception(unittest.TestCase):

    def setUp(self):
        self.perception = Perception(location="Current Location", object_queue=deque(), distance=9.0, lane_mark=True)

    def test_location_update(self):  # tests if location has been updated accurately
        self.perception.location_update(city="Kobe", country="Japan")
        self.assertEqual(self.perception.location, "Kobe, Japan")

    def test_queue_object_to_avoid(self):
        # tests that there is an object within 10 meters that should be avoided to prevent collision
        expected_queue = deque(["Another car", "Human", "Barricade", "Animal"])  # check to see if they are queued
        # indicate the object to avoid and their distance from the car
        self.perception.queue_object_to_avoid("Another car", 6.2)
        self.perception.queue_object_to_avoid("Human", 3.0)
        self.perception.queue_object_to_avoid("Barricade", 8.9)
        self.perception.queue_object_to_avoid("Animal", 4.0)
        self.assertEqual(self.perception.object_queue, expected_queue)

    def test_remove_object_avoided(self):  # tests if objects will be removed from the queue once it has been avoided
        self.perception.queue_object_to_avoid("Another car", 6.2)
        self.perception.remove_object_avoided()
        self.assertEqual(len(self.perception.object_queue),0)

    def test_lane_mark_detection(self):  # tests if car is driving within the lane
        self.perception.lane_mark_detection(lane_detected=False)
        self.assertFalse(self.perception.lane_mark)


if __name__ == '__main__':
    unittest.main()
