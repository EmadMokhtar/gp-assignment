#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Singleton


class AddressBook(Singleton):
    """
    Phone address book is a collection of persons and groups.
    It's implemented as Singleton, so you will have one
    instance of address book in package
    """
    groups = set()
    persons = set()

    def add_person(self, person):
        """
        Add person to address book
        :param person: person object
        :type person: Person
        """
        self.persons.add(person)

    def add_group(self, group):
        """
        Add group to address book
        :param group: group object
        :type group: Group
        """
        self.groups.add(group)

    def find_person_by_name(self, search_term):
        """
        Find person by name (can supply either first name, last name, or both)
        :param search_term: either person's first name, last name, or both
        :type search_term: string
        :return: first person found
        :rtype: Person
        """
        for person in self.persons:
            if search_term.lower() in person.get_full_name().lower():
                return person

    def find_person_by_email(self, email):
        """
        Find person by email address (can supply either the exact string
        or a prefix string)
        ie. both "alexander@company.com" and "alex" should work.
        :param email: person's email an supply either the exact string
        or a prefix string
        :type email: string
        :return: first person found
        :rtype: Person
        """
        for person in self.persons:
                if email.lower() in [e[:len(email)] for e in person.emails]:
                    return person


class Person(object):
    """
    Person contact information
    A person has a first name and a last name.
    A person has one or more street addresses.
    A person has one or more email addresses.
    A person has one or more phone numbers.
    A person can be a member of one or more groups.
    """

    def __init__(self, first_name, last_name):
        """
        Initiniate Person with first_name, last_name
        :param first_name: person's first name
        :type first_name: string
        :param last_name: person's last name
        :type last_name: string
        """
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = set()
        self.emails = set()
        self.phone_numbers = set()
        self.in_groups = set()

    def add_phone_number(self, phone_number):
        """
        Add phone number to person information
        :param phone_number: person's phone number to be added
        :type phone_number: string
        """
        self.phone_numbers.add(phone_number)

    def add_email(self, email):
        """
        Add email to person information
        :param email: person's email to be added
        :type email: string
        """
        self.emails.add(email.lower())

    def add_address(self, address):
        """
        Add address to person information
        :param address: person's address to be added
        :type address: string
        """
        self.addresses.add(address)

    def get_full_name(self):
        """
        Return person's full name
        :return: person's full name
        :rtype: string
        """
        return '{} {}'.format(self.first_name, self.last_name)


class Group(object):
    """
    Persons Group
    """

    def __init__(self, name):
        """
        Initiniate Group with name
        :param name: name
        :type name: string
        """
        self.name = name
        self.members = set()

    def add_member(self, person):
        """
        Add member to the group
        :param person: person who will be a member in group
        :type person: Person
        """
        self.members.add(person)
        person.in_groups.add(self)
