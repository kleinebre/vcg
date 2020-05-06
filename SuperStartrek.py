#!/usr/bin/env python
from __future__ import print_function
from random import random as rnd
import random
import math

# return codes for commands
GAME_OVER = 10001
GAME_RESTART = 10002


def optupper(message):
    return message.upper()


def uprint(message):
    print(optupper(message))
    return


def num_input(message, default=0):
    while True:
        val = default
        try:
            raw = ""
            raw = input(optupper(message) + "? ")
        except:
            pass
        try:
            val = float(raw)
        except:
            pass
        break
    return val


def xy_input(message, default=0):
    while True:
        val = default
        try:
            raw = ""
            raw = input(optupper(message) + "? ")
        except:
            pass

        try:
            xy = raw.split(",")
            x = int(xy[0])
            y = int(xy[1])
            return (x, y)
        except:
            pass
        continue

    return val


def distance(from_x, from_y, to_x, to_y):
    return math.sqrt(((to_x - from_x) ** 2) + ((to_y - from_y) ** 2))


def calc_dir_and_dist(from_y, from_x, to_y, to_x):
    # silly original code swaps x and y
    from math import atan2, pi, sqrt

    xdist = to_x - from_x
    ydist = -(to_y - from_y)  # and reverses Y direction on axis.
    course = 1 + (4 * atan2(ydist, xdist) / pi)
    if course < 1:
        course += 8
    dist = distance(from_x, from_y, to_x, to_y)
    uprint("Direction = %s" % course)
    uprint("Distance = %s" % dist)
    return


def iround(x):
    return int(round(x))


def title():
    """
    ***        **** STAR TREK ****        ****
    *** SIMULATION OF A MISSION OF THE STARSHIP ENTERPRISE,
    *** AS SEEN ON THE STAR TREK TV SHOW.
    *** ORIGIONAL PROGRAM BY MIKE MAYFIELD, MODIFIED VERSION
    *** PUBLISHED IN DEC'S "101 BASIC GAMES", BY DAVE AHL.
    *** MODIFICATIONS TO THE LATTER (PLUS DEBUGGING) BY BOB
    *** LEEDOM - APRIL & DECEMBER 1974,
    *** WITH A LITTLE HELP FROM HIS FRIENDS . . .
    *** COMMENTS, EPITHETS, AND SUGGESTIONS SOLICITED --
    *** SEND TO:  R. C. LEEDOM
    ***           WESTINGHOUSE DEFENSE & ELECTRONICS SYSTEMS CNTR.
    ***           BOX 746, M.S. 338
    ***           BALTIMORE, MD  21203
    ***
    *** CONVERTED TO MICROSOFT 8 K BASIC 3/16/78 BY JOHN GORDERS
    *** LINE NUMBERS FROM VERSION STREKLINGON_WARSHIPS_INITIAL OF 1/12/75 PRESERVED AS
    *** MUCH AS POSSIBLE WHILE USING MULTIPLE STATEMENTS PER LINE
    *** SOME LINES ARE LONGER THAN 72 CHARACTERS; THIS WAS DONE
    *** BY USING "?" INSTEAD OF "PRINT" WHEN ENTERING LINES
    ***
    """
    for i in range(0, 12):
        uprint("")
    uprint("                                    ,------*------,")
    uprint("                    ,-------------   '---  ------'")
    uprint("                     '-------- --'      / /")
    uprint("                         ,---' '-------/ /--,")
    uprint("                          '----------------'")
    uprint("")
    uprint("                    THE USS ENTERPRISE --- NCC-1701")
    for i in range(0, 5):
        uprint("")


last_seed = 0


def randompos(r=1):
    global last_seed
    if last_seed != r:
        # Commented out - let's not make the game the same every time
        # random.seed(r)
        last_seed = r
    return int(rnd() * 7.98 + 1.01)


class Quadrant:
    def __init__(self, quadrant_x, quadrant_y):
        self.content = " " * 8 * 8 * 3
        self.quadrant_x = quadrant_x
        self.quadrant_y = quadrant_y

    def name(self, region_only=0):
        # quadrant_x and quadrant_y are 1-based
        quadrant_x = (self.quadrant_x - 1) % 8  # ensure always within bounds
        quadrant_y = (self.quadrant_y - 1) % 8  # ensure always within bounds

        names1 = [
            "Antares",
            "Rigel",
            "Procyon",
            "Vega",
            "Canopus",
            "Altair",
            "Sagittarius",
            "Pollux",
        ]
        names2 = [
            "Sirius",
            "Deneb",
            "Capella",
            "Betelgeuse",
            "Aldebaran",
            "Regulus",
            "Arcturus",
            "Spica",
        ]
        regions = ["I", "II", "III", "IV", "I", "II", "III", "IV"]

        if quadrant_y < 4:
            name = names1[quadrant_x]
        else:
            name = names2[quadrant_x]
        if region_only:
            return name
        name += " " + regions[quadrant_y]
        return name

    def set_content(self, sector_x, sector_y, new_content):
        """ 
        INSERT IN STRING ARRAY FOR QUADRANT
        """
        if len(new_content) != 3:
            raise RuntimeError("Quadrant content should be size 3")

        qpos = (int(sector_x - 0.5) * 3) + (int(sector_y - 0.5) * 24)
        self.content = self.content[:qpos] + new_content + self.content[qpos + 3 :]
        return self.content

    def get_content(self, sector_x, sector_y):
        qpos = (int(sector_x - 0.5) * 3) + (int(sector_y - 0.5) * 24)
        return self.content[qpos : qpos + 3]

    def is_content(self, sector_x, sector_y, expected_content):
        """
        STRING COMPARISON IN QUADRANT ARRAY
        """
        qpos = (int(sector_x - 0.5) * 3) + (int(sector_y - 0.5) * 24)
        return int(self.content[qpos : qpos + 3] == expected_content)

    def find_empty_sector(self):
        """
        FIND EMPTY PLACE IN QUADRANT (FOR THINGS)
        """
        while True:
            sector_x = randompos()
            sector_y = randompos()
            if self.is_content(sector_x, sector_y, "   "):
                break
        return sector_x, sector_y


