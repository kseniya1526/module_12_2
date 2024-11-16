import unittest
import TestCase


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.Usain = TestCase.Runner('Усэйн', 10)
        self.Andrey = TestCase.Runner('Андрей', 9)
        self.Nick = TestCase.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    def test_Usain_Nick(self):
        tournament = TestCase.Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

    def test_Andrey_Nick(self):
        tournament = TestCase.Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

    def test_Usain_Andrey_Nick(self):
        tournament = TestCase.Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

