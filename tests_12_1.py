import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """
        test for walk method in runner
        :return:
        """
        walker = runner.Runner('walker')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        """
        test for run method in runner
        :return:
        """
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        """
        test for compare walk and run method in runner
        :return:
        """
        walker = runner.Runner('walker')
        runner_ = runner.Runner('runner')
        for i in range(10):
            runner_.run()
            walker.walk()
        self.assertNotEqual(runner_.distance, walker.distance)

if __name__ == 'main':
    unittest.main()