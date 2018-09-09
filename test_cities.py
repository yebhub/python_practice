import unittest 
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_city = get_formatted_city("new york", "united states")
        self.assertEqual(formatted_city, "New York, United States")

    def test_city_population(self):
        formatted_city = get_formatted_city("new york", "united states", 8.5 )
        self.assertEqual(formatted_city, "New York, United States\npopulation: 8.5 million.")
unittest.main()