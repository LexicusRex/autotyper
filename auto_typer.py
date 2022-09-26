from keyboard import keyboard
import time
from colorama import Fore, Back, Style


def auto_typer_print(filename):
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("                             PRINTING FILE                           ")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print()

    try:
        with open(filename, "r") as file:
            print("Please navigate to the textbox you wish to type in.")
            time.sleep(1.5)

            line = file.readline()
            while line:
                keyboard.write(line)
                time.sleep(2)
                keyboard.press_and_release("enter")
                line = file.readline()
    except FileNotFoundError:
        print("FILE NOT FOUND.")
        print("FILE NOT FOUND.")
        print("FILE NOT FOUND.")
        print()


def auto_typer_map(filename):
    mapping = {}
    commands = ["RUN", "EXIT"]
    try:
        with open(filename, "r") as file:
            line = file.readline()
            while line:
                line_components = line.split(" - ", 1)
                if line_components[0] not in mapping:
                    mapping[line_components[0]] = line_components[1]
                else:
                    print(f"DUPLICATE MAPPING: {line}")
                    exit()
                line = file.readline()

        while True:

            print(
                "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
            )
            print(
                "                             MAPPING FILE                            "
            )
            print(
                "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"
            )
            print()
            print("Please select command from the following")
            print("     RUN - Type out the file line by line.")
            print("     EXIT- Quit the program.")

            command = input("Input command → ")

            if command.upper() not in commands:
                print("Invalid command, please try again...")
                print()
                continue

            if command.upper() == "EXIT":
                print("MAPPING ENDED...")
                print()
                break

            print()
            map_run(mapping)

    except FileNotFoundError:
        print("FILE NOT FOUND.")
        print("FILE NOT FOUND.")
        print("FILE NOT FOUND.")
        print()


def map_run(mapping):

    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("                          MAP CHAIN INPUT                            ")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print()
    key_chain = input("Please input key chain separated by spaces: ").split(" ")
    print()
    reps = int(input("Input number of times each line repeats: "))
    print()
    print("Please navigate to the textbox you wish to type in.")
    time.sleep(3)
    for key in key_chain:
        for _ in range(reps):
            try:
                keyboard.write(mapping[key])
                keyboard.press_and_release("enter")
            except KeyError:
                print("KEY IN CHAIN INVALID...")
                print()
                break


def select_mode():
    print(
        "=============================================================================================================="
    )
    print(
        "                                                 AUTO TYPER                                                   "
    )
    print(
        "=============================================================================================================="
    )
    modes = ["PRINT", "MAP", "EXIT"]

    while True:
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("                             MODE SELECTION                          ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        print("Please select a mode from the following")
        print("     PRINT →  Type out a file line by line.")
        print(
            "     MAP   →  Select a file with a key to value mapping, then enter a series of keys to print their corresponding values."
        )
        print("     EXIT  →  Exit the program.")
        mode = input("Input mode →  ")
        print()

        if mode.upper() == "EXIT":
            print("SHUTTING DOWN...")
            print()
            break

        if mode.upper() not in modes:
            print("Invalid mode, please try again...")
            print()
            continue

        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print("                             FILE SELECTION                          ")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        print()
        filename = input("Which file would you like to open? →  ")
        print()

        if mode.upper() == "PRINT":
            auto_typer_print(filename)
        elif mode.upper() == "MAP":
            auto_typer_map(filename)


if __name__ == "__main__":
    select_mode()


# time.sleep(3)
# keyboard.write(user_input)
# time.sleep(1)
# keyboard.press_and_release('enter')
