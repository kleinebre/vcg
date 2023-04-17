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
        defense = float(input("YOUR NEW DEFENSIVE ALIGNMENT IS? "))
        if defense >= 6.0:
            return defense


def get_starting_defense():
    yourshot = 0
    defense = int(input("YOUR STARTING DEFENSE WILL BE? "))
    if defense < 6:
        defense = defensive_alignment()
        print()
        yourshot = 1
    opponent = input("CHOOSE YOUR OPPONENT ")
    # assume there is a label "center_jump" somewhere
    return opponent, defense, yourshot


def print_score(score):
    print(f"SCORE: {score[US]} TO {score[THEM]}")


def foul_shooting(score, player, defense):
    if defense <= 0.49:
        print("SHOOTER MAKES BOTH SHOTS.")
        score[1 - player] += 2
        print_score(score)
        return score
    if rnd() <= 0.75:
        print("BOTH SHOTS MISSED.")
        return score
    print("SHOOTER MAKES ONE SHOT AND MISSES ONE.")
    score[1 - player] += 1
    print_score(score)
    return score


def points_for_them(score):
    score[THEM] += 2
    print_score(score)
    return score


def points_for_us(score):
    score[US] += 2
    print_score(score)
    return score


def end_of_first_half(score, opponent):
    print("\n   ***** END OF FIRST HALF *****\n")
    print(f"SCORE: DARTMOUTH: {score[US]}  {opponent}: {score[THEM]}\n\n")


def two_minutes_left():
    print("\n   *** TWO MINUTES LEFT IN THE GAME ***\n")


def end_of_game(score, opponent):
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
    player = 0
    while True:
        if yourshot == 0:
            print("CENTER JUMP")
            if rnd() <= 3 / 5:
                print(f"{opponent} CONTROLS THE TAP.")
                game_time, score, yourshot, defense = play_their_shot(
                    game_time, score, player, opponent, defense
                )
                continue
            print("DARTMOUTH CONTROLS THE TAP.")
            print()
        shot_type = request_shot()
        yourshot = 0
        player = 0
        if rnd() < 0.5:
            game_time, score, yourshot, defense = play_our_shot(
                shot_type, game_time, score, player, opponent, defense
            )
            continue

        if game_time < 100:
            game_time, score, yourshot, defense = play_our_shot(
                shot_type, game_time, score, player, opponent, defense
            )
            continue

        print()
        if score[US] != score[THEM]:
            end_of_game(score, opponent)
            exit(0)
        overtime(score, opponent)
        game_time = 93
        continue


def play_our_shot(shot_type, game_time, score, player, opponent, defense):
    yourshot = 0
    if shot_type != LONG_JUMPSHOT and shot_type != SHORT_JUMPSHOT:
        game_time, score, yourshot, defense = play_our_layup_setshot(
            shot_type, game_time, score, player, opponent, defense
        )
        return game_time, score, yourshot, defense
    game_time += 1
    if game_time == 50:
        end_of_first_half(score, opponent)
        return game_time, score, yourshot, defense
    if game_time == 92:
        two_minutes_left()

    print("JUMP SHOT")
    if rnd() <= 0.341 * defense / 8:
        print("SHOT IS GOOD.")
        score = points_for_us(score)
        game_time, score, yourshot, defense = play_their_shot(
            game_time, score, player, opponent, defense
        )
        return game_time, score, yourshot, defense

    if rnd() > 0.682 * defense / 8:
        if rnd() > .782 * defense / 8:
            if rnd() > .843 * defense / 8:
                print("CHARGING FOUL.  DARTMOUTH LOSES BALL.")
                return play_their_shot(game_time, score, player, opponent, defense)
            print("SHOOTER IS FOULED.  TWO SHOTS.")
            score = foul_shooting(score, player, defense)
            return play_their_shot(game_time, score, player, opponent, defense)

        if rnd() <= .5:
            print(f"SHOT IS BLOCKED.  BALL CONTROLLED BY {opponent}.")
            return play_their_shot(game_time, score, player, opponent, defense)
        print(f"SHOT IS BLOCKED.  BALL CONTROLLED BY DARTMOUTH.")
        yourshot = 1
        return game_time, score, yourshot, defense

    print("SHOT IS OFF TARGET.")
    if defense / 6 * rnd() > 0.45:
        print("REBOUND TO ", opponent)
        game_time, score, yourshot, defense = play_their_shot(
            game_time, score, player, opponent, defense
        )
        return game_time, score, yourshot, defense

    print("DARTMOUTH CONTROLS THE REBOUND.")
    if rnd() <= 0.4:
        game_time, score, yourshot, defense = play_our_layup_setshot(
            shot_type, game_time, score, player, opponent, defense
        )
        return game_time, score, yourshot, defense

    if defense != 6 or rnd() <= 0.6:
        print("BALL PASSED BACK TO YOU.")
        yourshot = 1
        return game_time, score, yourshot, defense

    print(f"PASS STOLEN BY {opponent}, EASY LAYUP.")
    score = points_for_them(score)
    print()
    yourshot = 1
    return game_time, score, yourshot, defense

