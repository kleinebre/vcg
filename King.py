#!/usr/bin/env python3
import random

print_bytheway = True


def title():
    print(" " * 34, "KING")
    print(" " * 15, "CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n")


def print_instructions(office_term_years):
    print("\n\n")
    print("CONGRATULATIONS! YOU'VE JUST BEEN ELECTED PREMIER OF SETATS")
    print("DETINU, A SMALL COMMUNIST ISLAND 30 BY 70 MILES LONG. YOUR")
    print("JOB IS TO DECIDE UPON THE CONTRY'S BUDGET AND DISTRIBUTE")
    print("MONEY TO YOUR COUNTRYMEN FROM THE COMMUNAL TREASURY.")
    print("THE MONEY SYSTEM IS RALLODS, AND EACH PERSON NEEDS 100")
    print("RALLODS PER YEAR TO SURVIVE. YOUR COUNTRY'S INCOME COMES")
    print("FROM FARM PRODUCE AND TOURISTS VISITING YOUR MAGNIFICENT")
    print("FORESTS, HUNTING, FISHING, ETC. HALF YOUR LAND IS FARM LAND")
    print("WHICH ALSO HAS AN EXCELLENT MINERAL CONTENT AND MAY BE SOLD")
    print("TO FOREIGN INDUSTRY (STRIP MINING) WHO IMPORT AND SUPPORT")
    print("THEIR OWN WORKERS. CROPS COST BETWEEN 10 AND 15 RALLODS PER")
    print("SQUARE MILE TO PLANT.")
    print("YOUR GOAL IS TO COMPLETE YOUR", office_term_years, "YEAR TERM OF OFFICE.")
    print("GOOD LUCK!")
    print("\n")


def ask_instructions(office_term_years):
    z = input("DO YOU WANT INSTRUCTIONS? ")
    if z[0].upper() != "N":
        print_instructions(office_term_years)
    return z


def quit_game():
    print("\n\n")
    exit(0)


def start_year(money, countrymen, workers, land_area):
    land_unitprice = int(10 * random.random() + 95)
    planting_unitprice = int(((random.random() / 2) * 10 + 10))

    print("\nYOU NOW HAVE", money, "RALLODS IN THE TREASURY.")
    print(int(countrymen), "COUNTRYMEN,", end="")
    if workers != 0:
        print(workers, "FOREIGN WORKERS,", end="")
    print("AND", int(land_area), "SQ. MILES OF LAND.")
    print(
        "THIS YEAR INDUSTRY WILL BUY LAND FOR",
        land_unitprice,
        "RALLODS PER SQUARE MILE.",
    )
    print(
        "LAND CURRENTLY COSTS",
        planting_unitprice,
        "RALLODS PER SQUARE MILE TO PLANT.\n",
    )

    return land_unitprice, planting_unitprice


def sell_land(land_area, money, land_unitprice):
    global print_bytheway
    while True:
        try:
            land_to_sell = int(
                input("HOW MANY SQUARE MILES DO YOU WISH TO SELL TO INDUSTRY? ")
            )
        except ValueError:
            print("INVALID VALUE, PLEASE ENTER AN INTEGER")
            continue
        if land_to_sell < 0:
            continue
        if land_to_sell <= land_area - 1000:
            break
        print(
            f"***  THINK AGAIN. YOU ONLY HAVE {land_area - 1000} SQUARE MILES OF FARM LAND."
        )
        if print_bytheway:
            print(
                "\n(FOREIGN INDUSTRY WILL ONLY BUY FARM LAND BECAUSE\nFOREST LAND IS UNECONOMICAL TO STRIP MINE DUE TO TREES,\nTHICKER TOP SOIL, ETC.)\n"
            )
            print_bytheway = False

    land_area -= land_to_sell
    money += land_to_sell * land_unitprice

    return (land_to_sell, land_area, money)


def distribute_money(money):
    money_to_distribute = 0
    if money == 0:
        return (money_to_distribute, money)
    while True:
        try:
            money_to_distribute = int(
                input("HOW MANY RALLODS WILL YOU DISTRIBUTE AMONG YOUR COUNTRYMEN? ")
            )
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue
        if money_to_distribute < 0:
            continue
        if money_to_distribute < money:
            money -= money_to_distribute
            return (money_to_distribute, money)
        if money_to_distribute == money:
            money -= money_to_distribute
            return (money_to_distribute, money)
        print("THINK AGAIN. YOU'VE ONLY", money, "RALLODS IN THE TREASURY")


