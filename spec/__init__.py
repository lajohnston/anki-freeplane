from .test_reader import TestReader
from .test_importer import TestImporter
from .test_node import TestNode
import unittest
import sys
import os

unittest.TestLoader().loadTestsFromTestCase(TestNode)
unittest.TestLoader().loadTestsFromTestCase(TestReader)
unittest.TestLoader().loadTestsFromTestCase(TestImporter)
