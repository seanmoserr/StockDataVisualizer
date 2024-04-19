import unittest
from datetime import datetime
import re

class sdvUnitTests(unittest.TestCase):

    def tSymbol(self):
        symbol = "AMD"
        self.assertTrue(re.match("^[A-Z]{1,7}$", symbol))

    def tChartType(self):
        chart_type = "2"
        self.assertTrue(chart_type in ["1", "2"])

    def tTimeSeries(self):
        time_series = "3"
        self.assertTrue(re.match("^[1-4]$", time_series))

    def tSDate(self):
        start_date = "2021-05-05"
        self.assertTrue(re.match("^(\d{4})-(\d{2})-(\d{2})$", start_date))

    def tEDate(self):
        end_date = "2022-06-06"
        self.assertTrue(re.match("^(\d{4})-(\d{2})-(\d{2})$", end_date))

if __name__ == '__main__':
    unittest.main()
