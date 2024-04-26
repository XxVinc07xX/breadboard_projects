from gpiozero import LED
import random
import time

led_1 = LED(24)
led_2 = LED(23)
led_3 = LED(17)
led_4 = LED(18)
led_5 = LED(14)
led_6 = LED(15)
led_7 = LED(27)

correct_led = LED(20)
wrong_led = LED(21)

def show_led(binary_string):
    for i in range(len(binary_string), 0, -1):
        led_name = f"led_{len(binary_string) - i + 1}"
        led = globals()[led_name] 
        if binary_string[i - 1] == '1':  
            led.on()
        else:
            led.off()

def all_off():
    for i in range(7):
        led_name = f"led_{i+1}"
        led = globals()[led_name] 
        led.off()


def correct_ans():
    correct_led.on()
    time.sleep(1)
    correct_led.off()

def wrong_ans():
    wrong_led.on()
    time.sleep(1)
    wrong_led.off()

def end_game():
    wrong_led.blink(background=False, n=10,on_time=0.2,off_time=0.2)

def end_game_win():
    correct_led.blink(background=False, n=30,on_time=0.1,off_time=0.1)

def next_level():
    correct_led.blink(background=False, n=3,on_time=0.1,off_time=0.1)

if __name__ == "__main__":
    print("\nWelcome to the game in which you have to guess the number showed on your raspberry!\nHope you get better at binary counting!\nEnjoy!")

    in_game = 1

    #====LEVEL 1====
    #easy level, numbers will be between 1 and 15
    print("\nWelcome to the easy level.\n")
    for i in range(5):
        if (in_game == 1):
            rd = random.randint(1,15)
            all_off()
            rd_bin_brut = bin(rd)
            rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
            #print(rd_bin)
            show_led(rd_bin)
            chance = 0

            while True:

                user_input = input("What is this number? : ")

                try:
                    user_input_int = int(user_input)
                    if user_input_int == rd:
                        print("Good answer! On to the next one\n")
                        if (i == 4):
                            next_level()
                        else:
                            correct_ans()
                        break
                    else:
                        chance += 1
                        if (chance == 3):
                            print("Sorry, you don't succeed this time...\nSee you later!")
                            in_game = 0
                            end_game()
                            break
                        else:
                            str_out = "Chance(s) left: "  + str(3-chance)
                            wrong_ans()
                            print("Wrong answer, try again...\n" + str_out + "\n")
                except ValueError:
                    print("Wrong input format, please enter an integer\n")

    #intermediate level, numbers will be between 16 and 31
    if (in_game == 1):
        print("\n==============================\nWelcome to the intermediate level. \nHere things start to be more spicy!\n")
        for i in range(7):
            if (in_game == 1):
                rd = random.randint(16,31)
                all_off()
                rd_bin_brut = bin(rd)
                rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
                #print(rd_bin)
                show_led(rd_bin)
                chance = 0

                while True:

                    user_input = input("What is this number? : ")

                    try:
                        user_input_int = int(user_input)
                        if (user_input_int == rd):
                            print("Good answer! On to the next one\n")
                            if (i == 6):
                                next_level()
                            else:
                                correct_ans()
                            break
                        else:
                            chance += 1
                            if (chance == 2):
                                print("Sorry, you don't succeed this time...\nSee you later!")
                                end_game()
                                in_game = 0
                                break
                            else:
                                str_out = "Chance left: "  + str(2-chance)
                                wrong_ans()
                                print("Wrong answer, try again...\n" + str_out + "\n")
                    except:
                        print("Wrong input format, please enter an integer\n")

    #hard level, number will be between 32 and 255
    if (in_game == 1):
        print("\n==============================\nWelcome to the boss level! \nKeep calm and good luck.. \nIf you succeed at this level, you're the boss at binary counting\n")

        for i in range(12):
            if (in_game == 1):
                rd = random.randint(32,127)
                all_off()
                rd_bin_brut = bin(rd)
                rd_bin = rd_bin_brut[rd_bin_brut.index('b')+1:]
                #print(rd_bin)
                show_led(rd_bin)
                
                while True:

                    user_input = input("What is this number? : ")

                    try:
                        user_input_int = int(user_input)
                        if (user_input_int == rd):
                            if (i == 10):
                                print("And one last to be the boss...\n")
                                correct_ans()
                            elif (i == 11):
                                print("CONGRATULATIONS!")
                                correct_ans()
                            else:
                                print("Good answer! On to the next one\n")
                                correct_ans()
                            break
                        else:
                            print("Wrong answer, try again...\n")
                            in_game = 0
                            end_game()
                            break
                    except:
                        print("Wrong input format, please enter an integer\n")

    if (in_game == 1):
        end_game_win()
        print("YOU'RE THE BOSS AT BINARY COUNTING")
                


