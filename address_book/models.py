from .base import Singleton


class AddressBook(Singleton):
    """
    Phone address book
    """
    groups = set()
    persons = set()

class Person(object):
    """
    Person contact information
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = set()
        self.emails = set()
        self.phone_numbers = set()
        self.in_groups = set()

    def add_phone_number(self, phone_number):
        self.phone_numbers.add(phone_number)

    def add_email(self, email):
        self.emails.add(email.lower())

    def add_address(self, address):
        self.addresses.add(address)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Group(object):
    """
    Persons Group
    """

    def __init__(self, name):
        self.name = name
        self.members = set()

    def add_member(self, person):
        self.members.add(person)
        person.in_groups.add(self)
