import Runners
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding="utf-8", format="%(asctime)s -|- %(levelname)s -|- %(message)s")


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            obj1 = Runners.Runner('Вася', -1)
            for _ in range(10):
                obj1.walk()
            self.assertEqual(obj1.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            obj2 = Runners.Runner(2)
            for _ in range(10):
                obj2.run()
            self.assertEqual(obj2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    if __name__ == "__main__":
        unittest.main()