def plant_crops(money, countrymen, land_area, planting_unitprice):
    if money == 0:
        area_to_plant = 0
        return area_to_plant, money

    while True:
        area_to_plant = int(input("HOW MANY SQUARE MILES DO YOU WISH TO PLANT? "))
        if area_to_plant < 0:
            continue
        if area_to_plant > countrymen * 2:
            print("SORRY, BUT EACH COUNTRYMAN CAN ONLY PLANT 2 SQ. MILES.")
            print(f"There are {countrymen=}")
            continue

        if area_to_plant > land_area - 1000:
            print("SORRY, BUT YOU'VE ONLY", land_area - 1000, "SQ. MILES OF FARM LAND.")
            continue

        total_planting_cost = int(area_to_plant * planting_unitprice)
        if total_planting_cost > money:
            print("THINK AGAIN. YOU'VE ONLY", money, "RALLODS LEFT IN THE TREASURY.")
            continue
        break
    money -= total_planting_cost
    return area_to_plant, money


def pollution_control(money):
    if money == 0:
        eco_funding = 0
        return eco_funding, money
    while True:
        eco_funding = int(
            input("HOW MANY RALLODS DO YOU WISH TO SPEND ON POLLUTION CONTROL? ")
        )
        if eco_funding < 0:
            continue
        if eco_funding <= money:
            return eco_funding, money - eco_funding
        print("   THINK AGAIN. YOU ONLY HAVE", money, "RALLODS REMAINING.")


def interrupt_game():
    print()
    print("GOODBYE.")
    print("(IF YOU WISH TO CONTINUE THIS GAME AT A LATER DATE, ANSWER")
    print("'AGAIN' WHEN ASKED IF YOU WANT INSTRUCTIONS AT THE START")
    print("OF THE GAME).")
    exit(0)


def your_life_is_over():
    if random.random() <= 0.5:
        print("YOU HAVE BEEN THROWN OUT OF OFFICE AND ARE NOW")
        print("RESIDING IN PRISON.")
    else:
        print("YOU HAVE BEEN ASSASSINATED.")
    quit_game()


def too_many_died():
    print()
    print()
    print("OVER ONE THIRD OF THE POPULATION HAS DIED SINCE YOU")
    print("WERE ELECTED TO OFFICE. THE PEOPLE (REMAINING)")
    print("HATE YOUR GUTS.")
    your_life_is_over()


def foreign_worker_revolt():
    print()
    print()
    print("THE NUMBER OF FOREIGN WORKERS HAS EXCEEDED THE NUMBER")
    print("OF COUNTRYMEN. AS A MINORITY, THEY HAVE REVOLTED AND")
    print("TAKEN OVER THE COUNTRY.")
    your_life_is_over()


def absolute_death_count_too_high(deaths):
    print()
    print()
    print(f"{deaths} COUNTRYMEN DIED IN ONE YEAR!!!!!")
    print("DUE TO THIS EXTREME MISMANAGEMENT, YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE, BUT YOU")

    also = random.randint(1, 10)
    if also <= 3:
        print("ALSO HAD YOUR LEFT EYE GOUGED OUT!")
    elif also <= 6:
        print("HAVE ALSO GAINED A VERY BAD REPUTATION.")
    else:
        print("HAVE ALSO BEEN DECLARED NATIONAL FINK.")
    quit_game()


def preventable_deaths():
    print()
    print("MONEY WAS LEFT OVER IN THE TREASURY WHICH YOU DID")
    print("NOT SPEND. AS A RESULT, SOME OF YOUR COUNTRYMEN DIED")
    print("OF STARVATION. THE PUBLIC IS ENRAGED AND YOU HAVE")
    print("BEEN FORCED TO EITHER RESIGN OR COMMIT SUICIDE.")
    print("THE CHOICE IS YOURS.")
    print("IF YOU CHOOSE THE LATTER, PLEASE TURN OFF YOUR COMPUTER")
    print("BEFORE PROCEEDING.")
    quit_game()


def term_ended_successfully(office_term_years):
    print("\n\n")
    print("CONGRATULATIONS!!!!!!!!!!!!!!!!!!")
    print("YOU HAVE SUCCESSFULLY COMPLETED YOUR", office_term_years, "YEAR TERM")
    print("OF OFFICE. YOU WERE, OF COURSE, EXTREMELY LUCKY, BUT")
    print("NEVERTHELESS, IT'S QUITE AN ACHIEVEMENT. GOODBYE AND GOOD")
    print("LUCK - YOU'LL PROBABLY NEED IT IF YOU'RE THE TYPE THAT")
    print("PLAYS THIS GAME.")
    quit_game()