def play_our_layup_setshot(shot_type, game_time, score, player, opponent, defense):
    yourshot = 0
    while True:
        game_time += 1
        if game_time == 50:
            end_of_first_half(score, opponent)
            return game_time, score, yourshot, defense

        if game_time == 92:
            two_minutes_left()

        if shot_type == 0:
            defense = defensive_alignment()
            print()
            yourshot = 1
            return game_time, score, yourshot, defense

        if shot_type > 3:
            print("SET SHOT.")
        else:
            print("LAY UP.")

        if defense * rnd() <= 0.4:
            print("SHOT IS GOOD.  TWO POINTS.")
            score = points_for_us(score)
            game_time, score, yourshot, defense = play_their_shot(
                game_time, score, player, opponent, defense
            )
            return game_time, score, yourshot, defense

        if 7 / defense * rnd() > 0.7:
            game_time, score, yourshot, defense = foul_handling(game_time, score, player, defense, opponent)
            return game_time, score, yourshot, defense

        print("SHOT IS OFF THE RIM.")

        if rnd() <= 2 / 3:
            print(f"{opponent} CONTROLS THE REBOUND.")
            game_time, score, yourshot, defense = play_their_shot(
                game_time, score, player, opponent, defense
            )
            return game_time, score, yourshot, defense

        print("DARTMOUTH CONTROLS THE REBOUND.")
        if rnd() <= 0.4:
            continue

        print("BALL PASSED BACK TO YOU.")
        yourshot = 1
        return game_time, score, yourshot, defense


def foul_handling(game_time, score, player, defense, opponent):
    # TODO: Time!
    if 7 / defense * rnd() <= 0.875:
        print("SHOOTER FOULED. TWO SHOTS.")
        score = foul_shooting(score, player, defense)
        return play_their_shot(game_time, score, player, opponent, defense)
    if 7 / defense * rnd() <= 0.925:
        print(f"SHOT BLOCKED. {opponent}'S BALL.")
        return play_their_shot(game_time, score, player, opponent, defense)
    print("CHARGING FOUL. DARTMOUTH LOSES THE BALL.")
    return play_their_shot(game_time, score, player, opponent, defense)


def play_their_layup_setshot(opp_shottype, defense, score):
    yourshot = 0
    missed = False
    if opp_shottype > 3:
        print("SET SHOT.")
    else:
        print("LAY UP.")

    if 7 / defense * rnd() > 0.413:
        missed = True
        print("SHOT IS MISSED.")
    else:
        print("SHOT IS GOOD.")
        score = points_for_them(score)
        print()
        yourshot = 1
    return score, yourshot, missed


def play_their_shot(game_time, score, player, opponent, defense):
    yourshot = 0
    while True:
        player = 1
        game_time += 1
        if game_time == 50:
            end_of_first_half(score, opponent)
            return game_time, score, yourshot, defense
        print()
        opp_shottype = 10 / 4 * rnd() + 1

        missed = False
        if opp_shottype > 2:
            score, yourshot, missed = play_their_layup_setshot(opp_shottype, defense, score)
        if not missed:
            print("JUMP SHOT.")
            if 8 / defense * rnd() <= 0.35:
                print("SHOT IS GOOD.")
                score = points_for_them(score)
                print("")
                yourshot = 1
                return game_time, score, yourshot, defense

            if 8 / defense * rnd() > 0.75:
                if 8 / defense * rnd() <= 0.9:
                    print("PLAYER FOULED.  TWO SHOTS.")
                    score = foul_shooting(score, player, defense)
                    print()
                    yourshot = 1
                    return game_time, score, yourshot, defense

                print("OFFENSIVE FOUL.  DARTMOUTH'S BALL.")
                print()
                yourshot = 1
                return game_time, score, yourshot, defense

            print("SHOT IS OFF RIM.")

        if defense / 6 * rnd() <= 0.5:
            print("DARTMOUTH CONTROLS THE REBOUND.")
            print()
            yourshot = 1
            return game_time, score, yourshot, defense

        print(f"{opponent} CONTROLS THE REBOUND.")
        if defense == 6:
            if rnd() <= 0.75:
                print("BALL STOLEN.  EASY LAY UP FOR DARTMOUTH.")
                score = points_for_us(score)
                continue
        if rnd() <= 0.5:
            print(f"PASS BACK TO {opponent} GUARD.")
            continue
        score, yourshot, missed = play_their_layup_setshot(opp_shottype, defense, score)
        return game_time, score, yourshot, defense


main()
