from .base import Singleton


class AddressBook(Singleton):
    """
    Phone address book
    """
    groups = set()
    persons = set()

