import unittest
from datetime import datetime
import re

class sdvUnitTests(unittest.TestCase):

    def test_symbol_constraint(self):
        symbol = "AMD"
        self.assertTrue(re.match("^[A-Z]{1,7}$", symbol))

    def test_chart_type_constraint(self):
        chart_type = "2"
        self.assertTrue(chart_type in ["1", "2"])

    def test_time_series_constraint(self):
        time_series = "3"
        self.assertTrue(re.match("^[1-4]$", time_series))

    def test_start_date_constraint(self):
        start_date = "2021-05-05"
        self.assertTrue(re.match("^(\d{4})-(\d{2})-(\d{2})$", start_date))

    def test_end_date_constraint(self):
        end_date = "2022-06-06"
        self.assertTrue(re.match("^(\d{4})-(\d{2})-(\d{2})$", end_date))

if __name__ == '__main__':
    unittest.main()
