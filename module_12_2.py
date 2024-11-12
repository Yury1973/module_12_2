import unittest


import runner_and_tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = runner_and_tournament.Runner('Усейн', 10)
        self.run_2 = runner_and_tournament.Runner('Андрей', 9)
        self.run_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            results = {}
            for place, runner in result.items():
                results[place] = runner.name
            print(results)

    def test_run_1(self):
        self.tournament_1 = runner_and_tournament.Tournament(90, self.run_1, self.run_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.tournament_2 = runner_and_tournament.Tournament(90, self.run_2, self.run_3)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.tournament_3 = runner_and_tournament.Tournament(90, self.run_1, self.run_2, self.run_3)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()
