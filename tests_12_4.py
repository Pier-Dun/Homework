import unittest
import rt_with_exceptions as rat
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):

    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        """
        test for walk method in runner
        :return:
        """
        try:
            walker = rat.Runner('walker', -1)
            for i in range(10):
                walker.walk()
            self.assertEqual(walker.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """
        test for run method in runner
        :return:
        """
        try:
            runner_ = rat.Runner(True)
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

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


if __name__ == '__main__':
    unittest.main()