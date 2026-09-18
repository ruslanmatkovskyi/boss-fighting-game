import random

try:
    while True:
        round_count = 1
        player_hp = 100
        boss_hp = 150

        print("Boss fighting game!")
        menu_select = int(input("1. Start\n2. Exit\n\n"))

        if menu_select == 2:
            print("Good bye!")
            break

        else:
            while True:

                print(f"Round {round_count}\nPlayer's HP: {player_hp}\nBosse's HP: {boss_hp}")
                act = int(input("1 --- Attack\n2 --- Heal Up\n3 --- Run away\n"))

                match act:
                    case 1:
                        boss_hp -= random.randint(10, 30)
                        if player_hp <= 0:
                                                        
                            print("Game over! Player has failed. Boss has winned.\n")
                            break

                        elif boss_hp <= 0:
                                        
                            print("You winned! Boss has failed. Player win!\n")
                            break

                    case 2:
                        player_hp += random.randint(10, 25)
                        if player_hp > 100:
                            player_hp = 100

                    case 3:
                        print("Game over! You ran away...\n")
                        break

                    case _:
                        print("Invalid select! You haven't acted\n")

                boss_attack = random.randint(5, 20)
                player_hp -= boss_attack
                print(f"Boss has hitted you {boss_attack} HP!\n")

                if player_hp <= 0:
                                                                        
                    print("Game over! Player has failed. Boss has winned.\n")
                    break
                
                elif boss_hp <= 0:
                                                        
                    print("You winned! Boss has failed. Player win!\n")
                    break

                round_count += 1

except ValueError:
    print("Input must be valid! Exiting app...")

except KeyboardInterrupt:
    print("\nExiting Programm...")
