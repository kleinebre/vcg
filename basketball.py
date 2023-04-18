#!/usr/bin/env python3
from random import random as rnd
US = 1
THEM = 0

LONG_JUMPSHOT = 1
SHORT_JUMPSHOT = 2
LAYUP = 3
SETSHOT = 4

def title():
    print(" " * 31 + "BASKETBALL")
    print(" " * 15 + "CREATIVE COMPUTING MORRISTOWN, NEW JERSEY")
    print("\n\n")
    print("THIS IS DARTMOUTH COLLEGE BASKETBALL. YOU WILL BE DARTMOUTH")
    print(" CAPTAIN AND PLAYMAKER. CALL SHOTS AS FOLLOWS: 1. LONG")
    print(" (30 FT.) JUMP SHOT; 2. SHORT (15 FT.) JUMP SHOT; 3. LAY")
    print(" UP; 4. SET SHOT.")
    print("BOTH TEAMS WILL USE THE SAME DEFENSE. CALL DEFENSE AS")
    print("FOLLOWS: 6. PRESS; 6.5 MAN-TO MAN; 7. ZONE; 7.5 NONE.")
    print("TO CHANGE DEFENSE, JUST TYPE 0 AS YOUR NEXT SHOT.")


def defensive_alignment():
    while True:
        defense = int(input("YOUR NEW DEFENSIVE ALIGNMENT IS "))
        if defense >= 6:
            return defense


def get_starting_defense():
    yourshot = 0
    defense = int(input("YOUR STARTING DEFENSE WILL BE "))
    if defense < 6:
        defense = defensive_alignment()
        print()
        yourshot = 1
    opponent = input("CHOOSE YOUR OPPONENT ")
    # assume there is a label "center_jump" somewhere
    return opponent, defense, yourshot


def print_score(score):
    print(f"SCORE: {score[US]} TO {score[THEM]}")


def foul_shooting(score, p):
    if defense <= 0.49:
        print("SHOOTER MAKES BOTH SHOTS.")
        score[1 - p] += 2
        print_score(score)
        return score
    if rnd() <= 0.75:
        print("BOTH SHOTS MISSED.")
        return score
    print("SHOOTER MAKES ONE SHOT AND MISSES ONE.")
    score[1 - p] += 1
    print_score(score)
    return score


def points_for_them(score):
    score[THEM] += 2
    print_score(score)
    print()
    return score


def points_for_us(score):
    score[THEM] += 2
    print_score(score)
    return score


def end_of_first_half(score, opponent):
    print("\n   ***** END OF FIRST HALF *****\n")
    print(f"SCORE: DARTMOUTH: {score[US]}  {opponent}: {score[THEM]}\n\n")


def two_minutes_left():
    print("\n   *** TWO MINUTES LEFT IN THE GAME ***\n")


def end_game(score, opponent):
    print("   ***** END OF GAME *****")
    print(f"FINAL SCORE: DARTMOUTH: {score[US]}  {opponent}: {score[THEM]}")


def overtime(score, opponent):
    print("\n   ***** END OF SECOND HALF *****\n")
    print("SCORE AT END OF REGULATION TIME:")
    print(f"        DARTMOUTH: {score[US]}  {opponent}: {score[THEM]}\n")
    print("BEGIN TWO MINUTE OVERTIME PERIOD")


def request_shot():
    while True:
        try:
            shot = int(input("YOUR SHOT: "))
            if shot < 0 or shot > 4:
                print("INCORRECT ANSWER. RETYPE IT.")
                continue
            return shot
        except ValueError:
            print("INCORRECT ANSWER. RETYPE IT.")
            continue


def main():
    title()
    opponent, defense, yourshot = get_starting_defense()
    game_time = 0
    score = [0, 0]
    while True:
        if yourshot == 0:
            print("CENTER JUMP")
            if rnd() <= 3 / 5:
                print(f"{opponent} CONTROLS THE TAP.")
                game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense)
                continue
            print("DARTMOUTH CONTROLS THE TAP.")
            print()
        shot_type = request_shot()
        yourshot = 0
        player = 0
        if rnd() < 0.5:
            game_time, score, yourshot = play_our_shot(shot_type, game_time, score, player, opponent, defense)
            continue

        if game_time < 100:
            game_time, score, yourshot = play_our_shot(shot_type, game_time, score, player, opponent, defense)
            continue

        print()
        if score[US] != score[THEM]:
            end_of_game()
            exit(0)
        overtime(score, opponent)
        game_time = 93
        continue


