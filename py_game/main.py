import Game

game1 = Game.Game()

player_name = game1.greet_name()

while True:
    choice = game1.choose_module()

    if choice == 1:
        game1.display_rules()
        game1.run_numbers_module()
    elif choice == 2:
        game1.display_rules()
        game1.run_colours_module()
    elif choice == 3:
        game1.display_rules()
        game1.run_animals_module()
    elif choice == 4:
        print("Thanks for playing. Goodbye!")
        exit()
    else:
        print("Invalid module choice. Please try again")