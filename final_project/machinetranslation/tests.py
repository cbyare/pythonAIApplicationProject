import unittest

from machinetranslation.translator import englishToFrench, frenchToEnglish
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when the input is Hello
        message = "Test value is not none."
        self.assertIsNotNone(englishToFrench(None), message)  #test when the input is null
        


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when the input is Bonjour
        message = "Test value is not none."
        self.assertIsNotNone(frenchToEnglish(None), message) # test when the input is null
        
unittest.main()