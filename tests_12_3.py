import unittest
import runner_and_tournament as rat


class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        test for walk method in runner
        :return:
        """
        walker = rat.Runner('walker')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        test for run method in runner
        :return:
        """
        runner_ = rat.Runner('runner')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """
        test for compare walk and run method in runner
        :return:
        """
        walker = rat.Runner('walker')
        runner_ = rat.Runner('runner')
        for i in range(10):
            runner_.run()
            walker.walk()
        self.assertNotEqual(runner_.distance, walker.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = rat.Runner('Усейн', 10)
        self.Andrew = rat.Runner('Андрей', 9)
        self.Nik = rat.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = rat.Tournament(90,self.Usein, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[1] = result
        self.assertTrue(TournamentTest.all_results[1][2] == ('Ник'))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = rat.Tournament(90,self.Andrew, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[2] = result
        self.assertTrue(TournamentTest.all_results[2][2] == ('Ник'))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        """
        test for start method in Tournament class
        :return:
        """
        Tournament = rat.Tournament(90,self.Usein, self.Andrew, self.Nik)
        result = Tournament.start()
        TournamentTest.all_results[3] = result
        self.assertTrue(TournamentTest.all_results[3][3] == ('Ник'))

    @classmethod
    def tearDownClass(cls):
        s = (tuple(list((j, str(cls.all_results[i][j].name)) for j in cls.all_results[i]) for i in cls.all_results))
        print(*[dict(i) for i in s], sep='\n')


if __name__ == '__main__':
    unittest.main()