def again(office_term_years):
    while True:
        print("HOW MANY YEARS HAD YOU BEEN IN OFFICE WHEN INTERRUPTED?")
        try:
            years_in_office = int(input())
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue
        if years_in_office < 0:
            quit_game()
        if years_in_office < office_term_years:
            break
        print(f"   COME ON, YOUR TERM IN OFFICE IS ONLY {office_term_years} YEARS.")
        continue

    while True:
        print("HOW MUCH DID YOU HAVE IN THE TREASURY")
        try:
            money = int(input())
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue
        if money < 0:
            quit_game()
        break

    while True:
        print("HOW MANY COUNTRYMEN")
        try:
            countrymen = int(input())
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue
        if countrymen < 0:
            quit_game()
        break

    while True:
        print("HOW MANY WORKERS")
        try:
            workers = int(input())
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue
        if workers < 0:
            quit_game()
        break

    while True:
        print("HOW MANY SQUARE MILES OF LAND? ")
        try:
            land_area = int(input())
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER.")
            continue

        if land_area < 0:
            quit_game()
        if land_area > 2000:
            print("   COME ON, YOU STARTED WITH 1000 SQ. MILES OF FARM LAND")
            print("   AND 10,000 SQ. MILES OF FOREST LAND.")
            continue
        if land_area > 1000:
            break

    return (money, countrymen, land_area, years_in_office)


def calculate_worker_immigrants(land_to_sell, workers):
    if land_to_sell == 0:
        return 0
    worker_immigrants = int(
        land_to_sell + (random.random() * 10) - (random.random() * 20)
    )
    if workers == 0:
        worker_immigrants += 20

    return worker_immigrants


def calculate_countrymen_migration(
    money_to_distribute, countrymen, eco_funding, land_area, eco_deaths
):
    migration = int(
        ((money_to_distribute / 100 - countrymen) / 10)
        + (eco_funding / 25)
        - ((2000 - land_area) / 50)
        - (eco_deaths / 2)
    )

    return migration


def migration_effect(
    land_to_sell,
    workers,
    money_to_distribute,
    countrymen,
    eco_funding,
    land_area,
    eco_deaths,
):
    worker_immigrants = calculate_worker_immigrants(land_to_sell, workers)
    if worker_immigrants != 0:
        print(worker_immigrants, "WORKERS CAME TO THE COUNTRY AND")
    workers += worker_immigrants

    countrymen_migration = calculate_countrymen_migration(
        money_to_distribute, countrymen, eco_funding, land_area, eco_deaths
    )
    countrymen += countrymen_migration
    print(abs(countrymen_migration), "COUNTRYMEN ", end="")
    if countrymen_migration < 0:
        print("LEFT ", end="")
    else:
        print("CAME TO ", end="")
    print("THE ISLAND.")

    return countrymen_migration, countrymen, workers


def excess_deaths(
    money_to_distribute, countrymen, eco_funding, land_area, land_unitprice, money
):
    fed_people = money_to_distribute / 100.0
    starvation = countrymen - fed_people
    if starvation < 0:
        starvation = 0
    if fed_people < countrymen:
        if starvation > (countrymen / 2.0):
            too_many_died()
        print(int(starvation), "COUNTRYMEN DIED OF STARVATION")

    eco_deaths = int(random.random() * (2000 - land_area))
    if eco_funding > 25:
        eco_deaths = int(eco_deaths / (eco_funding / 25))
    if eco_deaths < 0:
        eco_deaths = 0
    if eco_deaths > 0:
        print(eco_deaths, "COUNTRYMEN DIED OF CARBON-MONOXIDE AND DUST INHALATION")
    deaths = eco_deaths + starvation
    if deaths > 0:
        death_cost = int(deaths * 9)
        print("   YOU WERE FORCED TO SPEND", death_cost, "RALLODS ON FUNERAL EXPENSES")
        money -= death_cost
    if money < 0:
        print("   INSUFFICIENT RESERVES TO COVER COST - LAND WAS SOLD")
        # land_area decreases because money is negative.
        land_area = int(land_area + (money / land_unitprice))
        money = 0
    countrymen = int(countrymen - deaths)

    # return all the local variables that were changed
    return (eco_deaths, deaths, land_area, countrymen, money)


