import unittest
from solution import Doors


class Test100Doors(unittest.TestCase):
    def test_returns_correct_initial_state(self):
        self.assertEqual(["closed" for _ in range(100)], Doors().doors)

    def test_toggle_doors_returns_false_if_given_invalid_idx(self):
        doors = Doors()
        self.assertFalse(doors.toggle_door(-5))
        self.assertFalse(doors.toggle_door(100))
        self.assertFalse(doors.toggle_door(101))
        self.assertEqual(["closed" for _ in range(100)], doors.doors)
        
    def test_toggles_door_if_given_valid_idx(self):
        doors = Doors()
        doors.toggle_door(0)
        self.assertEqual(doors.doors[0], "opened")
        doors.toggle_door(0)
        self.assertEqual(doors.doors[0], "closed")
        doors.toggle_door(0)
        self.assertEqual(doors.doors[0], "opened")
        

                
    
