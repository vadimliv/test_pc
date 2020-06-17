from unittest import TestCase, skipIf


class TestPerson(TestCase):
    def test_person(self):
        self.assertTrue(3 == 3)

    @skipIf(3 == 3, 'just')
    def test_new(self):
        self.assertEqual(2, 2)
