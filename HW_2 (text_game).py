import random
from time import sleep
import os


def main():
    print("Welcome!")
    # sleep(1)
    print("This is a simple lifecycle game :)")
    # sleep(1)
    raw_input("Press any key to continue...")

    # General variables:
    choice = None
    locations_list = ['America', 'Europe', 'Asia']
    relationships = None
    love = None
    exams_pass_perc = 85  # start value (may change during the game)
    const_increase = 5
    universities = list()
    univer_choice = None

    while type(choice) is not int:
        os.system('clear')
        print("Chose your character:")
        print("1) Human")
        print("2) Dog")
        print("3) Cat")
        try:
            choice = input(">>> ")
            if choice < 0 or choice > 3:
                raise NameError("Wrong choice")
        except (NameError, SyntaxError, TypeError):
            choice = None

    birth_location = random.choice(locations_list)

    if choice is 1:
        if birth_location is 'America':
            print("OK, so ya birth location iz Murica!")
            sleep(1)
            print("Congrats, tho ))")
            print("You was born in wealth family and there is not much stuff "
                  "to worry about")
            sleep(1)
            print("...for you, as a child/teenager...")
            sleep(3)
            print('\n')
            print("But ya know that awesome school-time, do you ;)")
            sleep(1)
            print("As you get to know - you have fallen in love!!!11")
            sleep(1)
            print("Buuuut, graduation exams are coming...")
            print("So, chose if you really need this relationships:")

            while type(relationships) is not str:
                try:
                    relationships = raw_input("'Y/N' >>> ").upper()
                    if relationships != 'Y' and relationships != 'N':
                        raise NameError("Wrong choice")
                except (NameError, SyntaxError, TypeError):
                    print("\nPlease, try again...")
                    relationships = None

            if relationships == 'Y':
                print("\nAlright, bro)")
                sleep(1)
                print("But how strong is your love? Huh?")
                print("Evaluate it in range from 0 ('don't really luw.') "
                      "to 50 ('FU***NG LOVE MY SPIRITUAL PERSON')")

                while type(love) is not int:
                    try:
                        love = input(">>> ")
                        if love < 0 or love > 50:
                            raise NameError("Wrong number has been entered")
                    except (NameError, SyntaxError, TypeError):
                        print("\nPlease, try again...")
                        love = None

                print("Now, keep in mind, that the possibility of "
                      "successful exam passing has been decreased "
                      "by {love} points ;(".format(love=love))
                sleep(1)
                print("...the original value was '{original}'".format(
                    original=exams_pass_perc))
                exams_pass_perc -= love
                print("'\_(oo)_/'")

            elif relationships == 'N':
                print("\nWell, OK then...")
                sleep(1)
                print("But there are some advantages - your possibility of "
                      "successful exam passing has been increased "
                      "to '{points}' points!".format(points=const_increase))
                exams_pass_perc += const_increase
                print("Because you now have more time to concentrate on "
                      "exams preparation ;)")

            sleep(3)
            print("\nOK, cool!")
            sleep(1)
            print("But exams are around the corner! O_O")
            sleep(1)
            raw_input("Press any key to start the exam...")
            print("Note: you have 3 chances to pass the exams!")
            sleep(1)
            print('\n')
            for i in range(1, 4):
                sleep(3)
                print("Turn #{turn}".format(turn=i))
                exams_result = random.randint(0, 100+exams_pass_perc)
                if exams_result < 100:
                    print("Your result is {result} points...".format(
                        result=exams_result))
                    print("When at least '{p}' is required".format(p=100))
                    if i != 3:
                        print("Try again!")
                        print('\n')
                        continue
                    else:
                        print("You have completely failed the exams((")
                        exams_pass_perc = 0
                        break
                if exams_result >= exams_pass_perc:
                    print("Yey! You are lucky AF!")
                    print("Your result is {result} points!".format(
                        result=exams_result))
                    sleep(1)
                    print("-__-")
                    print("Have you cheated?..")
                    sleep(1)
                    print("Just joking :) lol")
                    exams_pass_perc = 100
                    break

            if exams_pass_perc == 100:
                universities = ['MTI', 'Medical', 'Academy of Art']
            if exams_pass_perc == 0:
                universities = ['Ordinary college', 'Skip university']

            print('\n')
            print("Time goes by so fast... And now its a high time "
                  "to chose what to do after school graduation.")

            print("Make a choice: ")
            for univer in universities:
                index = universities.index(univer) + 1
                print("{i}) {u}".format(i=index, u=univer))
            while type(univer_choice) is not int:
                try:
                    univer_choice = input(">>> ")
                    if univer_choice < 0 or univer_choice > len(universities):
                        raise NameError("Wrong choice")
                except (NameError, SyntaxError, TypeError):
                    print("\nPlease, try again...")
                    univer_choice = None

            finished_university = random.choice([True, False])  # final decision
            if univer_choice == 1:
                if len(universities) == 2:
                    print("You have entered an ordinary college")
                    sleep(1)
                    print("You have finished it with an ordinary diploma")
                    sleep(1)
                    print("Soon, you meat an ordinary partner")
                    sleep(1)
                    print("Got married, of course))")
                    sleep(1)
                    print("And raised an ordinary children")
                    sleep(3)
                    print("As you can see, the life wasnt bad... "
                          "But a little bit boring, right?")
                    sleep(3)
                    print("Now it's your turn to live a life! "
                          "Everything depends on you!")
                    sleep(1)
                    print("Simply do not fuck up.")
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[0]))
                    print('\n')
                    if finished_university is True:
                        sleep(3)
                        print("And you have successfully finished this univer!")
                        sleep(3)
                        print("Then, you have started working as a Python dev!")
                        sleep(3)
                        print("After a few years of hard work and some "
                              "personal investigation, you have done a "
                              "research essay about the fact, that our life "
                              "are not our own...")
                        print("We are just a simple simulation of a "
                              "programmable lifecycle and a holly random "
                              "rules our minds!..")
                        sleep(3)
                        print('\n')
                        raise EnvironmentError("Your character has left the "
                                               "program!..")
                    else:
                        sleep(1)
                        print("Unfortunately, you have not finished the univer")
                        sleep(3)
                        print("Life sucks...")
                        sleep(3)
                        print("The only job you could apply at was illegal "
                              "hacker) somewhere is da hood")
                        sleep(3)
                        print("But every crime is punished!")
                        print("And you appeared in a jail soon...")
                        print("Where committed suicide after 5 years (")
                        sleep(5)
                        print("That's creepy, right?..")
                        print("So, do not make such mistakes as your character "
                              "actually did!!!")
            elif univer_choice == 2:
                if len(universities) == 2:
                    print("That's your choice, btw...")
                    sleep(1)
                    print('\n')
                    print("Bu the way, you decided to travel around the globe!")
                    sleep(3)
                    print("And you have already visited so many countries...")
                    sleep(3)
                    print("But the next stop is Ukraine!")
                    print("Where some guy named Andriy Marusyak gonna host you")
                    print(";-)")
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[1]))
                    print('\n')
                    if finished_university is True:
                        sleep(3)
                        print("And you have successfully finished this univer!")
                        sleep(3)
                        print("Soon you have been relocated to Iran.")
                        print("Where you meet your second half of a solid "
                              "one that calls family!")
                        sleep(3)
                        print("Aww))) That's cute!")
                    else:
                        sleep(3)
                        print("Unfortunately, you have not finished the univer")
                        sleep(3)
                        print("But you moved to Albania and started to trade "
                              "in human's organs...")
                        sleep(3)
                        print("But every crime is punished!")
                        print("And you appeared in a local jail soon...")
                        print("Where committed suicide after 2 years (")
                        sleep(5)
                        print("That's creepy, right?..")
                        print("So, do not make such mistakes as your character "
                              "actually did!!!")
            elif univer_choice == 3:
                print("Congratulations! You have entered '{u}'!".format(
                    u=universities[2]))
                print('\n')
                if finished_university is True:
                    sleep(3)
                    print("And you have successfully finished this university!")
                    sleep(3)
                    print("Also, you got a Nobel prize as the most "
                          "progressive designer!")
                    sleep(3)
                    print("You are famous now ;)")
                    sleep(1)
                    print("Soon, you meet your second half of a solid "
                          "one that calls family!")
                    sleep(5)
                    print("Aww))) That's cute!")
                else:
                    sleep(3)
                    print("Unfortunately, you have not finished the university")
                    sleep(3)
                    print("Further scenario is well known:")
                    print("drugs, alcohol and a cheap cigarettes with coffee (")
                    sleep(3)
                    print("Your, let's say, pocket money are getting from the "
                          "pictures you sell near a local market...")
                    sleep(5)
                    print("That's creepy, right?..")
                    print("So, do not make such mistakes as your character did")
                    print("!!!")

        elif birth_location is 'Europe':
            pass
        else:
            pass
    elif choice is 2:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
