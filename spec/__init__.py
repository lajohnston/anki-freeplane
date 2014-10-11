# Add parent folder to include path
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')


import unittest
from test_freeplane_node import TestFreeplaneNode
suite = unittest.TestLoader().loadTestsFromTestCase(TestFreeplaneNode)
