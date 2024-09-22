import unittest
from tests12_3 import TournamentTest, RunnerTest


test_suite_new = unittest.TestSuite()
test_suite_new.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite_new.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite_new)
