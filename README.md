# Python Address book
This is a simple address book python implementation.

## Test

1. Install dependencies `pip install -r requirements_dev.txt`.
2. Run `nosetests` or run `nosetests --with-coverag` to run test with coverage report.

## Test Coverage

Package is 100% test Coverage

| Name                       | Stmts | Miss | Cover |
|----------------------------|-------|------|-------|
| `address_book/__init__.py` | 0     | 0    | 100%  |
| `address_book/base.py`     | 6     | 0    | 100%  |
| `address_book/models.py`   | 46    | 0    | 100%  |
|           TOTAL            | 163   | 0    | 100%  |

# Usage

## Create Person and add person to Address Book.

``` python
from address_book import models

address_book = models.AddressBook()

person = models.Person('Jack', 'Scoot')
person.add_email = 'jack@company.com'
person.add_address = 'Alex Company, Random Street'
person.add_phone_number = '999-999-9999'

address_book.add_person(person)
```

## Create person and add person to teh address book and group

``` python
from address_book import models

address_book = models.AddressBook()

person = models.Person('Jack', 'Scoot')
person.add_email = 'jack@company.com'
person.add_address = 'Alex Company, Random Street'
person.add_phone_number = '999-999-9999'

group = models.Group('Friends')
group.add_member(person)

address_book.add_person(person)
address_book.add_group(group)
```


## Create group and add group to the address book

``` python
from address_book import models

address_book = models.AddressBook()

group = models.Group('Friends')

address_book.add_group(group)
```

## Find person in address book by name

``` python
from address_book import models

address_book = models.AddressBook()

person = address_book.find_person_by_name('Jack')

print(person.get_full_name())
>>> Jack Scott
```

## Find person in address book by email

``` python
from address_book import models

address_book = models.AddressBook()

person = address_book.find_person_by_email('jack@company.com')

print(person.get_full_name())
>>> Jack Scott
```


## Address book APIs

### class `AddressBook()`
Phone address book is a collection of persons and groups. It's implemented as Singleton, so you will have one instance of address book in package

#### Attributes

##### `groups` type: `set()`
##### `persons` type: `set()`

#### Methods

##### `add_person(person)`

Add person to address book
###### parameters
* **person**: person object

##### `add_group(group)`

Add group to address book
###### parameters
* **group**: group object

##### `find_person_by_email(email)`

Find person by email address (can supply either the exact string
or a prefix string)
ie. both "alexander@company.com" and "alex" should work.
group
###### parameters
* **email**: person's email an supply either the exact string
or a prefix string

###### return
* First person found

##### `find_person_by_name(search_term)`

Find person by name (can supply either first name, last name, or both)
###### parameters
* **search_term**: either person's first name, last name, or both

###### return
* First person found

--
### class `Person()`
Person contact information

* A person has a first name and a last name.
* A person has one or more street addresses.
* A person has one or more email addresses.
* A person has one or more phone numbers.
* A person can be a member of one or more groups.

#### Attributes

##### `first_name` as `string`
##### `last_name` as `string`
##### `addresses` as `set()`
##### `emails` as `set()`
##### `phone_numbers` as `set()`
##### `in_groups` as `set()`


#### Methods

##### `add_address(address)`

Add address to person information
###### parameters
* **address**: person's address to be added

##### `add_email(email)`

Add email to person information

###### parameters
* **email**: person's email to be added

#### `add_phone_number(phone_number)`

Add phone number to person information

###### parameters
* **phone_number**: person's phone number to be added

##### `get_full_name()`
Return person's full name
###### return
* person's full name

--
### class `Group()`
Persons Group

#### Attributes

##### `name` type `string`
##### `members` type `set()`

#### Methods

##### `add_member(person)`
Add member to the group

###### parameters
* **person**: person who will be a member in group

--
# Design Question
***Find person by email address (can supply any substring, ie. "comp" should work assuming "alexander@company.com" is an email address in the address book)***

If we aggregate the persons's contact information regardless of the type of information like this:

``` python
{'contact_info': ['alexander@company.com'
                   'Alex Company, Random Street',
                   ...
                  ]
}
```

We can search for **comp** in the contact_info, or more better is creating a method that aggregate the contact information and return it as on string and search for **comp** in it, but these soltion will have big time complexity for that we can gather all of these information in text file or json file and update the file everytime user add a conntact informtaiont to the person object.
