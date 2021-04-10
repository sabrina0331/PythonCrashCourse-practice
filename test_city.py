import unittest
from city_function import describe_city

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        all_info = describe_city('tianjin','china','3000000')
        self.assertEqual(all_info,'Tianjin China-Population 3000000')
unittest.main()