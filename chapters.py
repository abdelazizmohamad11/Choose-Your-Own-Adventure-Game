import random

# import the colorama module
import colorama
from colorama import Fore

from music_player import *
from GUI.GUI import GUIInstance

colorama.init(convert=True)

# start the game

# NOT CALLED ANYWHERE
def start():
    if GUIInstance.ask_question("You are on a dirt road. Which way do you want to go left or right?", "Left", "Right"):
        random.choice(my_list)()
    else:
        random.choice(my_list)()


def chapter_river():
    if GUIInstance.ask_question("You come to a river, you can walk around it or swim across.", "Walk", "Swim"):
        # 1. Walk
        # Feedback for choosing to walk
        GUIInstance.text_until_enter("You chose to walk around the river.")
        if GUIInstance.ask_question("You walked for many miles, ran out of water and remembered that there was a shop far away which supplies water. Do you want to go there?", "Yes", "No"):
            # 2. Yes
            # Feedback for choosing to go to the shop
            GUIInstance.text_until_enter("You decided to go to the shop for water.")
            if GUIInstance.ask_question("You went 10 miles walking and bought 10 liters of drinking water. Do you want to drink the water?", "Yes", "No"):
                # 3. Yes
                # Feedback for choosing to drink water
                GUIInstance.text_until_enter("You drank 5 liters of water and now you feel refreshed.")
                if GUIInstance.ask_question("Do you want to walk further or go back home?", "Further", "Home"):
                    # 4. Further
                    # Feedback for choosing to walk further
                    GUIInstance.text_until_enter("You decided to walk further.")
                    game_over("You walked 100 more miles and you WIN the game! \U0001f3c6", win=True)
                else:
                    # 4. Home
                    # Feedback for choosing to go home
                    GUIInstance.text_until_enter("You chose to go back home.")
                    game_over("A car crashed you and you were rushed to hospital. Although, it was too late by the time you reached the hospital, and you had already died. \U0001F480")

            else:
                # 3. No
                # Feedback for choosing not to drink water
                GUIInstance.text_until_enter("You decided not to drink the water.")
                game_over("You died of thirst.\U0001F480")

        else:
            # 2. No
            # Feedback for choosing not to go to the shop
            GUIInstance.text_until_enter("You chose not to go to the shop.")
            game_over("You were very de-hydrated and died of thirst when you were walking. \U0001F480")

    else:
        # 1. Swim
        # Feedback for choosing to swim
        GUIInstance.text_until_enter("You chose to swim across the river.")
        game_over("You swam across the river and were eaten by an aligator \U0001F480")



