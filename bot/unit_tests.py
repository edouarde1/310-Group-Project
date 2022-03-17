import unittest
import bot

#TODO update testclass, make sure this shit actually runs tests. 
class TestClass(unittest.TestCase):
    def test_spell_check(self):
        #TODO: Add 2 more test cases
        #self.assertEqual(bot.spell_check("tdll md wdy"), ["tell me why"])
        #self.assertEqual(bot.spell_check("ain't nothin but a heartche"),["ain't nothing but a heartache"])
        #self.assertEqual(bot.spell_check("I nevr wanna hear yu say "),["I never wanna hear you say"])
        #print(bot.spell_check("tdll md wdy ain't nothin but a heartche I nevr wanna hear yu say "))
        #I want it that way! 
        print("test")
        return True

    def test_get_response(self):
        # TODO: Use bot get_response to test 3 inputs
        print("test")
        return False
        # keywords = data_utils.data_load.load_data("keywords.csv")
        # self.assertEqual(bot.get_response("1", keywords), "Sorry I did not understand what you said")

    def test_load_data(self):
        # TODO: Test json data loading
        # self.assertEqual(load_data("file_does_not_exist.csv"), "Sorry! I cant come up with the words right now")
        return False

    def test_syn_detection(self):
        # TODO: Test synonyms for 3 commonly used words
        return False

if __name__ == '__main__':
    unittest.main()
