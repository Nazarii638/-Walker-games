"""This program is the one part of the game.('main.py')"""


class Room:
    """Class Room"""
    def __init__(self, name_of_room: str):
        """
        Initiate parameters.
        Args:
            name_of_room (str)
        """
        self.name_of_room = name_of_room
        self.description = None
        self.neighbour_rooms = []
        self.character = None
        self.items = None

    def set_description(self, description):
        """
        Function that sets the description of the room.
        Args:
            description (str)
        """
        self.description = description

    def link_room(self, room, direction):
        """
        Function that assigns direction for neighbour room.
        Args:
            room (object)
            direction (str)
        """
        self.neighbour_rooms.append([room.name_of_room, direction, room])

    def set_character(self, name):
        """
        Function that places character into room.
        Args:
            name (object)
        """
        self.character = name

    def set_item(self, item_name):
        """
        Function that places item into room.
        Args:
            item_name (object)
        """
        self.items = item_name

    def get_details(self):
        """Function that prints information about the room."""
        print(self.name_of_room)
        print("--------------------")
        print(self.description)
        print("\n".join([f"The {every[0]} is {every[1]}" for every in self.neighbour_rooms]))

    def get_character(self):
        """
        Function that returns the character which is in the room.
        >>> kitchen = Room("Kitchen")
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> kitchen.set_character(dave)
        >>> kitchen.get_character().name
        'Dave'
        """
        return self.character

    def get_item(self):
        """
        Function that returns the item which is in the room.
        >>> kitchen = Room("Kitchen")
        >>> book = Item("book")
        >>> kitchen.set_item(book)
        >>> kitchen.get_item().name_of_item
        'book'
        """
        return self.items

    def move(self, command):
        """
        Function for moving into different rooms.
        >>> kitchen = Room("Kitchen")
        >>> dining_hall = Room("Dining Hall")
        >>> kitchen.link_room(dining_hall, "south")
        >>> kitchen.move("south").name_of_room
        'Dining Hall'
        """
        for each in self.neighbour_rooms:
            if command == each[1]:
                return each[2]
        return None


class Enemy:
    """Class Enemy"""
    wins = []

    def __init__(self, name, description):
        """
        Initiate parameters.
        Args:
            name (str)
            description (str)
        """
        self.name = name
        self.description = description
        self.phrase = None
        self.weakness = None

    def set_conversation(self, phrase):
        """
        Function for setting a phrase for character.
        Args:
            phrase (str)
        """
        self.phrase = phrase

    def set_weakness(self, weakness):
        """
        Function for setting a weakness for character.
        Args:
            weakness (str)
        """
        self.weakness = weakness

    def describe(self):
        """Function for describing the character."""
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        """Function that prints character's phrase."""
        print(f"[{self.name} says]: {self.phrase}")

    def fight(self, thing):
        """
        Function that checkes whether you can win the character
        with certain thing that you choose.
        Args:
            thing (str)
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("onion")
        >>> dave.fight("wrist")
        Dave crushes you, puny adventurer!
        False
        """
        if self.weakness == thing:
            Enemy.wins.append("+")
            print(f"You fend {self.name} off with the {thing}")
            return True
        print(f"{self.name} crushes you, puny adventurer!")
        return False

    def get_defeated(self):
        """
        Function that counts the amount of your wins.
        >>> dave = Enemy("Dave", "A smelly zombie")
        >>> dave.set_weakness("onion")
        >>> dave.get_defeated()
        0
        >>> dave.fight("onion")
        You fend Dave off with the onion
        True
        >>> dave.get_defeated()
        1
        """
        return len(Enemy.wins)


class Item:
    """Class Item"""
    def __init__(self, name_of_item):
        """
        Initiate parameters.
        Args:
            name_of_item (str)
        """
        self.name_of_item = name_of_item
        self.item_description = None

    def set_description(self, sentence):
        """
        Function for setting the descriptionfro item.
        Args:
            sentence (str)
        """
        self.item_description = sentence

    def describe(self):
        """Function that prints the information about the item."""
        print(f"The [{self.name_of_item}] is here - {self.item_description}")

    def get_name(self):
        """
        Function that returns the name of the item.
        >>> book = Item("Book")
        >>> book.get_name()
        'Book'
        """
        return self.name_of_item
