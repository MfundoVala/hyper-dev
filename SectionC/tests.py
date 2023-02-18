import unittest
from unittest.mock import patch
from SectionC.Option2 import *

class MyTestCase(unittest.TestCase):

    def test_no_immediate(self):
        # Test case 1: Shortest path has no intermediate nodes
        path1 = navigate(roads, 1, 3)
        self.assertEqual(path1, {'distance': 9, 'path': [1, 3]})

    def test_immediate(self):
        # Test case 2: Shortest path has intermediate nodes
        path2 = navigate(roads, 2, 0)
        assert path2 == {'distance': 5, 'path': [2, 4, 0]}

    def test_same_node(self):     
        # Test case 3: Shortest path is the same node
        path3 = navigate(roads, 0, 0)
        assert path3 == {'distance': 0, 'path': [0]}