class Klingon:
    strength = 200

    def __init__(self, x, y, hitpoints):
        self.x = 0
        self.y = 0
        self.hitpoints = 0


class Starship:
    course_x = [0, 0, -1, -1, -1, 0, 1, 1, 1, 0]
    course_y = [0, 1, 1, 0, -1, -1, -1, 0, 1, 1]

    def __init__(self, mission):
        self.docked = False
        self.energy = 3000
        self.torpedos = 10
        self.energy_initial = self.energy
        self.torpedos_initial = self.torpedos
        self.shields = 0
        self.damage = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # INITIALIZE ENTERPRIZE'S POSITION
        self.quadrant_x = randompos()
        self.quadrant_y = randompos()
        self.sector_x = randompos()
        self.sector_y = randompos()
        self.mission = mission

    def fly_to(self, quadrant_x, quadrant_y, sector_x, sector_y):
        """
        In the original code, quadrant indices were used both before 
        validating them, and after being validated as invalid.
        So I have dropped the boundary validation altogether, since 
        in practice, it apparently served no actual purpose.    
        """
        klingons = 0
        starbases = 0
        stars = 0

        self.new_damage = 0.5 * rnd()
        galaxy = self.mission.galaxy

        quadrant = galaxy.enter_quadrant(quadrant_x, quadrant_y)
        quadrant_name = quadrant.name()
        self.quadrant = quadrant

        uprint("")
        if mission.curr_stardate == mission.stardate_initial:
            uprint("Your mission begins with your starship located ")
            uprint("in the galactic quadrant, '%s'." % quadrant_name)
        else:
            uprint("Now entering %s quadrant . . ." % quadrant_name)
        uprint("")
        if quadrant.klingons > 0:
            uprint("Combat area      Condition RED")
            if self.shields <= 200:
                uprint("   Shields dangerously low")

    def srs_and_startup(self):
        """
        SHORT RANGE SENSOR SCAN & STARTUP SUBROUTINE
        """
        self.docked = False
        for i in range(-1, 2):
            x = round(self.sector_x + i)
            if x < 1 or x > 8:
                continue
            for j in range(-1, 2):
                y = round(self.sector_y + j)
                if y < 1 or y > 8:
                    continue
                if self.quadrant.is_content(x, y, ">!<"):
                    self.docked = True
                    break
                continue

        if self.docked:
            self.energy = self.energy_initial
            self.torpedos = self.torpedos_initial
            self.shields = 0
            uprint("Shields dropped for docking purposes")
            if self.damage[2] < 0:
                uprint("")
                uprint("*** Short range sensors are out ***")
                uprint("")
                return
        self.mission.print_status()
        return

    def print_commands(self, help=False):
        uprint("Enter one of the following:")
        if help:
            uprint("  RUL  (RULES)")

        uprint("  NAV  (TO SET COURSE)")
        uprint("  SRS  (FOR SHORT RANGE SENSOR SCAN)")
        uprint("  LRS  (FOR LONG RANGE SENSOR SCAN)")
        uprint("  PHA  (TO FIRE PHASERS)")
        uprint("  TOR  (TO FIRE PHOTON TORPEDOES)")
        uprint("  SHE  (TO RAISE OR LOWER SHIELDS)")
        uprint("  DAM  (FOR DAMAGE CONTROL REPORTS)")
        uprint("  COM  (TO CALL ON LIBRARY-COMPUTER)")
        uprint("  XXX  (TO RESIGN YOUR COMMAND)")

        if not help:
            uprint("  ?    (HELP)")

        uprint("")
        return

    def ask_command(self, help=False):
        if help:
            # help file
            commands = [
                "RUL",
                "NAV",
                "SRS",
                "LRS",
                "PHA",
                "TOR",
                "SHE",
                "DAM",
                "COM",
                "XXX",
            ]
        else:
            commands = [
                "NAV",
                "SRS",
                "LRS",
                "PHA",
                "TOR",
                "SHE",
                "DAM",
                "COM",
                "XXX",
                "?",
            ]

        while True:
            if help:
                answer = input(optupper("Help on which command? "))
            else:
                answer = input(optupper("Command? "))
            try:
                index = commands.index(answer.upper())
            except:
                self.print_commands(help=help)
                continue
            break
        return index

    def input_course(
        self,
        message="Course (1-9)? ",
        error="   Lt. Sulu reports, 'Incorrect course data, sir!'",
    ):
        while True:
            raw_course = input(optupper(message))
            try:
                float_course = float(raw_course)
            except:
                return 0

            if float_course >= 1:
                if float_course < 9:
                    return float_course
                if float_course == 9:
                    float_course = 1
                    return float_course
            uprint(error)
            return 0

    def input_warp(self):
        max_warp = 8
        if self.damage[1] < 0:
            max_warp = 0.2
        while True:
            try:
                raw_warp = input(optupper("Warp factor (0-%s)? " % str(max_warp)))
            except:
                continue

            float_warp = float(raw_warp)
            if float_warp > 0:
                if float_warp > max_warp:
                    if self.damage[1] < 0:
                        uprint(
                            "Warp engines are damaged.  Maximum speed = warp %s"
                            % max_warp
                        )
                    else:
                        uprint(
                            "    Chief engineer Scott reports 'The engines won't take"
                        )
                        uprint(" warp %s!" % str(float_warp))
                    return
            return float_warp

    def enterprise_destroyed(self):
        uprint("")
        uprint("The Enterprise has been detroyed.  The Federation will be conquered.")
        return self.game_over()

    def klingons_shooting(self):
        klingons = self.quadrant.klingons
        if klingons <= 0:
            return

        if self.docked:
            uprint("Starbase shields protect the Enterprise")
            return

        for i in range(0, Galaxy.MAX_KLINGONS):
            klingon = self.mission.galaxy.klingon[i]
            if klingon.hitpoints == 0:
                continue

            mult = 2 + rnd()
            hit = mult * int(
                klingon.hitpoints
                / distance(self.sector_x, self.sector_y, klingon.x, klingon.y)
            )
            self.shields -= klingon.hitpoints
            klingon.hitpoints = klingon.hitpoints / (3 + rnd())

            uprint(
                "%s unit hit on Enterprise from sector %s,%s"
                % (hit, klingon.x, klingon.y)
            )

            if self.shields <= 0:
                return self.enterprise_destroyed()

            uprint("      <Shields down to %s units>" % self.shields)
            if hit < 20:
                continue

            if rnd() > 0.6:
                continue

            if hit / self.shields < 0.02:
                continue

            devnum = randompos()
            self.damage[devnum] -= hit / self.shields - 0.5 * rnd()
            devname = get_device_name(devnum)
            uprint("Damage control reports '%s damaged by the hit'" % devname)

        return

    def klingons_fire_moving_starship(self, warp):
        """
        KLINGONS MOVE/FIRE ON MOVING STARSHIP . . .
        """
        galaxy = self.mission.galaxy

        for i in range(0, Galaxy.MAX_KLINGONS):
            klingon = galaxy.klingon[i]
            if klingon.hitpoints == 0:
                continue
            # Klingon with this index exists. Move it randomly
            self.quadrant.set_content(klingon.x, klingon.y, "   ")
            x, y = self.quadrant.find_empty_sector()
            klingon.x = x
            klingon.y = y
            self.quadrant.set_content(klingon.x, klingon.y, "+K+")

        self.klingons_shooting()

        damageflag = 0
        warpdamage = warp
        if warp >= 1:
            warpdamage = 1

        for i in range(0, 8):
            j = i + 1
            if self.damage[j] >= 0:
                continue
            self.damage[j] += warpdamage
            if self.damage[j] > -0.1 and self.damage[j] < 0:
                self.damage[j] = -0.1
                continue
            if self.damage[j] < 0:
                continue
            if damageflag != 1:
                damageflag = 1
                uprint(
                    "Damage control report:  %s repair completed." % get_device_name(j)
                )

        if rnd() > 0.2:
            return

        device = randompos()
        if rnd() < 0.6:
            self.damage[device] -= rnd() * 5 + 1
            uprint("Damage control report:  %s damaged" % get_device_name(device))

        else:
            self.damage[device] -= rnd() * 3 + 1
            uprint(
                "Damage control report:  %s state of repair improved"
                % get_device_name(device)
            )

        uprint("")
        return

    def navigation(self):
        course = self.input_course()
        if course == 0:
            return

        warp = self.input_warp()
        if not warp:
            return

        energy_needed = int(warp * 8 + 0.5)
        if self.energy < energy_needed:
            uprint("Engineering reports   'Insufficient energy available")
            uprint("                       for maneuvering at warp %s!" % warp)
            if self.shields < energy_needed - self.energy or self.damage[7] < 0:
                return
            uprint("Deflector control room acknowledges %s units of energy")
            uprint("                         presently deployed to shields.")
            return
        self.klingons_fire_moving_starship(warp)
        return self.move_starship(course, warp, energy_needed)

    def short_range_scan(self):
        self.srs_and_startup()
        if self.shields + self.energy > 10:
            if self.energy > 10 or self.damage[7] == 0:
                return

        uprint("")
        uprint("** FATAL ERROR **   You've just stranded your ship in space")
        uprint("You have insufficient maneuvering energy, and shield control")
        uprint("is presently incapable of cross-circuiting to engine room!!")
        return self.game_over()

    def long_range_scan(self):
        if self.damage[3] < 0:
            uprint("Long range sensors are inoperable")
            return
        uprint(
            "Long range scan for quadrant %s,%s" % (self.quadrant_x, self.quadrant_y)
        )
        uprint("-" * 19)
        n = [0, 0, 0, 0]
        for i in range(self.quadrant_x - 1, self.quadrant_x + 2):
            n[1] = -1
            n[2] = -2
            n[3] = -3
            for j in range(self.quadrant_y - 1, self.quadrant_y + 2):
                if i >= 1 and i <= 8 and j >= 1 and j <= 8:
                    n[j - self.quadrant_y + 2] = self.mission.galaxy.galaxy[i][j]
                    self.mission.galaxy.seen[i][j] = self.mission.galaxy.galaxy[i][j]
            line = ": "
            for l in range(1, 4):
                toprint = ""
                if n[l] < 0:
                    toprint = "***"
                else:
                    toprint = ("000" + str((n[l] + 1000) % 1000))[-3:]
                line += "%s : " % toprint
            uprint(line)
            print("-" * 19)
        return

    def phaser(self):
        if self.damage[4] < 0:
            uprint("Phasers inoperative")
            return

        if not (self.quadrant.klingons > 0):
            uprint("Science officer Spock reports  'Sensors show no enemy ships")
            uprint("                                in this quadrant'")
            return
        if self.damage[8] < 0:
            uprint("Computer failure hampers accuracy")
        uprint("Phasers locked on target;  energy available = %s units" % self.energy)
        while True:
            units = num_input("Number of units to fire")
            if units <= 0:
                return
            if self.energy - units < 0:
                continue
            break

        self.energy -= units
        if self.damage[7] < 0:
            units = units * rnd()
        hitperklingon = int(units / self.quadrant.klingons)
        for i in range(0, Galaxy.MAX_KLINGONS):
            if self.mission.galaxy.klingon[i].hitpoints <= 0:
                continue
            hit = int(
                (
                    hitperklingon
                    / distance(
                        self.sector_x,
                        self.sector_y,
                        self.mission.galaxy.klingon[i].x,
                        self.mission.galaxy.klingon[i].y,
                    )
                )
                * (rnd() + 2)
            )
            if hit <= 0.15 * self.mission.galaxy.klingon[i].hitpoints:
                uprint(
                    "Sensors show no damage to enemy at %s,%s"
                    % (
                        self.mission.galaxy.klingon[i].x,
                        self.mission.galaxy.klingon[i].y,
                    )
                )
                continue
            self.mission.galaxy.klingon[i].hitpoints -= hit
            uprint(
                "%s unit hit on klingon at sector %s,%s"
                % (
                    hit,
                    self.mission.galaxy.klingon[i].x,
                    self.mission.galaxy.klingon[i].y,
                )
            )
            if self.mission.galaxy.klingon[i].hitpoints <= 0:
                self.mission.galaxy.klingon[i].hitpoints = 0
                uprint("*** Klingon destroyed ***")
                self.quadrant.klingons -= 1
                self.mission.galaxy.klingons_total -= 1
                self.quadrant.set_content(
                    self.mission.galaxy.klingon[i].x,
                    self.mission.galaxy.klingon[i].y,
                    "   ",
                )
                self.mission.galaxy.galaxy[self.quadrant_x][self.quadrant_y] -= 100
                self.mission.galaxy.seen[self.quadrant_x][
                    self.quadrant_y
                ] = self.mission.galaxy.galaxy[self.quadrant_x][self.quadrant_y]

                if self.mission.galaxy.klingons_total <= 0:
                    klingons_destroyed()
                    return GAME_OVER

            else:
                uprint(
                    "(Sensors show %s units remaining)"
                    % self.mission.galaxy.klingon[i].hitpoints
                )
                continue

        return self.klingons_shooting()

    def torpedo(self):
        if self.torpedos <= 0:
            uprint("All photon torpedoes expended")
            return
        if self.damage[5] < 0:
            uprint("Photon tubes are not operational")
            return
        course = self.input_course(
            message="Photon torpedo course (1-9)? ",
            error="Ensign checkov reports, 'Incorrect course data, sir!'",
        )
        if course == 0:
            return

        tcourse_x = self.course_x[int(course)] + (
            self.course_x[int(course) + 1] - self.course_x[int(course)]
        ) * (course - int(course))
        tcourse_y = self.course_y[int(course)] + (
            self.course_y[int(course) + 1] - self.course_y[int(course)]
        ) * (course - int(course))

        self.energy -= 2
        self.torpedos -= 1

        x = self.sector_x
        y = self.sector_y

        uprint("Torpedo track:")
        while True:
            x += tcourse_x
            y += tcourse_y
            xend = int(x + 0.5)
            yend = int(y + 0.5)

            if xend < 1 or xend > 8 or yend < 1 or yend > 8:
                uprint("Torpedo missed")
                return self.klingons_shooting()

            uprint(" " * 15 + "%s,%s" % (xend, yend))
            if self.quadrant.is_content(xend, yend, "   "):
                continue

            break

        if self.quadrant.is_content(xend, yend, "+K+"):
            uprint("*** Klingon destroyed ***")
            self.quadrant.klingons -= 1
            self.mission.galaxy.klingons_total -= 1
            if self.mission.galaxy.klingons_total <= 0:
                klingons_destroyed()
                return GAME_OVER
            for i in range(0, Galaxy.MAX_KLINGONS):
                if (
                    self.mission.galaxy.klingon[i].x == xend
                    and self.mission.galaxy.klingon[i].y == yend
                ):
                    self.mission.galaxy.klingon[i].hitpoints = 0
                    self.quadrant.set_content(
                        self.mission.galaxy.klingon[i].x,
                        self.mission.galaxy.klingon[i].y,
                        "   ",
                    )
                    self.mission.galaxy.galaxy[self.quadrant_x][self.quadrant_y] -= 100
                    self.mission.galaxy.seen[self.quadrant_x][
                        self.quadrant_y
                    ] = self.mission.galaxy.galaxy[self.quadrant_x][self.quadrant_y]
                    return self.klingons_shooting()

        if self.quadrant.is_content(xend, yend, " * "):
            uprint("Star at %s,%s absorbed torpedo energy." % (xend, yend))
            return self.klingons_shooting()

        if self.quadrant.is_content(xend, yend, ">!<"):
            uprint("*** Starbase destroyed ***")
            self.mission.galaxy.starbases_total -= 1
            self.mission.galaxy.galaxy[self.quadrant_x][self.quadrant_y] -= 10
            self.mission.galaxy.starbases = self.mission.galaxy.starbases - 1
            self.quadrant.set_content(xend, yend, "   ")
            self.docked = False

            if (
                self.mission.galaxy.starbases_total > 0
                or self.mission.galaxy.klingons_total
                > self.mission.curr_startdate
                - self.mission.stardate_initial
                - self.mission.days
            ):
                uprint(
                    "Starfleet command reviewing your record to consider court marshall!"
                )
            else:
                uprint("That does it, captain!!  You are hereby relieved of command")
                uprint("and sentenced to 99 stardates at hard labor on Cygnus 12!!")
                return GAME_OVER

        return self.klingons_shooting()

    def shield(self):
        if self.damage[7] < 0:
            uprint("Shield control inoperable")
            return

        uprint("Energy available = %s" % (self.energy + self.shields))

        try:
            x = input(optupper("Number of units to shields? "))
            x = float(x)
        except:
            x = 0
            raise

        if x < 0 or self.shields == x:
            uprint("<Shields unchanged>")
            return

        if x > self.energy + self.shields:
            uprint("Shield control reports  'This is not the federation treasury.'")
            uprint("<Shields unchanged>")
            return

        self.energy = self.energy + self.shields - x
        self.shields = x
        uprint("Deflector control room report:")
        uprint("  'Shields now at %s units per your command.'" % self.shields)
        return

    def maneuver_energy_shields(self, n):
        self.energy -= n
        self.energy -= 10
        if self.energy >= 0:
            return

        uprint("Shield control supplies energy to complete the maneuver.")

        self.shields += self.energy  # Energy is negative.
        self.energy = 0
        if self.shields <= 0:
            self.shields = 0
        return

    def print_state_of_repair(self):
        uprint("")
        uprint("Device             State of repair")
        for i in range(1, 9):
            devname = get_device_name(i)
            devname += " " * (25 - len(devname))
            uprint("%s%s" % (devname, int(self.damage[i] * 100) * 0.01))
        uprint("")

    def damage_control(self):
        if self.damage[6] < 0:
            uprint("Damage control report not available")
        else:
            self.print_state_of_repair()

        if not self.docked:
            return

        time_to_fix = 0
        for i in range(1, 9):
            if self.damage[i] < 0:
                time_to_fix += 0.1
        if time_to_fix == 0:
            return

        uprint("")
        time_to_fix += self.new_damage
        if time_to_fix >= 1:
            time_to_fix = 0.9
        uprint("Technicians standing by to effect repairs to your ship;")
        uprint("Estimated time to repair: %s stardates" % 0.01 * int(100 * time_to_fix))
        auth = input(optupper("Will you authorize the repair order (Y/N)? "))
        if auth.upper() != "Y":
            return
        for i in range(1, 9):
            if self.damage[i] < 0:
                self.damage[i] = 0
        self.mission.curr_stardate += time_to_fix + 0.1
        self.print_state_of_repair()
        return

    def libcom(self):
        if self.damage[8] < 0:
            uprint("Computer disabled")
            return

        while True:
            a = input(optupper("Computer active and awaiting command: "))
            a = a.strip()
            if a == "":
                uprint("Functions available from library-computer:")
                uprint("   0 = Cumulative galactic record")
                uprint("   1 = Status report")
                uprint("   2 = Photon torpedo data")
                uprint("   3 = Starbase nav data")
                uprint("   4 = Direction/distance calcultor")
                uprint("   5 = Galaxy 'region name' map")
                uprint("")
                continue
            try:
                inta = -1
                inta = int(a)
                a = inta
            except:
                pass

            if a < 0:
                return
            if a > 5:
                return
            if a == 0:
                return self.cumulative_galactic_record()
            if a == 1:
                return self.status_report()
            if a == 2:
                return self.photon_torpedo_data()
            if a == 3:
                return self.starbase_nav_data()
            if a == 4:
                return self.dir_dist_calculator()
            if a == 5:
                return self.galaxy_map()
            continue

    def photon_torpedo_data(self):
        klingons = self.quadrant.klingons

        if klingons == 0:
            uprint("Science officer Spock reports  'Sensors show no enemy ships")
            uprint("                                in this quadrant'")
            return

        strplural = ""
        if klingons > 1:
            strplural = "s"
        uprint("From Enterprise to Klingon battle cruiser%s" % strplural)

        for i in range(0, Galaxy.MAX_KLINGONS):
            klingon = self.mission.galaxy.klingon[i]
            if klingon.hitpoints == 0:
                continue
            calc_dir_and_dist(self.sector_x, self.sector_y, klingon.x, klingon.y)

        return

    def resign(self):
        uprint(
            "There were %s Klingon battle cruisers left at"
            % self.mission.galaxy.klingons_total
        )
        uprint("the end of your mission.")
        uprint("")
        uprint("")
        if self.mission.galaxy.starbases_total == 0:
            return GAME_OVER
        uprint("The Federation is in need of a new starship commander")
        uprint("for a similar mission -- if there is a volunteer,")
        answer = input(optupper("let him step forward and enter 'AYE': "))
        if answer.upper() == "AYE":
            return GAME_RESTART

        return GAME_OVER

    def game_over(self):
        """
        END OF GAME
        """
        uprint("It is stardate %s " % self.mission.curr_stardate)
        return self.resign()

    def starbase_nav_data(self):
        if self.mission.galaxy.count_starbases(self.quadrant_x, self.quadrant_y) == 0:
            uprint("Mr. Spock reports,  'Sensors show no starbases in this quadrant.'")
            return
        uprint("From Enterprise to starbase:")

        sx = self.mission.galaxy.starbase_x
        sy = self.quadrant.starbase_y
        calc_dir_and_dist(self.sector_x, self.sector_y, sx, sy)
        return

    def command_loop(self):
        self.fly_to(self.quadrant_x, self.quadrant_y, self.sector_x, self.sector_y)
        self.srs_and_startup()
        # ["NAV","SRS","LRS","PHA","TOR","SHE","DAM","COM","XXX"]
        run_commands = [
            self.navigation,
            self.short_range_scan,
            self.long_range_scan,
            self.phaser,
            self.torpedo,
            self.shield,
            self.damage_control,
            self.libcom,
            self.resign,
            self.help,
        ]

        while True:
            command = self.ask_command()
            try:
                run_command = run_commands[command]
            except:
                uprint("Not implemented.")
                exit(1)

            result = run_command()
            if result:
                return result

    ###########
    # Help section not present in original game
    # but integrated as interactive help from "instructions" program
    ###########
    def help(self):
        help_commands = [
            self.help_rul,
            self.help_nav,
            self.help_srs,
            self.help_lrs,
            self.help_pha,
            self.help_tor,
            self.help_she,
            self.help_dam,
            self.help_com,
        ]
        command = self.ask_command(help=True)
        try:
            help_command = help_commands[command]
        except:
            uprint("No help available for that command.")
            return

        help_command()
        uprint("")
        return

    def help_rul(self):
        uprint("      Instructions for 'Super Star Trek'")
        uprint("")
        uprint("1. When you see 'Command ?' printed, enter one of the legal")
        uprint("     commands (NAV,SRS,LRS,PHA,TOR,SHE,DAM,COM, OR XXX).")
        uprint("2. If you should type in an illegal command, you'll get a short")
        uprint("     list of the legal commands printed out.")
        uprint("3. Some commands require you to enter data (for example, the")
        uprint("     'NAV' command comes back with 'Course (1-9) ?'.) If you")
        uprint("     type in illegal data (like negative numbers), the command")
        uprint("     will be aborted")
        uprint("")
        uprint("     The galaxy is divided into an 8 x 8 quadrant grid,")
        uprint("and each quadrant is further divided into an 8 x 8 sector grid.")
        uprint("")
        uprint("     You will be assigned a starting point somewhere in the")
        uprint("galaxy to begin a tour of duty as a commander of the starship")
        uprint("Enterprise; your mission: To seek and destroy the fleet of")
        uprint("Klingon warships which are menacing the United Federation of")
        uprint("planets.")
        return

    def help_nav(self):
        uprint("NAV command = Warp engine control --")
        uprint("     Course is in a circular numerical      4  3  2")
        uprint("     vector arrangement as shown.            . . .")
        uprint("     Integer and real values may be           ...")
        uprint("     used.  (Thus course 1.5 is half-     5 ---*--- 1")
        uprint("     way between 1 and 2.                     ...")
        uprint("                                             . . .")
        uprint("     Values may approach 9.0, which         6  7  8")
        uprint("     itself is equivalent to 1.0.")
        uprint("                                            COURSE")
        uprint("     One warp factor is the size of ")
        uprint("     one quadrant.  Therefore, to get")
        uprint("     from quadrant 6,5 to 5,5, you would")
        uprint("     use course 3, warp factor 1.")
        return

    def help_srs(self):
        uprint("SRS command = Short Range Sensor scan")
        uprint("     Shows you a scan of your present quadrant.")
        uprint("")
        uprint("     Symbology on your sensor screen is as follows:")
        uprint("        <*> = Your starship's position")
        uprint("        +K+ = Klingon battle cruiser")
        uprint("        >!< = Federation starbase (Refuel/repair/re-arm here!)")
        uprint("         *  = Star")
        uprint("")
        uprint("     A condensed 'status report' will also be presented.")
        return

    def help_lrs(self):
        uprint("LRS command = Long range sensor scan")
        uprint("     Shows conditions in space for one quadrant on each side")
        uprint("     of the Enterprise (which is in the middle of the scan)")
        uprint("     The scan is coded in the form '###' where the units digit")
        uprint("     is the number of stars, the tens digit is the number of")
        uprint("     starbases, and the hundreds digit is the number of")
        uprint("     Klingons.")
        uprint("")
        uprint("     Example - 207 = 2 Klingons, no starbases, and 7 stars.")
        return

    def help_pha(self):
        uprint("PHA command = Phaser control.")
        uprint("     Allows you to destroy the Klingon battle cruisers by ")
        uprint("     zapping them with suitably large units of energy to")
        uprint("     deplete their shield power.  (Remember, Klingons have")
        uprint("     phasers too!)")
        return

    def help_tor(self):
        uprint("TOR command = Photon torpedo control")
        uprint("     Torpedo course is the same as used in warp engine control.")
        uprint("     If you hit the Klingon vessel, it is destroyed and")
        uprint("     cannot fire back at you. If you miss, you are subject to")
        uprint("     its phaser fire. In either case, you are also subject to")
        uprint("     the phase fire of all other Klingons in the quadrant.")
        uprint("")
        uprint("     The library-computer (COM command) has an option to ")
        uprint("     compute torpedo trajectory for you (Option 2).")
        return

    def help_she(self):
        uprint("SHE command = Shield control")
        uprint("     Defines the number of energy units to be assigned to the")
        uprint("     shields. Energy is taken from total ship's energy. Note")
        uprint("     that the status display total energy includes shield energy")
        return

    def help_dam(self):
        uprint("DAM command = Damage control report")
        uprint("     Gives the state of repair of all devices, where a negative")
        uprint("     'state of repair' shows that the device is temporarily")
        uprint("     damaged.")
        return

    def help_com(self):
        uprint("COM command = library-computer")
        uprint("     The library-computer contains six options:")
        uprint("     Option 0 = Cumulative Galactic Record")
        uprint("        This options shows computer memory of the results of all")
        uprint("        previous short and long range sensor scans")
        uprint("     Option 1 = Status report")
        uprint("        This option shows the number of Klingons, stardates,")
        uprint("        and starbases remaining in the game.")
        uprint("     Option 2 = Photon torpedo data")
        uprint("        Which gives directions and distance from the Enterprise")
        uprint("        to all Klingons in your quadrant")
        uprint("     OPTION 3 = Starbase NAV data")
        uprint("        This option gives direction and distance to any ")
        uprint("        starbase within your quadrant")
        uprint("     OPTION 4 = Direction/distance calculator")
        uprint("        This option allows you to enter coordinates for")
        uprint("        direction/distance calculations")
        uprint("     OPTION 5 = Galactic / Region name / map")
        uprint("        This option prints the names of the sixteen major")
        uprint("        galactic regions referred to in the game.")
        return

    def exceed_quadrant_limits(self, start_x, start_y, course_x, course_y, energy):
        x = 8 * self.quadrant_x + start_x + energy * course_x
        y = 8 * self.quadrant_y + start_y + energy * course_y
        self.quadrant_x = int(x / 8)
        self.quadrant_y = int(y / 8)
        self.sector_x = int(x - (8 * self.quadrant_x))
        self.sector_y = int(y - (8 * self.quadrant_y))
        if self.sector_x == 0:
            self.quadrant_x -= 1
            self.sector_x = 8
        if self.sector_y == 0:
            self.quadrant_y -= 1
            self.sector_y = 8

        cross_perimeter = False
        if self.quadrant_x < 1:
            cross_perimeter = True
            self.quadrant_x = 1
            self.sector_x = 1

        if self.quadrant_y < 1:
            cross_perimeter = True
            self.quadrant_y = 1
            self.sector_y = 1

        if self.quadrant_x > 8:
            cross_perimeter = True
            self.quadrant_x = 8
            self.sector_x = 8

        if self.quadrant_y > 8:
            cross_perimeter = True
            self.quadrant_y = 8
            self.sector_y = 8

        if cross_perimeter:
            uprint("Lt. Uhura reports message from Starfleet Command:")
            uprint("  'Permission to attempt crossing of galactic perimeter")
            uprint("  is hereby *DENIED*.  Shut down your engines.'")
            uprint("Chief engineer Scott reports  'Warp engines shut down")
            uprint(
                "  at sector %s,%s of quadrant %s,%s.'"
                % (self.sector_x, self.sector_y, self.quadrant_x, self.quadrant_y)
            )
            if (
                self.mission.curr_stardate
                > self.mission.stardate_initial + self.mission.days
            ):
                return GAME_OVER

        return

    def move_starship(self, course, warp, energy_provided):
        self.quadrant.set_content(self.sector_x, self.sector_y, "   ")
        course_x = self.course_x[int(course)] + (
            self.course_x[int(course) + 1] - self.course_x[int(course)]
        ) * (course - int(course))
        course_y = self.course_y[int(course)] + (
            self.course_y[int(course) + 1] - self.course_y[int(course)]
        ) * (course - int(course))
        start_x = self.sector_x
        start_y = self.sector_y
        start_quadrant_x = self.quadrant_x
        start_quadrant_y = self.quadrant_y

        set_sector = True
        for i in range(0, energy_provided):
            self.sector_x += course_x
            self.sector_y += course_y
            if (
                self.sector_x < 1
                or self.sector_x >= 9
                or self.sector_y < 1
                or self.sector_y >= 9
            ):
                self.exceed_quadrant_limits(
                    start_x, start_y, course_x, course_y, energy_provided
                )
                if self.quadrant_x == start_quadrant_x:
                    if self.quadrant_y == start_quadrant_y:
                        set_sector = False
                        break
                self.mission.curr_stardate += 1
                self.maneuver_energy_shields(energy_provided)
                self.fly_to(
                    self.quadrant_x, self.quadrant_y, self.sector_x, self.sector_y
                )
                return self.short_range_scan()
                return
            if self.quadrant.get_content(self.sector_x, self.sector_y) == "   ":
                continue
            self.sector_x = int(self.sector_x - course_x)
            self.sector_y = int(self.sector_y - course_y)
            uprint(
                "Warp engines shut down at sector %s,%s due to bad navigation"
                % (self.sector_x, self.sector_y)
            )
            break

        if set_sector:
            self.sector_x = int(self.sector_x)
            self.sector_y = int(self.sector_y)

        self.quadrant.set_content(self.sector_x, self.sector_y, "<*>")
        self.maneuver_energy_shields(energy_provided)
        time_spent = 1
        if warp < 1:
            time_spent = 0.1 * int(10 * warp)
        self.mission.curr_stardate += time_spent
        if (
            self.mission.curr_stardate
            > self.mission.stardate_initial + self.mission.days
        ):
            return GAME_OVER

        return self.short_range_scan()

    def dir_dist_calculator(self):
        uprint("Direction/distance calculator:")
        uprint(
            "You are at quadrant %s,%s sector %s,%s"
            % (self.quadrant_x, self.quadrant_y, self.sector_x, self.sector_y)
        )
        uprint("Please enter")
        (from_x, from_y) = xy_input("  Initial coordinates (x,y)")
        (to_x, to_y) = xy_input("    Final coordinates (x,y)")
        return calc_dir_and_dist(from_x, from_y, to_x, to_y)

    def cumulative_galactic_record(self):
        """
        7530 REM CUM GALACTIC RECORD
        7540 REM INPUT "DO YOU WANT A HARDCOPY? IS THE TTY ON (Y/N)";A$
        7542 REM IF A$="Y" THEN POKE1229,2:POKE1237,3:NULL1    
        """
        uprint("")
        uprint(
            "        Computer record of galaxy for quadrant %s,%s"
            % (self.quadrant_x, self.quadrant_y)
        )
        uprint("")
        self.print_map(visited=1, galaxy=0)
        return

    def galaxy_map(self):
        uprint("                        THE GALAXY")
        self.print_map(visited=0, galaxy=1)
        return

    def print_map(self, visited=0, galaxy=0):
        uprint("       1     2     3     4     5     6     7     8")
        stro1 = "     ----- ----- ----- ----- ----- ----- ----- -----"
        uprint(stro1)
        for i in range(1, 9):
            line = "  %s" % (i)
            if visited != 0:
                for j in range(1, 9):
                    line += "   "
                    cell = self.mission.galaxy.seen[i][j]
                    if cell == 0:
                        line += "***"
                    else:
                        toprint = ("000" + str((cell + 1000) % 1000))[-3:]
                        line += toprint
                uprint(line)
                continue
            q = Quadrant(i, 1)
            qname = q.name(region_only=True)
            j0 = int(15 - 0.5 * len(qname))
            line = " " * j0 + qname
            line += (27 - len(line)) * " "

            q = Quadrant(i, 5)
            qname = q.name(region_only=True)
            j0 = int(15 - 0.5 * len(qname))
            uprint(line + (" " * j0 + qname))
            uprint(stro1)
        uprint("")
        return

    def status_report(self):
        # REM STATUS REPORT
        uprint("   Status report:")
        plural = ""

        if self.mission.galaxy.klingons_total != 1:
            plural = "s"
        uprint("Klingon%s left: %s" % (plural, self.mission.galaxy.klingons_total))

        stardates_left = 0.1 * int(
            (
                self.mission.stardate_initial
                + self.mission.days
                - self.mission.curr_stardate
            )
            * 10
        )

        uprint("Mission must be completed in %s stardates" % stardates_left)
        if self.mission.galaxy.starbases_total == 0:
            uprint("Your stupidity has left you on your own in")
            uprint("  the galaxy -- you have no starbases left!")
        else:
            plural = ""
            if self.mission.galaxy.starbases_total > 1:
                plural = "s"
            uprint(
                "The Federation is maintaining %s starbase%s in the galaxy"
                % (self.mission.galaxy.starbases_total, plural)
            )
        return self.damage_control()


