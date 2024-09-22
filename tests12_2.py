import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = list()

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def test_tournament_01(self):
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner_3)

    def test_tournament_02(self):
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(TournamentTest.all_results[-1][2] == self.runner_3)

    def test_tournament_03(self):
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results.append(tournament_3.start())
        self.assertTrue(TournamentTest.all_results[-1][3] == self.runner_3)

    def test_tournament_04(self):
        if self.prepare_test4() != self.runner_3:
            with self.assertRaises(Exception):
                self.prepare_test4()
        else:
            self.assertTrue(self.prepare_test4() == self.runner_3)

    def prepare_test4(self):
        tournament_4 = Tournament(81, self.runner_3, self.runner_2, self.runner_1)
        TournamentTest.all_results.append(tournament_4.start())
        last_runner = TournamentTest.all_results[-1][3]
        second_runner = TournamentTest.all_results[-1][2]
        if last_runner != self.runner_3:
            raise Exception(f'Самый медленный {self.runner_3} должен быть на 3-м месте, а не {last_runner} ')
        elif second_runner != self.runner_2:
            raise Exception(f'Вторым должен быть {self.runner_2}, а не {second_runner} ')
        else:
            return self.runner_3

    @classmethod
    def tearDownClass(cls):
        for test in cls.all_results:
            print(test)

    if __name__ == "__main__":
        unittest.main()
