import unittest
from main import distribution_of_clans, count_wedding_pairs

class test_main(unittest.TestCase):
    def setUp(self):
        self.first_test_quantity_pairs = 3
        self.first_test_graph = [(1,2),(2,4),(3,5)]
        self.second_test_quantity_pairs = 5
        self.second_test_graph = [(1,2),(2,4),(1,3),(3,5),(8,10)]
        self.third_test_quantity_pairs = 3
        self.third_test_graph = [(1,3),(5,7),(9,11)]
        self.first_result = 4
        self.second_result = 6
        self.third_result = 0

    def test_first(self):
        self.assertEqual(count_wedding_pairs(distribution_of_clans(self.first_test_quantity_pairs, self.first_test_graph)), self.first_result)

    def test_second(self):
        self.assertEqual(count_wedding_pairs(distribution_of_clans(self.second_test_quantity_pairs, self.second_test_graph)), self.second_result)

    def test_third(self):
        self.assertEqual(count_wedding_pairs(distribution_of_clans(self.third_test_quantity_pairs, self.third_test_graph)), self.third_result)

if __name__ == '__main__':
    unittest.main( )