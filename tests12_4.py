import unittest
import logging
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                    encoding="UTF-8", format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            self.Bob_ = Runner("Bob", -5)
            for _ in range(10): self.Bob_.walk()
            self.assertEqual(self.Bob_.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning("Неверная скорость для Runner", exc_info=exc)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            self.Alex_ = Runner(True)
            for _ in range(10): self.Alex_.run()
            self.assertEqual(self.Alex_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except Exception as exc:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=exc)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        self.Karl_, self.Ivan_ = Runner("Karl"), Runner("Ivan")
        for _ in range(10): self.Karl_.walk(); self.Ivan_.run()
        self.assertNotEqual(self.Karl_.distance, self.Ivan_.distance)


if __name__ == "__main__":
    unittest.main()
