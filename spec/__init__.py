# Add parent folder to include path
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')


import unittest
from test_node import TestNode
from test_importer import TestImporter
from test_reader import TestReader

unittest.TestLoader().loadTestsFromTestCase(TestNode)
unittest.TestLoader().loadTestsFromTestCase(TestReader)
unittest.TestLoader().loadTestsFromTestCase(TestImporter)

