from model import func, reverse_string
import unittest

funct = func()


class TestFunc(unittest.TestCase):
    def test_rev_str(self):
        self.assertEqual(reverse_string('nika'), 'akin')

    def test_not_rev_str(self):
        self.assertNotEqual(reverse_string('nika'), 'aakin')

    def test_is_palindrome(self):
        funct = func()
        self.assertEqual(funct.is_palindrome('ana'), True)

    def test_not_is_palindrome(self):
        funct = func()
        self.assertNotEqual(funct.is_palindrome('nika'), True)

    def test_capitalize_words(self):
        funct = func()
        self.assertEqual(funct.capitalize_words('aaa'), 'Aaa')

    def test_not_capitalize_words(self):
        funct = func()
        self.assertNotEqual(funct.capitalize_words('aaa'), 'aaa')

    def test_celsius_to_fahrenheit(self):
        funct = func()
        self.assertEqual(funct.celsius_to_fahrenheit(0), 32)

    def test_not_celsius_to_fahrenheit(self):
        funct = func()
        self.assertNotEqual(funct.celsius_to_fahrenheit(0), 33)

    def test_fahrenheit_to_celsius(self):
        funct = func()
        self.assertEqual(funct.fahrenheit_to_celsius(32), 0)

    def test_not_fahrenheit_to_celsius(self):
        funct = func()
        self.assertNotEqual(funct.fahrenheit_to_celsius(33), 0)



def test_is_palindrome():
    assert funct.is_palindrome('ana') == True

def test_not_is_palindrome():
    assert funct.is_palindrome('nika') == False

def test_fahrenheit_to_celsius():
     assert funct.fahrenheit_to_celsius(32)== 0

def test_not_fahrenheit_to_celsius():
    assert funct.fahrenheit_to_celsius(33) != 0

def test_celsius_to_fahrenheit():
    assert funct.celsius_to_fahrenheit(0) ==  32

def test_not_celsius_to_fahrenheit():
    assert funct.celsius_to_fahrenheit(1) !=  32

def test_capitalize_words():
    assert funct.capitalize_words('aaa') == 'Aaa'

def test_not_capitalize_words():
    assert funct.capitalize_words('aaa') != 'AAa'

def test_rev_str():
    assert reverse_string('nika') =='akin'

def test_not_rev_str():
    assert reverse_string('nika') !='ain'