class Galaxy:
    MAX_KLINGONS = 3  # per quadrant

    def __init__(self, starship):
        self.starship = starship
        self.galaxy = [x[:] for x in [[0] * 9] * 9]
        self.seen = [x[:] for x in [[0] * 9] * 9]
        self.klingon = []
        self.n = []
        for i in range(Galaxy.MAX_KLINGONS):
            self.klingon.append(Klingon(0, 0, 0))
            self.n.append(0)

        # Set up what exists in galaxy
        self.klingons_total = 0
        self.starbases_total = 0

        for i in range(1, 9):
            for j in range(1, 9):
                klingons = 0
                self.seen[i][j] = 0
                r1 = rnd()
                if r1 > 0.98:
                    klingons += 1
                    self.klingons_total += 1
                elif r1 > 0.95:
                    klingons += 2
                    self.klingons_total += 2
                elif r1 > 0.80:
                    klingons += 3
                    self.klingons_total += 3
                starbases = 0
                if rnd() > 0.96:
                    starbases = 1
                    self.starbases_total += 1
                self.galaxy[i][j] = (klingons * 100) + (starbases * 10) + randompos()

        if self.klingons_total > starship.mission.days:
            starship.mission.days = self.klingons_total + 1

        if self.starbases_total == 0:
            quadrant_x = starship.quadrant_x
            quadrant_y = starship.quadrant_y

            if self.galaxy[quadrant_x][quadrant_y] < 200:
                self.galaxy[quadrant_x][quadrant_y] += 120
                self.klingons_total += 1
            self.starbases_total = 1
            self.galaxy[quadrant_x][quadrant_y] += 10
            starship.quadrant_x = randompos()
            starship.quadrant_y = randompos()

    def enter_quadrant(self, quadrant_x, quadrant_y):
        # not sure what the point of this is
        self.seen[quadrant_x][quadrant_y] = self.galaxy[quadrant_x][quadrant_y]

        # decode compacted quadrant contents
        self.klingons = self.count_klingons(quadrant_x, quadrant_y)
        self.starbases = self.count_starbases(quadrant_x, quadrant_y)
        self.stars = self.count_stars(quadrant_x, quadrant_y)

        for i in range(0, Galaxy.MAX_KLINGONS):
            self.klingon[i].x = 0
            self.klingon[i].y = 0
            self.klingon[i].hitpoints = 0

        # clear quadrant
        quadrant = Quadrant(quadrant_x, quadrant_y)
        self.quadrant = quadrant
        quadrant.klingons = self.klingons

        # Position Enterprise in quadrant, then place requisite number of
        # klingons, star bases and stars elsewhere.
        quadrant.set_content(self.starship.sector_x, self.starship.sector_y, "<*>")

        if self.klingons >= 1:
            for i in range(0, self.klingons):
                sector_x, sector_y = quadrant.find_empty_sector()
                quadrant.set_content(sector_x, sector_y, "+K+")
                self.klingon[i].x = sector_x
                self.klingon[i].y = sector_y
                self.klingon[i].hitpoints = Klingon.strength * (0.5 + rnd())

        if self.starbases >= 1:
            sector_x, sector_y = quadrant.find_empty_sector()
            quadrant.set_content(sector_x, sector_y, ">!<")
            quadrant.starbase_x = sector_x
            quadrant.starbase_y = sector_y
            self.starbase_x = sector_x
            self.starbase_y = sector_y

        for i in range(0, self.stars):
            sector_x, sector_y = quadrant.find_empty_sector()
            quadrant.set_content(sector_x, sector_y, " * ")

        return quadrant

    def count_klingons(self, quadrant_x, quadrant_y):
        return int(self.galaxy[quadrant_x][quadrant_y] * 0.01)

    def count_starbases(self, quadrant_x, quadrant_y):
        return int(
            self.galaxy[quadrant_x][quadrant_y] * 0.1
        ) - 10 * self.count_klingons(quadrant_x, quadrant_y)

    def count_stars(self, quadrant_x, quadrant_y):
        return (
            self.galaxy[quadrant_x][quadrant_y]
            - 100 * self.count_klingons(quadrant_x, quadrant_y)
            - 10 * self.count_starbases(quadrant_x, quadrant_y)
        )


