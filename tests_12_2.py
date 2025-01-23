import unittest
import runner_and_tournament as runner


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = runner.Runner('Усейн', 10)
        self.Andrew = runner.Runner('Андрей', 9)
        self.Nik = runner.Runner('Ник', 3)

    def test_1(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = runner.Tournament(90,self.Usein, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(TournamentTest.all_results[1][2] == ('Ник'))

    def test_2(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = runner.Tournament(90,self.Andrew, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(TournamentTest.all_results[2][2] == ('Ник'))

    def test_3(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = runner.Tournament(90,self.Usein, self.Andrew, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(TournamentTest.all_results[3][3] == ('Ник'))

    @classmethod
    def tearDownClass(cls):
        s = (tuple(list((j, str(cls.all_results[i][j].name)) for j in cls.all_results[i]) for i in cls.all_results))
        print(*[dict(i) for i in s], sep='\n')


if __name__ == '__main__':
    unittest.main()
