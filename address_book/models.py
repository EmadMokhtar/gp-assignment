from .base import Singleton


class AddressBook(Singleton):
    """
    Phone address book
    """
    groups = set()
    persons = set()

    def add_person(self, person):
        self.persons.add(person)

    def add_group(self, group):
        self.groups.add(group)

    def find_person_by_name(self, search_term):
        for person in self.persons:
            if search_term.lower() in person.get_full_name().lower():
                return person

    def find_person_by_email(self, email):
        for person in self.persons:
                if email.lower() in [e[:len(email)] for e in person.emails]:
                    return person


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
