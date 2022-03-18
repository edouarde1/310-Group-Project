import unittest
import os
import boty
import data_utils.data_load as dl

import csv

class TestClass(unittest.TestCase):
    def test_spell_check(self):
        self.assertEqual(boty.spell_check("tdll md wdy"),"tell my why")
    
    def test_get_response(self):
        self.assertEqual(boty.get_response("1"),"I am unsure what you are asking me.")
    
    def test_load_data(self):
        self.assertEqual(dl.data_load("file_does_not_exist.csv"),"Sorry! I cant come up with the words right now")

if __name__ == '__main__':
    unittest.main()