def chapter_bridge():
    if GUIInstance.ask_question("You come to a bridge, it looks wobbly. Do you want to cross it or do you want to head back?", "Cross", "Back"):
        # 1. Cross
        # Feedback for crossing the bridge
        GUIInstance.text_until_enter("You chose to cross the bridge.")
        chapter_stranger()

    else:
        # 1. Back
        # Feedback for heading back
        GUIInstance.text_until_enter("You decided to go back.")
        if GUIInstance.ask_question("You go back to the main road. Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            # Feedback for going forward
            GUIInstance.text_until_enter("You decided to go forward.")
            game_over("You drive forward and crash into a tree and die.\U0001F480")
        else:
            # 2. Left
            # Feedback for going left
            GUIInstance.text_until_enter("You decided to go left.")
            chapter_lake()


def chapter_stranger():
    if GUIInstance.ask_question("You cross the bridge and meet a stranger, do you talk to them?", "Yes", "No"):
        # 1. Yes
        GUIInstance.text_until_enter("You decided to talk to the stranger.")
        if GUIInstance.ask_question("You talk to a wizard, and he asks you, do you want to be a wizard?", "Yes", "No"):
            # 2. Yes
            GUIInstance.text_until_enter("You decided to be a wizard.")
            game_over("You become a wizard and WIN the game! \U0001f3c6", win=True)
        else:
            # 2. No
            GUIInstance.text_until_enter("You decided to not be a wizard.")
            game_over("The stranger was not pleased by you and murdered you. \U0001F480")
    else:
        # 1. No
        GUIInstance.text_until_enter("You decided not to talk to the stranger.")
        game_over("The stranger was not pleased by you and murdered you. \U0001F480")


def chapter_mountain():
    if GUIInstance.ask_question("You reached a mountain. Do you want to climb it?", "Yes", "No"):
        # 1. Yes
        GUIInstance.text_until_enter("You decided to climb the mountain.")
        if GUIInstance.ask_question("You start climbing the mountain. You see a rope bridge ahead. Do you want to cross it?", "Yes", "No"):
            # 2. Yes
            GUIInstance.text_until_enter("You decided to cross the rope.")
            game_over("You walk on the bridge, but suddenly it collapses. You fall to the ground and die \U0001F480")
        else:
            # 2. No
            GUIInstance.text_until_enter("You decided to not cross the rope.")
            if GUIInstance.ask_question("Do you want to continue climbing or go back down?", "Climb", "Back"):
                # 3. Climb
                GUIInstance.text_until_enter("You decided to keep climbing the mountain.")
                game_over("You climb the mountain for many days, and you finally reach the top. You WIN the game! \U0001f3c6", win=True)
            else:
                # 3. Back
                GUIInstance.text_until_enter("You safely decide to climb back down.")
                random.choice(my_list)()

    else:
        # 1. No
        GUIInstance.text_until_enter("You decided not to climb the mountain.");
        random.choice(my_list)()


def chapter_lake():
    if GUIInstance.ask_question("You turned left and come to a lake, do you want to swim or go back?", "Swim", "Back"):
        # 1. Swim
        GUIInstance.text_until_enter("You decided to swim across the lake.")
        game_over("You swam across the lake and were eaten by a shark. \U0001F480 ")
    else:
        # 1. Back
        GUIInstance.text_until_enter("You chose to go back to the main road.")
        if GUIInstance.ask_question("Now you can decide to drive forward or turn left.", "Forward", "Left"):
            # 2. Forward
            GUIInstance.text_until_enter("You decided to drive forward.")
            game_over("You died. \U0001F480")
        else:
            # 2. Left
            GUIInstance.text_until_enter("You decided to turn left.")
            chapter_tree()


def chapter_tree():
    if GUIInstance.ask_question("You are very hungry and you see a tree with apples, do you want to eat the fruit?", "Yes", "No"):
        # 1. Yes
        GUIInstance.text_until_enter("You decided to eat the apples.")
        game_over("You ate the fruit but it was poisonous and you died. \U0001F480")
    else:
        # 1. No
        GUIInstance.text_until_enter("You chose not to eat the apples.")
        if GUIInstance.ask_question("You are nearly starving to death. Do you want to eat Pears instead of apples?", "Yes", "No"):
            # 2. Yes
            GUIInstance.text_until_enter("You decided to eat the pears.")
            game_over("You ate the pears but they were poisonous and you died. \U0001F480")
        else:
            # 2. No
            GUIInstance.text_until_enter("You refused to eat anything.")
            game_over("You were super hungry and nearly died, but a lovely gentleman gave you some food and you WIN the game! \U0001f3c6", win=True)


def game_over(message: str = None, *, win=False):
    "Shows Game over message"
    if not GUIInstance.run_gui:
        # No gui
        if win:
            print(Fore.YELLOW + message)
        else:
            print(Fore.RED + message)

    elif message:
        # Gui and message
        GUIInstance.text_until_enter(message)

    if GUIInstance.ask_question("Thanks for playing!", "Play Again", "Quit"):
        # Play again
        random.choice(my_list)()
    else:
        # Quit
        GUIInstance.exit_func()


my_list = [chapter_bridge, chapter_lake, chapter_mountain, chapter_river]