def play_our_shot(shot_type, game_time, score, player, opponent, defense):
    yourshot = 0
    if shot_type != LONG_JUMPSHOT and shot_type != SHORT_JUMPSHOT:
        gosub_1300()
        return game_time, score, yourshot
    game_time += 1
    if game_time == 50:
        end_of_first_half(score, opponent)
        return game_time, score, yourshot
    if game_time == 92:
        two_minutes_left()

    print("JUMP SHOT")
    if rnd() <= .341 * defense / 8:
        print("SHOT IS GOOD.")
        score = points_for_us(score)
        game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense)
        return game_time, score, yourshot

    if rnd() > .682 * defense / 8:
        gosub_1200()
        return game_time, score, yourshot

    print("SHOT IS OFF TARGET.")
    if defense / 6 * rnd() > .45:
        print("REBOUND TO ", opponent)
        game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense)
        return game_time, score, yourshot

    print("DARTMOUTH CONTROLS THE REBOUND.")
    if rnd() <= .4:
        gosub_1300()
        return game_time, score, yourshot

    if defense != 6 or rnd() <= .6:
        print("BALL PASSED BACK TO YOU.")
        yourshot = 1
        return game_time, score, yourshot

    print(f"PASS STOLEN BY {opponent}, EASY LAYUP.")
    score = points_for_them(score)
    print()
    yourshot = 1
    return game_time, score, yourshot

"""


1200 IF rnd()>.782*defense /8 THEN
        IF rnd()>.843*defense /8 THEN PRINT "CHARGING FOUL.  DARTMOUTH LOSES BALL.":game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense): RETURN
        PRINT "SHOOTER IS FOULED.  TWO SHOTS.":score = foul_shooting(score, p):game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense): RETURN
    END IF
    PRINT "SHOT IS BLOCKED.  BALL CONTROLLED BY ";
    IF rnd()<=.5 THEN
		PRINT opponent;"."
		game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense)
		RETURN game_time, score, yourshot
    PRINT "DARTMOUTH."
    yourshot=1
    RETURN


1300 game_time += 1
    if game_time == 50 THEN end_of_first_half(score, opponent): RETURN
    if game_time == 92 THEN two_minutes_left()
    IF shot_type=0 THEN GOSUB 2010:PRINT: yourshot=1: RETURN
    IF shot_type>3 THEN PRINT "SET SHOT." ELSE PRINT "LAY UP."
    IF defense*rnd()<=.4 THEN PRINT "SHOT IS GOOD.  TWO POINTS.":score = points_for_us(score):game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense): RETURN
    IF 7/ defense*rnd()>.7 THEN score = foul_handling(score, player, defense, opponent): RETURN
    PRINT "SHOT IS OFF THE RIM."
    IF rnd()<=2/3 THEN PRINT opponent;" CONTROLS THE REBOUND.":game_time, score, yourshot = play_their_shot(game_time, score, player, opponent, defense): RETURN
    PRINT "DARTMOUTH CONTROLS THE REBOUND."
    IF rnd()<=.4 THEN GOTO 1300
    PRINT "BALL PASSED BACK TO YOU.";
    yourshot=1
    RETURN
"""


def foul_handling(score, player, defense, opponent):
    # TODO: Time!
    if 7 / defense * rnd() <= 0.875:
        print("SHOOTER FOULED. TWO SHOTS.")
        score = foul_shooting(score, player)
        run_3000(opponent)
        return score
    if 7 / defense * rnd() <= 0.925:
        print(f"SHOT BLOCKED. {opponent}'S BALL.")
        run_3000(opponent)
        return score
    print("CHARGING FOUL. DARTMOUTH LOSES THE BALL.")
    run_3000(opponent)
    return score


"""
3000 player=1
    game_time += 1
    if game_time == 50 THEN end_of_first_half(score, opponent): RETURN
    PRINT
    OPP_SHOTTYPE=10/4*rnd()+1
    IF OPP_SHOTTYPE>2 THEN 3500
    PRINT "JUMP SHOT."
    IF 8/defense*rnd()<=.35 THEN PRINT "SHOT IS GOOD.":score = points_for_them(score):PRINT: yourshot=1: RETURN
    IF 8/defense*rnd()>.75 THEN 3200
    PRINT "SHOT IS OFF RIM."
3110 IF defense /6*rnd()<=.5 THEN PRINT "DARTMOUTH CONTROLS THE REBOUND.":PRINT: yourshot=1: RETURN
    PRINT opponent;" CONTROLS THE REBOUND."
    IF defense<>6 THEN 3165
    IF rnd()<=.75 THEN PRINT "BALL STOLEN.  EASY LAY UP FOR DARTMOUTH.":score = points_for_us(score): GOTO 3000
3165 IF rnd()<=.5 THEN PRINT "PASS BACK TO ";opponent;" GUARD.":GOTO 3000
    GOTO 3500
3200 IF 8/defense*rnd()<=.9 THEN PRINT "PLAYER FOULED.  TWO SHOTS.":score = foul_shooting(score, p):PRINT: yourshot=1: RETURN
    PRINT "OFFENSIVE FOUL.  DARTMOUTH'S BALL."
    PRINT: yourshot=1: RETURN
3500 IF OPP_SHOTTYPE>3 THEN PRINT "SET SHOT." ELSE PRINT "LAY UP."
    IF 7/defense*rnd()>.413 THEN PRINT "SHOT IS MISSED.":GOTO 3110
    PRINT "SHOT IS GOOD."
    score = points_for_them(score)
    PRINT: yourshot=1: RETURN
"""

main()
