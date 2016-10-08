import unittest
from address_book import models


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = models.AddressBook()

    def test_address_book_is_singleton(self):
        address_book = models.AddressBook()
        self.assertEqual(self.address_book, address_book)

if __name__ == '__main__':
    unittest.main()
