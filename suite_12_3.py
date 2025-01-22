import unittest

from tests_12_3 import RunnerTest
from tests_12_3 import TournamentTest


test = unittest.TestSuite()
test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner_test = unittest.TextTestRunner(verbosity=2)
runner_test.run(test)
