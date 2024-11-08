import Runners
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r = Runners.Runner('Bob')
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r = Runners.Runner('Bob')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r = Runners.Runner('Bob')
        b = Runners.Runner('Jack')
        for i in range(10):
            r.run()
            b.walk()
        self.assertNotEqual(r.distance, b.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = Runners.Runner('Усэйн', 10)
        self.runner_2 = Runners.Runner('Андрей', 9)
        self.runner_3 = Runners.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = Runners.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест первого раунда'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = Runners.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест второго раунда'] = result

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = Runners.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест третьего раунда'] = result


if __name__ == '__main__':
    unittest.main()
