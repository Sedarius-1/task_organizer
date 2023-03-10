import hashlib
import unittest

import bcrypt

import classes
import queries
import tasks


class MyTestCase(unittest.TestCase):

    def test_register(self):
        test_uzytkownik = classes.Uzytkownik("test", "test")
        hashed=tasks.hashPassword(test_uzytkownik.haslo)
        print(hashed)

    def test_something(self):
        test_uzytkownik = classes.Uzytkownik("test", "test")
        hashed_pass_dict = tasks.hashPassword(test_uzytkownik.haslo)
        self.assertTrue(tasks.loginTry(test_uzytkownik, hashed_pass_dict[0].decode('utf-8'), hashed_pass_dict[1].decode('utf-8')))

    def test_password(self):
        uzytkownik_test = classes.Uzytkownik("testtest", "test")



if __name__ == '__main__':
    unittest.main()
