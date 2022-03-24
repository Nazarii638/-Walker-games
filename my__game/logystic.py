"""The module has one of the parts of the 'walker' game."""
import my_game


kozelnytska = my_game.Street("Kozelnytska St")
kozelnytska.set_description("Beautiful street! There is a colegium of UCU.")

franka = my_game.Street("Ivana Franka St")
franka.set_description("There is very dark at night, however there is Ivan's Franko house.")

rustaveli = my_game.Street("Shota Rustaveli St")
rustaveli.set_description("Wow, handsome street. But there is an awful congestion.")

knaiaz = my_game.Street("Kniazia Romana St")
knaiaz.set_description("It is very narrow street.")

svobody = my_game.Street("Svobody Ave")
svobody.set_description("This place is fascinating, incredibly beautiful!")

kozelnytska.connection(franka, "next")
franka.connection(kozelnytska, "previous")
franka.connection(rustaveli, "next")
rustaveli.connection(franka, "previous")
rustaveli.connection(knaiaz, "next")
knaiaz.connection(rustaveli, "previous")
knaiaz.connection(svobody, "next")
svobody.connection(knaiaz, "previous")

moskal = my_game.Character("moskal")
moskal.set_description("he is coward and ork like other people from moscovia.")
moskal.set_phrase("Don't bite me (((")
franka.set_enemy(moskal)

swindler = my_game.Robber("Swindler")
swindler.set_description("Pay attantion!")
swindler.set_phrase("Oh, did you make money for me?)")
rustaveli.set_enemy(swindler)

boss = my_game.Boss("Boss")
boss.set_description("Boss has a lot of health and he is angry :|")
svobody.set_enemy(boss)

spray = my_game.Item("spray")
spray.set_description("Pepper spray can help you when you are fighting with someone.")
kozelnytska.set_item(spray)

bat = my_game.Item("bat")
bat.set_description("Baseball bat can help you when you are fighting with someone.")
franka.set_item(bat)

skill = my_game.Item("skill")
skill.set_description("Boxing skill can help you when you are fighting with someone.")
rustaveli.set_item(skill)

money = my_game.Item("Money")
money.set_description("100$ for trapezna or silpo:)")
knaiaz.set_item(money)

exam = my_game.Item("40 points")
exam.set_description("These points you can use for any exam.")
svobody.set_item(exam)

print("Hello, this is a 'walker' game. Your main aim is to put the prize('40 points' - for \
exams :) )in your bag and come back to the place where you were started. But for taking the main \
prize, you need to win the Boss, firstly. He has a lot of health, so you should have minimum two \
weapons on your bag. The program has following inputs: 'next'(go to the next street), 'previous'\
(go to the previous street), 'take'(put the item in the bag), 'talk'(talk with the character), \
'fight'(fight with the character) and the items that you have in the bag.", end="\n")
print()
print("For leaving the game, please, write 'q' or 'quit'.")


def user_input():
    print("What will you fight with?")
    user_data = input(">>> ")
    if user_data == "q" or user_data == "quit":
        exit()
    return user_data

current_street = kozelnytska

bag = []

alive = True

while alive:

    print("\n")

    current_street.describe()  # print info

    person = current_street.get_character()  # get character who is in the street
    if person is not None:
        person.describe()  # print info about person

    thing = current_street.get_item()  # get item
    if thing is not None:
        thing.describe()  # info about the item

    command = input(">>> ")

    if command == "q" or command == "quit":
        exit()

    if command in ["previous", "next"]:
        current_street = current_street.move(command)

    elif command == "talk":
        if person is not None:
            person.talk()
        else:
            print("There is no one to talk with!")

    elif command == "take":
        if thing is not None:
            if isinstance(person, my_game.Boss):
                print("Firstly, you need to win the Boss.")
            else:
                print(f"You put the {thing.unit} in the bag.")
                bag.append(thing.unit)
                current_street.set_item(None)
        else:
            print("There is nothing to take!")

    elif command == "fight":
        if person is not None:
            if isinstance(person, my_game.Boss):
                indicators = []
                print("For defeating the Boss you need use two weapons, because he")
                print("has a lot of health. You will have two inputs. Please, write in turn.")
                for num in range(2):
                    user_weapon = user_input()
                    if user_weapon in bag:
                        indicators.append(person.fight(user_weapon))
                    else:
                        print(f"You don't have a {user_weapon} in the bag.")
                if indicators == [True, True]:
                    print("Congratulations! You defeated the Boss. Now you can take the prize")
                    print("and go to the point from which you started for winning the game!")
                    current_street.set_enemy(None)
                else:
                    print("Ohhh dear, I know that you were trying a lot,")
                    print("but, unfortunately, you lose. Good luck!")
                    alive = False

            elif isinstance(person, my_game.Robber):
                user_weapon = user_input()
                if user_weapon in bag:
                    if person.fight(user_weapon) is True:
                        print(f"Congratulations! You defeated the {person.name}.")
                        print("You are on the right way.")
                        current_street.set_enemy(None)
                    else:
                        print("You lose the fight :(")
                        print("Good luck!")
                        alive = False
                else:
                    print(f"You don't have a {user_weapon} in the bag.")

            else:
                print(f"Congratulations! You defeated the {person.name}, because")
                print(f"you don't need anything to fight with him.")
                current_street.set_enemy(None)
        else:
            print("There is no one to fight with!")

    else:
        print(f"The game has no action: {command}")

    if current_street.title == "Kozelnytska St" and "40 points" in bag:
        print("Congratulations!!! You won the game and recieved the main prize - '40 points' \
for the exam! Good luck!")
        alive = False
