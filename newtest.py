import unittest
from Runner import Runner
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF',
                    format='%(funcName)s - %(asctime)s - %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            r1 = Runner('Petr', -5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50, f'{r1.name}Должен пробежать 50, а пробежал {r1.distance}')
            logging.info('"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            r2 = Runner(2)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100, f'{r2.name}Должен пробежать 100, а пробежал {r2.distance}')
            logging.info('"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning("Неверный тип данных для объекта Runner")

    def test_challenge(self):
        r1 = Runner('Petr')
        r2 = Runner('iVAN')
        for _ in range(10):
            r1.walk()
            r2.run()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()