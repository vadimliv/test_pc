import unittest
from unittest import TestCase, skipIf


class TestPerson(TestCase):
    def test_person(self):
        self.assertTrue(3 == 4, 'should be true')

    @skipIf(3 == 4, 'just')
    def test_new(self):
        self.assertEqual(2, 2, 'should be equal')


if __name__ == '__main__':
    unittest.main()
