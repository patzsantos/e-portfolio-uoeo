import unittest
from vtoi import V2I


class TestV2I(unittest.TestCase):

    def setUp(self):
        self.v2i = V2I()

    def test_decipher_traffic_sign(self):  # asserts that the traffic sign is being interpreted correctly
        expected = "This traffic sign says no left turn."
        result = self.v2i.decipher_traffic_sign("no left turn")
        assert result == expected, "Invalid traffic sign."


    def test_decipher_traffic_light(self):  # asserts that the traffic light is being interpreted correctly
        expected = "Car should stop."
        result = self.v2i.decipher_traffic_light("red")
        assert result == expected, "Invalid traffic light."


if __name__ == '__main__':
    unittest.main()
