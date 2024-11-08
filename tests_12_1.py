import Runners
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        r = Runners.Runner('Bob')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    def test_run(self):
        r = Runners.Runner('Bob')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        r = Runners.Runner('Bob')
        b = Runners.Runner('Jack')
        for i in range(10):
            r.run()
            b.walk()
        self.assertNotEqual(r.distance, b.distance)


if __name__ == '__main__':
    unittest.main()
