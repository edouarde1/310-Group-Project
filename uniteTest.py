import unittest
from Scripts import spell_check
from naive_bot.naive_bot import load_data, get_response
import csv

class TestClass(unittest.TestCase):
    def test_spell_check(self):
        self.assertEqual(spell_check("tdll md wdy"),["tell", "my", "why"])
    
    def test_get_response(self):
        keywords = load_data("keywords.csv")
        self.assertEqual(get_response("1",keywords),"Sorry I did not understand what you said")
    
    def test_load_data(self):
        self.assertEqual(load_data("file_does_not_exist.csv"),"Sorry! I cant come up with the words right now")

if __name__ == '__main__':
    unittest.main()
