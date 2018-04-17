import random
from time import sleep
from platform import system
import os


def main():
    os_type = system()
    if os_type != 'Windows' and os_type != 'Linux':
        raise EnvironmentError("Unsupported Operating System. Cannot continue.")

    print()
    print("Welcome!")
    sleep(1)
    print("This is a simple lifecycle game :)")
    sleep(3)
    input("Press any key to continue...")

    # General variables:
    choice = None
    locations_list = ['America', 'Europe']
    relationships = None
    love = None
    exams_pass_perc = 85  # start value (may change during the game)
    const_increase = 5
    universities = list()
    univer_choice = None
    gender = None
    dead = None

    while type(choice) is not int:
        if os_type == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print("Chose your character:")
        print("1) Human")
        print("2) Dog")
        print("3) Cat")
        try:
            choice = int(input(">>> "))
            if choice <= 0 or choice > 3:
                raise SyntaxError("Wrong choice")
        except (NameError, SyntaxError, TypeError, ValueError):
            choice = None

    birth_location = random.choice(locations_list)

    if choice is 1:
        print()
        if birth_location is 'America':
            print("OK, so ya birth location iz Murica!")
            sleep(1)
            print("Congrats, tho")
            print("You was born in wealth family and there is not much stuff "
                  "to worry about")
            sleep(1)
            print("...for you, as a child/teenager...")
            sleep(3)
            print()
            print("But ya know that awesome school-time, do you ;)")
            sleep(1)
            print("As you get to know - you have fallen in love!!!11")
            sleep(1)
            print("Buuuut, graduation exams are coming...")
            print("So, chose if you really need this relationships:")

            while type(relationships) is not str:
                try:
                    relationships = input("'Y/N' >>> ").upper()
                    if relationships != 'Y' and relationships != 'N':
                        raise SyntaxError("Wrong choice")
                except (NameError, SyntaxError, TypeError, ValueError):
                    print("\nPlease, try again...")
                    relationships = None

            if relationships == 'Y':
                print()
                print("Alright, bro)")
                sleep(1)
                print("But how strong is your love? Huh?")
                print("Evaluate it in range from 0 ('don't really luw.') "
                      "to 50 ('FU***NG LOVE MY SPIRITUAL PERSON')")

                while type(love) is not int:
                    try:
                        love = int(input(">>> "))
                        if love < 0 or love > 50:
                            raise SyntaxError("Wrong number has been entered")
                    except (NameError, SyntaxError, TypeError, ValueError):
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
            input("Press any key to start the exam...")
            print("Note: you have 3 chances to pass the exams!")
            sleep(1)
            print()
            for n in range(1, 4):
                sleep(3)
                print("Turn #{turn}".format(turn=n))
                exams_result = random.randint(0, 100+exams_pass_perc)
                if exams_result < 100:
                    print("Your result is {result} points...".format(
                        result=exams_result))
                    print("When at least '{p}' is required".format(p=100))
                    if n != 3:
                        print("Try again!")
                        print()
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

            print()
            print("Time goes by so fast... And now its a high time "
                  "to chose what to do after school graduation.")

            print("Make a choice: ")
            for univer in universities:
                index = universities.index(univer) + 1
                print("{i}) {u}".format(i=index, u=univer))
            while type(univer_choice) is not int:
                try:
                    univer_choice = int(input(">>> "))
                    if univer_choice <= 0 or univer_choice > len(universities):
                        raise SyntaxError("Wrong choice")
                except (NameError, SyntaxError, TypeError, ValueError):
                    print("\nPlease, try again...")
                    univer_choice = None
            finished_university = random.choice([True, False])
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
                    dead = True
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[0]))
                    print()
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
                        print()
                        raise EnvironmentError(
                            "Your character has left the program!.."
                        )
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
                        dead = True
            elif univer_choice == 2:
                if len(universities) == 2:
                    print("That's your choice, btw...")
                    sleep(1)
                    print()
                    print("By the way, you decided to travel around the globe!")
                    sleep(3)
                    print("And you have already visited so many countries...")
                    sleep(3)
                    print("But the next stop is Ukraine!")
                    print("Where some guy named Andriy Marusyak gonna host you")
                    print(";-)")
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[1]))
                    print()
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
                        dead = True
            elif univer_choice == 3:
                print("Congratulations! You have entered '{u}'!".format(
                    u=universities[2]))
                print()
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
                    dead = True

        else:
            print("Here we go! Your birth location is Europe!")
            sleep(1)

            print("Now, chose your gender:")
            print("1) Boy")
            print("2) Girl")
            while type(gender) is not int:
                try:
                    gender = int(input(">>> "))
                    if gender <= 0 or gender > 2:
                        raise SyntaxError("Wrong choice")
                except (NameError, SyntaxError, TypeError, ValueError):
                    print("\nPlease, try again...")
                    gender = None

            sleep(1)
            print("Nice! As well as you was born in an intelligent family, "
                  "your lovely parents were trying to give you all the best.")
            sleep(5)
            print("You was studying a in high-paying educational institution;")
            sleep(3)
            print("And was a part of different school groups, like fine art, "
                  "music (piano) and computer science.")
            sleep(5)
            print()
            print("But you know that awesome school-time, do you ;)")
            sleep(1)
            print("As you get to know - you have fallen in love <3")
            sleep(1)
            if gender == 1:
                print("The girl you are in love with is really cute!")
                print("But God-damned graduation exams are coming...")
            if gender == 2:
                print("You like this nice guy, but graduation exams are coming")
            print("So, chose if you really need this relationships:")

            while type(relationships) is not str:
                try:
                    relationships = input("'Y/N' >>> ").upper()
                    if relationships != 'Y' and relationships != 'N':
                        raise SyntaxError("Wrong choice")
                except (NameError, SyntaxError, TypeError, ValueError):
                    print("\nPlease, try again...")
                    relationships = None

            if relationships == 'Y':
                print()
                print("Alright :)")
                sleep(1)
                print("But how strong is your love?")
                print("Evaluate it in range from 0 ('do not really love...') "
                      "to 50 ('i have lost my mind')")

                while type(love) is not int:
                    try:
                        love = int(input(">>> "))
                        if love < 0 or love > 50:
                            raise SyntaxError("Wrong number has been entered")
                    except (NameError, SyntaxError, TypeError, ValueError):
                        print("\nPlease, try again...")
                        love = None

                if gender == 1:
                    print("Now, keep in mind, that the possibility of "
                          "successful exam passing has been decreased "
                          "by {love} points ;(".format(love=love))
                    sleep(1)
                    print("...the original value was '{original}'".format(
                        original=exams_pass_perc))
                    exams_pass_perc -= love
                    print("You have spent to much time on that girl...")
                if gender == 2:
                    exams_pass_perc += const_increase
                    print("Hooray! Your possibility of successful exam passing "
                          "has been increased to '{points}' points!".format(
                              points=const_increase))
                    sleep(3)
                    print("Because your boyfriend helped you with preparation)")

            elif relationships == 'N':
                print("\nWell, that's sad...")
                sleep(1)
                print("But there are some advantages - your possibility of "
                      "successful exam passing has been increased "
                      "to '{points}' points!".format(points=const_increase))
                exams_pass_perc += const_increase
                print("Because you now have more time to concentrate on "
                      "exams preparation ;)")

            sleep(3)
            print("\nAnyway...")
            sleep(1)
            print("Exams are around the corner! O_O")
            sleep(1)
            input("Press any key to start the exam...")
            print("Note: you have 3 chances to pass the exams!")
            sleep(1)
            print()
            for n in range(1, 4):
                sleep(3)
                print("Turn #{turn}".format(turn=n))
                exams_result = random.randint(0, 100 + exams_pass_perc)
                if exams_result < 100:
                    print("Your result is {result} points...".format(
                        result=exams_result))
                    print("When at least '{p}' is required".format(p=100))
                    if n != 3:
                        print("Try again!")
                        print()
                        continue
                    else:
                        print("You have completely failed exams ((")
                        exams_pass_perc = 0
                        break
                if exams_result >= exams_pass_perc:
                    print("Yey! Lucky you! :)")
                    print("The result is {result} points!".format(
                        result=exams_result))
                    sleep(1)
                    print("-__-")
                    print("Have you cheated?..")
                    sleep(1)
                    print("Just joking, never mind ;)")
                    exams_pass_perc = 100
                    break

            if exams_pass_perc == 100:
                universities = ['Oxford', 'Cambridge', 'ETH Zurich']
            if exams_pass_perc == 0:
                universities = ['Ordinary college', 'Skip university']

            print()
            print("Time goes by so fast... And now its a high time "
                  "to chose what to do after school graduation.")

            print("Make a choice: ")
            for univer in universities:
                index = universities.index(univer) + 1
                print("{i}) {u}".format(i=index, u=univer))
            while type(univer_choice) is not int:
                try:
                    univer_choice = int(input(">>> "))
                    if univer_choice <= 0 or univer_choice > len(universities):
                        raise SyntaxError("Wrong choice")
                except (NameError, SyntaxError, TypeError, ValueError):
                    print("\nPlease, try again...")
                    univer_choice = None
            finished_university = random.choice([True, False])
            if univer_choice == 1:
                if len(universities) == 2:
                    print("So, you have entered an ordinary college")
                    sleep(1)
                    print("You have finished it with an ordinary diploma")
                    sleep(1)
                    print("Soon, you meat an ordinary partner")
                    sleep(1)
                    print("Got married, of course))")
                    sleep(1)
                    print("And raised an ordinary children")
                    sleep(3)
                    print("As you can see, the life was not bad... "
                          "But a little bit boring, right?")
                    sleep(3)
                    print("Now it's your turn to live a life! "
                          "Everything depends on you!")
                    sleep(1)
                    print("Simply do not screw this up.")
                    dead = True
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[0]))
                    print()
                    if finished_university is True:
                        sleep(3)
                        print("And you have successfully finished it!")
                        sleep(3)
                        print("After graduation, you went to a local "
                              "graduation school.")
                        sleep(3)
                        print("Soon, you become a candidate of technical "
                              "sciences in the field of machine learning!")
                        sleep(3)
                        print("Every one know you as a successful person :)")
                        sleep(3)
                        second_half = 'wife' if gender == 1 else 'husband'
                        if relationships == 'Y':
                            print("You also meet your future {sh} during "
                                  "business trip".format(sh=second_half))
                            sleep(3)
                            print("Together you have grown beautiful child!")
                        else:
                            print("Everything is going fine!")
                            sleep(3)
                            print("But you still haven't found your {sh} ((".
                                  format(sh=second_half))
                            print("'\_(oo)_/'")
                    else:
                        sleep(1)
                        print("Unfortunately, you have not finished the "
                              "university, due to active student's life ;)")
                        sleep(3)
                        print("Well, sometimes, life is unfair...")
                        sleep(3)
                        print("But you haven't give up!")
                        sleep(3)
                        print("And soon, started out your own programming "
                              "courses! Based on educational knowledge;")
                        print("Also, you have enough time for your hobbies")
                        print("Like music and painting.")
                        print("That's pretty nice ;)")
            elif univer_choice == 2:
                if len(universities) == 2:
                    print("That's your choice, btw...")
                    sleep(1)
                    print()
                    print("By the way, you decided to travel around the globe!")
                    sleep(3)
                    print("And you have already visited so many countries...")
                    sleep(3)
                    print("But the next stop is Ukraine!")
                    print("Where some guy named Andriy Marusyak gonna host you")
                    print(";-)")
                else:
                    print("Congratulations! You have entered '{u}'!".format(
                        u=universities[1]))
                    print()
                    if finished_university is True:
                        sleep(3)
                        print("And you have successfully finished it!")
                        sleep(3)
                        print("After that, you was working as a politician "
                              "in a local City Council...")
                        sleep(3)
                        print("But the more important is that after a few "
                              "years you have been chosen as a president!!!")
                        sleep(3)
                        second_half = 'lady' if gender == 1 else 'gentleman'
                        if relationships == 'Y':
                            print("Also, you finally found a 'first {sh}'!)".
                                  format(sh=second_half))
                            sleep(3)
                            print("Together you have grown beautiful child!")
                            print("They were for you as a sunshine :)")
                        else:
                            print("Everything is going fine!")
                            sleep(3)
                            print("But you still haven't found your "
                                  "'first {sh}' ((".format(sh=second_half))
                            print("But during the time you was a president, "
                                  "you have had enough of '{sh}s' ;)".format(
                                      sh=second_half))
                            print("If you know what i mean!)")
                    else:
                        sleep(1)
                        print("Unfortunately, you have not finished the "
                              "university, due to hard disease ((")
                        sleep(3)
                        print("Well, sometimes, life is unfair...")
                        sleep(3)
                        print("But you haven't give up!")
                        sleep(3)
                        print("And soon, started out your own group of "
                              "support for people with cancer!")
                        print("And helped a lot of people to overcome "
                              "all the hardships...")
                        dead = True
            elif univer_choice == 3:
                print("Congratulations! You have entered '{u}'!".format(
                    u=universities[2]))
                print()
                if finished_university is True:
                    sleep(3)
                    print("And you have successfully finished it!")
                    sleep(3)
                    print("And decided to stay in Germany")
                    sleep(3)
                    second_half = 'wife' if gender == 1 else 'husband'
                    if relationships == 'Y':
                        print("Also, you finally your future {sh}!)".format(
                                  sh=second_half))
                        sleep(3)
                        print("Together you have grown beautiful child!")
                        print("Cuteness overload! :)")
                    else:
                        print("Everything is going fine!")
                        sleep(3)
                        print("But you still haven't found your {sh} ((".
                              format(sh=second_half))
                        print("So you moved to France! :)")
                else:
                    sleep(1)
                    print("Unfortunately, you have not finished the "
                          "university, due to deportation...")
                    sleep(3)
                    print("The reason for that is you was caught by smoking "
                          "weed in your dormitory!")
                    sleep(3)
                    print("Damn... Why have you ruined such a bright future?..")
                    sleep(3)
                    print("Conclusion: don't be like your character! :)")
                    dead = True

        sleep(1)
        print()
        if not dead:
            print("You also spent wonderful old ages!")
            sleep(3)
            print("Congrats on passing this game :)")
            print("Remember - every scenario is unique!")
            sleep(1)
            print("Bye!")
        else:
            print("For now, you game is ended...")
            print("But remember - every scenario is unique!")
            print("You should definitely try it again ;)")
            sleep(1)
            print("Bye!")

    elif choice is 2:
        print()
        print("Hey! You are happy doggo :)")
        sleep(3)
        birth_location = random.choice(['street', 'house'])
        if birth_location == 'street':
            print("But you was born on the street...")
            print("Pure doggo :(")
            is_picked_up = random.choice([True, False])
            sleep(3)
            if is_picked_up:
                print("But don't be so upset")
                sleep(1)
                print("Because you have been picked up from the street!")
                sleep(1)
                print("And from that point, your life become much better)")
                sleep(5)
                print("Even was working is police!")
                sleep(3)
                print("Yes, yes!")
                print("You caught a lot of bad people...")
                sleep(3)
                print("Once, you helped to undercover one person in Zurich, "
                      "that was selling and doing drugs (weed, etc.)...")
                sleep(3)
                print("So, you was a goood boi!))")
                print("Congrats!")
            else:
                print("Soon you have joined a bad squad...")
                sleep(3)
                print("Life was hard, from the beginning(")
                sleep(1)
                print("But you learned how to overcome all the hardships!")
                sleep(1)
                print("You often was hanging out near people houses...")
                print("And they loved you :)")
                sleep(5)
                print("Well, that's all folks...")
                print("Life wasn't fare to you")
                print("But more important is that you remained to be good boi!")
        else:
            print("That was born in a lovely family! :)")
            sleep(3)
            print("The kids from that house loved you!")
            sleep(3)
            print("What else to tell you about your game character?..")
            sleep(1)
            print("You had just a normal dog's life))")
            print("Eat, sleep, bork, repeat")
            sleep(3)
            print("But i have to say that it's not bad, by the way!")
        sleep(3)
        print()
        print("You see, not much stuff is needed to be a nice pet!")
        sleep(3)
        print("I wish it would be applicable to people as well...")
        print("That's why sometimes i rather want to become a dog...")
        sleep(3)
        print("But OK, never mind :)")
        print()
        print("Remember - every scenario is unique!")
        print("And bye, for now! ;)")
    else:
        print()
        print("Hi, kitty! :)")
        sleep(3)
        birth_location = random.choice(['street', 'house'])
        if birth_location == 'street':
            print("But you was born on the street...")
            print("Pure little kitten :(")
            is_picked_up = random.choice([True, False])
            sleep(3)
            if is_picked_up:
                print("But don't be so upset")
                sleep(1)
                print("Because you have been picked up from the street!")
                sleep(1)
                print("And from that point, your life become much better)")
                sleep(5)
                print("Chill out, kitty...")
                print("And say 'meow' ;)")
            else:
                print("Soon you have joined a bad squad...")
                sleep(3)
                print("Life was hard, from the beginning(")
                sleep(1)
                print("But you learned how to overcome all the hardships!")
                sleep(1)
                print("You often was hanging out near people houses...")
                print("And they loved you :)")
                sleep(5)
                print("Well, that's all folks...")
                print("Life wasn't fare to you")
                print("But more important is that you remained to be good cat!")
        else:
            print("That was born in a lovely family! :)")
            sleep(3)
            print("The kids from that house loved you!")
            sleep(3)
            print("What else to tell you about your game character?..")
            sleep(1)
            print("You had just a normal cat's life))")
            print("Eat, sleep, murrr, repeat")
            sleep(3)
            print("But i have to say that it's not bad, by the way!")
        sleep(3)
        print()
        print("You see, not much stuff is needed to be a nice pet!")
        sleep(3)
        print("I wish it would be applicable to people as well...")
        print("That's why sometimes i rather want to become a cat...")
        sleep(3)
        print("But i'm just a peace of ...")
        sleep(1)
        print("code...")
        sleep(3)
        print("OK, never mind ;)")
        print()
        print("Remember - every scenario is unique!")
        print("Bye, for now!")


if __name__ == "__main__":
    main()
