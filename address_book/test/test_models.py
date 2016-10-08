import unittest
from address_book import models


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = models.AddressBook()

    def test_address_book_is_singleton(self):
        address_book = models.AddressBook()
        self.assertEqual(self.address_book, address_book)

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = models.Person('Dummy', 'Person')

    def test_initialize_person(self):
        first_name = 'Emad'
        last_name = 'Mokhtar'
        person = models.Person(first_name, last_name)
        self.assertIsNotNone(person)
        self.assertEqual(person.last_name, last_name)
        self.assertEqual(person.first_name, first_name)
        self.assertIsInstance(person, models.Person)

    def test_add_phone_number(self, phone_number='999-999-999'):
        self.person.add_phone_number(phone_number)
        self.assertIn(phone_number, self.person.phone_numbers)

    def test_add_duplicate_phone_number(self, phone_number='999-999-999'):
        self.person.add_phone_number(phone_number)
        self.person.add_phone_number(phone_number)
        self.assertEqual(1, len(self.person.phone_numbers))

    def test_add_email(self, email='email@company.com'):
        self.person.add_email(email)
        self.assertIn(email, self.person.emails)

    def test_add_duplicate_email(self, email='email@company.com'):
        self.person.add_email(email)
        self.person.add_email(email)
        self.assertEqual(1, len(self.person.emails))

    def test_add_address(self, address='Inifite Loop, Apple'):
        self.person.add_address(address)
        self.assertIn(address, self.person.addresses)

    def test_add_duplicate_address(self, address='Inifite Loop, Apple'):
        self.person.add_address(address)
        self.person.add_address(address)
        self.assertEqual(1, len(self.person.addresses))

    def test_get_full_name(self):
        self.assertEqual(self.person.get_full_name(), 'Dummy Person')

    def test_get_groups_perosn_belongs_to(self):
        family_group = models.Group('Family')
        close_family_group = models.Group('Close Family')
        friends_group = models.Group('Firends')
        close_friends_group = models.Group('Firends')
        brother = models.Person('Sam', 'Albert')
        best_friend = models.Person('Kenneth', 'Boyce')
        family_group.add_member(brother)
        close_family_group.add_member(brother)
        friends_group.add_member(best_friend)
        close_friends_group.add_member(best_friend)

        self.assertEqual(brother.in_groups,
                         set([family_group, close_family_group]))
        self.assertEqual(best_friend.in_groups,
                         set([friends_group, close_friends_group]))


class TestGroup(unittest.TestCase):
    def setUp(self):
        self.group = models.Group('Group')

    def test_initialize_group(self):
        group_name = 'Family'
        group = models.Group(group_name)
        self.assertIsNotNone(group)
        self.assertEqual(group.name, group_name)
        self.assertIsInstance(group, models.Group)

    def test_add_person_to_group(self):
        person = models.Person('Dummy', 'Person')
        self.group.add_member(person)
        self.assertEqual(1, len(self.group.members))

    def test_get_persons_in_group(self):
        family_group = models.Group('Family')
        friends_group = models.Group('Firends')
        brother = models.Person('Sam', 'Albert')
        sister = models.Person('Susan', 'Albert')
        friend_1 = models.Person('Kenneth', 'Boyce')
        friend_2 = models.Person('Brandon', 'Crawley')
        family_group.add_member(brother)
        family_group.add_member(sister)
        friends_group.add_member(friend_1)
        friends_group.add_member(friend_2)

        self.assertEqual(family_group.members, set([brother, sister]))
        self.assertEqual(friends_group.members, set([friend_1, friend_2]))


if __name__ == '__main__':
    unittest.main()
