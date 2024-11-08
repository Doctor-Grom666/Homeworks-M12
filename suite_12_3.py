import unittest
import tests_12_3 as tests

suite = unittest.TestSuite()

suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))


testy_runner = unittest.TextTestRunner(verbosity=2)
testy_runner.run(suite)