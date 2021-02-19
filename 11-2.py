import unittest
from city_functions import city
class test_cities(unittest.TestCase):
    def test_city_country(self):
        city_country = city('beijing','china','1600')
        self.assertEqual(city_country,'Beijing China-1600')
unittest.main()
        
