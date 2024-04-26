import random


if __name__ == "__main__":

    print("\nWelcome to the game in which you have to guess the number showed on your terminal!\nHope you get better at binary counting!\nEnjoy!")

    in_game = 1

    #====LEVEL 1====
    #easy level, numbers will be between 1 and 15
    print("\nWelcome to the easy level.\n")
    for _ in range(5):
        if (in_game == 1):
            rd = random.randint(1,15)
            rd_bin_brut = bin(rd)
            rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
            print(rd_bin)
            chance = 0

            while True:

                user_input = input("What is this number? : ")

                try:
                    user_input_int = int(user_input)
                    if user_input_int == rd:
                        print("Good answer! On to the next one\n")
                        break
                    else:
                        chance += 1
                        if (chance == 3):
                            print("Sorry, you don't succeed this time...\nSee you later!")
                            in_game = 0
                            break
                        else:
                            str_out = "Chance(s) left: "  + str(3-chance)
                            print("Wrong answer, try again...\n" + str_out + "\n")
                except ValueError:
                    print("Wrong input format, please enter an integer\n")

    #intermediate level, numbers will be between 16 and 31
    if (in_game == 1):
        print("\n==============================\nWelcome to the intermediate level. \nHere things start to be more spicy!\n")
        for _ in range(7):
            if (in_game == 1):
                rd = random.randint(16,31)
                rd_bin_brut = bin(rd)
                rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
                print(rd_bin)
                chance = 0

                while True:

                    user_input = input("What is this number? : ")

                    try:
                        user_input_int = int(user_input)
                        if (user_input_int == rd):
                            print("Good answer! On to the next one\n")
                            break
                        else:
                            chance += 1
                            if (chance == 2):
                                print("Sorry, you don't succeed this time...\nSee you later!")
                                in_game = 0
                                break
                            else:
                                str_out = "Chance left: "  + str(2-chance)
                                print("Wrong answer, try again...\n" + str_out + "\n")
                    except:
                        print("Wrong input format, please enter an integer\n")

    #hard level, number will be between 32 and 255
    if (in_game == 1):
        print("\n==============================\nWelcome to the boss level! \nKeep calm and good luck.. \nIf you succeed at this level, you're the boss at binary counting\n")

        for i in range(12):
            if (in_game == 1):
                rd = random.randint(32,255)
                rd_bin_brut = bin(rd)
                rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
                print(rd_bin)

                while True:

                    user_input = input("What is this number? : ")

                    try:
                        user_input_int = int(user_input)
                        if (user_input_int == rd):
                            if (i == 11):
                                print("And one last to be the boss...\n")
                            elif (i == 1):
                                print("CONGRATULATIONS!")
                            else:
                                print("Good answer! On to the next one\n")
                            break
                        else:
                            print("Wrong answer, try again...\n")
                            in_game = 0
                            break
                    except:
                        print("Wrong input format, please enter an integer\n")

    if (in_game == 1):
        print("YOU'RE THE BOSS AT BINARY COUNTING")
                


