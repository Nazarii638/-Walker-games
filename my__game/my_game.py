"""The module has one of the parts of the 'walker' game."""


class Street:
    """Class for streets"""

    def __init__(self, title: str):
        """
        Initiate parameters.
        Args:
            title (str)
        """
        self.title = title
        self.description = None
        self.neighbour_streets = []
        self.character = None
        self.thing = None

    def set_description(self, info: str):
        """
        Function for setting the description for the street
        Args:
            info (str)
        """
        self.description = info

    def connection(self, neighb_street: object, direction: str):
        """
        Function for linking the neighbour streets.
        Args:
            neighb_street (object)
            direction (str)
        """
        self.neighbour_streets.append([neighb_street.title, direction, neighb_street])

    def set_enemy(self, enemy: object):
        """
        Function for setting the character for the street.
        Args:
            enemy (object)
        """
        self.character = enemy

    def set_item(self, item: object):
        """
        Function fro setting the item for the street.
        Args:
            item (object)
        """
        self.thing = item

    def move(self, command: str):
        """
        Function for moving between the streets.
        Args:
            command (str)

        >>> kozelnytska = Street("Kozelnytska St")
        >>> franka = Street("Ivana Franka St")
        >>> kozelnytska.connection(franka, "next")
        >>> kozelnytska.move("next").title
        'Ivana Franka St'
        """
        for every in self.neighbour_streets:
            if command in every:
                return every[2]
        return self

    def get_character(self):
        """
        Function for returning the character who is located in that street.
        >>> franka = Street("Ivana Franka St")
        >>> moskal = Character("moskal")
        >>> franka.set_enemy(moskal)
        >>> franka.get_character().name
        'moskal'
        """
        return self.character

    def get_item(self):
        """
        Function for returning the item that is located in the street.
        >>> kozelnytska = Street("Kozelnytska St")
        >>> spray = Item("spray")
        >>> kozelnytska.set_item(spray)
        >>> kozelnytska.get_item().unit
        'spray'
        """
        return self.thing

    def describe(self):
        """
        Function for describing the street: title of the street and the
        description if it is not equal to None
        >>> kozelnytska = Street("Kozelnytska St")
        >>> kozelnytska.set_description("Beautiful street! There is a colegium of UCU.")
        >>> kozelnytska.describe()
        <===================>
         Kozelnytska St
        <===================>
        Beautiful street! There is a colegium of UCU.
        """
        print("<===================>")
        print(" " + self.title)
        print("<===================>")
        print(self.description)


class Character:
    """Class for characters"""

    def __init__(self, name: str):
        """
        Initiate parameters.
        Args:
            name (str)
        """
        self.name = name
        self.description = None
        self.phrase = None

    def set_description(self, description: str):
        """
        Function for setting the description of the character.
        Args:
            description (str)
        """
        self.description = description

    def set_phrase(self, phrase: str):
        """
        Function for setting the phrase for the character.
        Args:
            phrase (str)
        """
        self.phrase = phrase

    def talk(self):
        """
        If you call this function, the character will have a conversation with you.
        >>> moskal = Character("moskal")
        >>> moskal.set_phrase("Don't bite me (((")
        >>> moskal.talk()
        moskal: 'Don't bite me ((('
        """
        if self.phrase is not None:
            print(f"{self.name}: '{self.phrase}'")
        else:
            print(f"{self.name} doesn't want to talk.")

    def describe(self):
        """
        Function for printing the description in the terminal.
        >>> swindler = Robber("Swindler")
        >>> swindler.set_description("Pay attantion!")
        >>> swindler.describe()
        Swindler is here!
        Pay attantion!
        """
        print(self.name + " is here!")
        print(self.description)


class Robber(Character):
    """Class Robber has inherintance from the Character class"""

    def __init__(self, name: str):
        """
        Initiate parameters.
        Args:
            name (str)
        """
        super().__init__(name)
        self.weakness = ["pepper spray", "spray", "baseball bat", "bat", "boxing skill", "skill"]

    def fight(self, weapon: str):
        """
        Function for fighting with the character. If you win (you need to write a weapon in the
        input) the function will return True.
        >>> swindler = Robber("Swindler")
        >>> swindler.fight("spray")
        True
        """
        if weapon in self.weakness:
            return True
        return False


class Boss(Robber):
    """Class Boss has inheritance from Robber class"""

    def __init__(self, name: str):
        """
        Initiate parameters.
        Args:
            name (str)
        """
        super().__init__(name)


class Item:
    """Class for items"""

    def __init__(self, unit: str):
        """
        Initiate parameters.
        Args:
            unit (str)
        """
        self.unit = unit
        self.description = None

    def set_description(self, description: str):
        """
        Function for setting the item's description.
        Args:
            description (str)
        """
        self.description = description

    def describe(self):
        """
        Function fro describing the item.
        >>> money = Item("Money")
        >>> money.set_description("100$ for trapezna or silpo:)")
        >>> money.describe()
        Money is here.
        100$ for trapezna or silpo:)
        """
        print(self.unit + " is here.")
        print(self.description)