class Mission:
    MAX_KLINGONS = 3

    def __init__(self):
        self.n = []

        self.curr_stardate = int(rnd() * 20 + 10) * 100
        self.stardate_initial = self.curr_stardate
        self.days = 25 + int(rnd() * 10)

        self.starship = Starship(self)
        self.galaxy = Galaxy(self.starship)
        self.klingons_total_initial = self.galaxy.klingons_total

        return

    def show(self):
        # klingons_total, starbases_total, stardate_initial, days):
        pluralizer = ""
        tobe_singularplural = " is "

        if self.galaxy.starbases_total != 1:
            pluralizer = "s"
            tobe_singularplural = "are"

        uprint("Your orders are as follows:")
        uprint(
            "     Destroy the %s klingon warships which have invaded"
            % self.galaxy.klingons_total
        )
        uprint("   the galaxy before they can attack federation headquarters")
        uprint(
            "   on stardate %s.  This gives you %s days.  There %s"
            % (self.stardate_initial + self.days, self.days, tobe_singularplural)
        )
        uprint(
            "   %s starbase%s in the galaxy for resupplying your ship"
            % (self.galaxy.starbases_total, pluralizer)
        )
        uprint("")
        x = input(optupper("Press enter to continue."))
        return

    def start(self):
        while True:
            starship = self.starship
            result = starship.command_loop()
            if result == GAME_OVER:
                break
            if result == GAME_RESTART:
                return GAME_RESTART

    def print_status(self):

        if self.starship.quadrant.klingons > 0:
            condition = "*RED*"
        else:
            if self.starship.energy < (self.starship.energy_initial * 0.1):
                condition = "Green"
            else:
                condition = "Yellow"

        stats = []
        stats.append("STARDATE           %s" % self.curr_stardate)
        stats.append("CONDITION          %s" % condition)
        stats.append(
            "QUADRANT           %s,%s"
            % (self.starship.quadrant_x, self.starship.quadrant_y)
        )
        stats.append(
            "SECTOR             %s,%s"
            % (self.starship.sector_x, self.starship.sector_y)
        )
        stats.append("PHOTON TORPEDOES   %s" % self.starship.torpedos)
        stats.append(
            "TOTAL ENERGY       %s" % (self.starship.energy + self.starship.shields)
        )
        stats.append("SHIELDS            %s" % self.starship.shields)
        stats.append("KLINGONS REMAINING %s" % self.galaxy.klingons_total)
        uprint("-" * 33)
        for i in range(0, 8):
            line = ""
            for j in range(0, 8):
                line += " "
                line += self.starship.quadrant.get_content(i + 1, j + 1)
            line += 7 * " " + stats[i]
            uprint(line)
        uprint("-" * 33)

    def klingons_destroyed():
        uprint("Congratulations, captain!  The last Klingon battle cruiser")
        uprint("menacing the Federation has been destroyed.")
        uprint("")
        rating = (
            1000
            * (
                self.mission.klingons_total_initial
                / (self.mission.curr_stardate - self.mission.stardate_initial)
            )
            ** 2
        )
        uprint("Your efficiency rating is %s" % rating)
        return GAME_OVER


def get_device_name(num):
    return [
        "WARP ENGINES",
        "SHORT RANGE SENSORS",
        "LONG RANGE SENSORS",
        "PHASER CONTROL",
        "PHOTON TUBES",
        "DAMAGE CONTROL",
        "SHIELD CONTROL",
        "LIBRARY-COMPUTER",
    ][(num - 1) % 8]


title()
while True:
    mission = Mission()
    mission.show()
    result = mission.start()
    if result == GAME_RESTART:
        continue
    break
