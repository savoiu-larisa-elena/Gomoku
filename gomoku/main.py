from ui.ui import UI
from gui.gui import GUI
from domain.humanPlayer import Player

if __name__ == "__main__":

    print("Welcome to Gomoku!\n")

    difficulty = input("Please enter the difficulty level (easy, medium, hard): \n")
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        print("Invalid difficulty, please try again")
        difficulty = input("Please enter the difficulty level (easy, medium, hard): \n")

    size = int(input("Please enter the size of the board (15 or 19): \n"))
    while size != 15 and size != 19:
        print("Invalid size, please try again")
        size = int(input("Please enter the size of the board (15 or 19): \n"))

    playerName = input("Enter your name: ")

    """ this creates the player """
    player = Player(playerName, "X", difficulty)

    print("Please choose: \n"
          "\t1. UI\n"
          "\t2. GUI\n")
    choice = input("Enter your choice: ")

    while choice != "1" and choice != "2":
        print("Invalid choice, please try again")
        print("Please choose: \n"
                "\t1. UI\n"
                "\t2. GUI\n")
        choice = input("Enter your choice: ")

    if choice == "1":
        ui = UI(size, difficulty, player)
        ui.run(player)

    elif choice == "2":
        gui = GUI(size, difficulty, player)
        gui.run()