def food_production(land_area, area_to_plant, workers, land_unitprice, money):
    if workers == 0:
        # no farming income.
        return money

    failed_crops_area = int(((2000 - land_area) * ((random.random() + 1.5) / 2.0)))
    print("OF", int(area_to_plant), "SQ. MILES PLANTED,")
    if area_to_plant < failed_crops_area:
        failed_crops_area = area_to_plant
    successful_crops = area_to_plant - failed_crops_area
    print(" YOU HARVESTED", int(successful_crops), "SQ. MILES OF CROPS.")
    harvest_income = int(successful_crops * (land_unitprice / 2.0))
    print("MAKING", int(harvest_income), "RALLODS.")
    money = int(money + harvest_income)

    return money


def tourism(previous_tourism, money, countrymen, migration, land_area):
    tourist_income = int(((countrymen - migration) * 22) + (random.random() * 500))
    tourist_cost = int((2000 - land_area) * 15)
    tourist_profit = int(tourist_income - tourist_cost)
    if tourist_profit < 0:
        tourist_profit = 0
    print(" YOU MADE", tourist_profit, "RALLODS FROM TOURIST TRADE.")
    if tourist_profit < previous_tourism:
        decrease_reason = 10 * random.random()
        if decrease_reason <= 2:
            print("FISH POPULATION HAS DWINDLED DUE TO WATER POLLUTION.")
        elif decrease_reason <= 4:
            print("AIR POLLUTION IS KILLING GAME BIRD POPULATION.")
        elif decrease_reason <= 6:
            print("MINERAL BATHS ARE BEING RUINED BY WATER POLLUTION.")
        elif decrease_reason <= 8:
            print("UNPLEASANT SMOG IS DISCOURAGING SUN BATHERS.")
        else:
            print("HOTELS ARE LOOKING SHABBY DUE TO SMOG GRIT.")
    money += tourist_profit
    previous_tourism = tourist_profit
    return previous_tourism, money


def main():
    title()
    office_term_years = 8
    workers = 0
    previous_tourism = 0
    if ask_instructions(office_term_years).lower() == "again":
        (money, countrymen, land_area, years_in_office) = again(office_term_years)
    else:
        money = int(60000 + (1000 * random.random()) - (1000 * random.random()))
        countrymen = int(500 + (10 * random.random()) - (10 * random.random()))
        land_area = 2000
        years_in_office = 0

    while True:
        # Show status and set params for this year
        land_unitprice, planting_unitprice = start_year(
            money, countrymen, workers, land_area
        )
        deaths = 0  # nobody died yet this year.

        # Ask for governing input
        (land_to_sell, land_area, money) = sell_land(land_area, money, land_unitprice)
        (money_to_distribute, money) = distribute_money(money)
        (area_to_plant, money) = plant_crops(
            money, countrymen, land_area, planting_unitprice
        )
        (eco_funding, money) = pollution_control(money)
        money_headroom = money

        if (
            land_area == 0
            and money_to_distribute == 0
            and area_to_plant == 0
            and eco_funding == 0
        ):
            interrupt_game()

        print()
        print()
        # Now let's see how things develop...
        (eco_deaths, deaths, land_area, countrymen, money) = excess_deaths(
            money_to_distribute,
            countrymen,
            eco_funding,
            land_area,
            land_unitprice,
            money,
        )

        migration, countrymen, workers = migration_effect(
            land_to_sell,
            workers,
            money_to_distribute,
            countrymen,
            eco_funding,
            land_area,
            eco_deaths,
        )

        # calculate money after food production income
        money = food_production(
            land_area, area_to_plant, workers, land_unitprice, money
        )
        previous_tourism, money = tourism(
            previous_tourism, money, countrymen, migration, land_area
        )

        # check if we're ousted prematurely
        if deaths > 200:
            absolute_death_count_too_high(deaths)
        if countrymen < 343:
            too_many_died()

        if money_headroom / 100 > 5:
            if deaths - eco_deaths >= 2:
                # people starved unnecessarily
                preventable_deaths()

        if workers > countrymen:
            foreign_worker_revolt()

        years_in_office = years_in_office + 1
        if years_in_office == office_term_years:
            term_ended_successfully(office_term_years)
        continue


main()
