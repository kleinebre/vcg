def title():
    print((33*" ")+"BATNUM")
    print((15*" ")+"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print(""):print(""):print("")
    print("THIS PROGRAM IS A 'BATTLE OF NUMBERS' GAME, WHERE THE"
    print("COMPUTER IS YOUR OPPONENT."
    print("")
    print("THE GAME STARTS WITH AN ASSUMED PILE OF OBJECTS. YOU"
    print("AND YOUR OPPONENT ALTERNATELY REMOVE OBJECTS FROM THE PILE."
    print("NOT. YOU CAN ALSO SPECIFY SOME OTHER BEGINNING CONDITIONS."
    print("WINNING IS DEFINED IN ADVANCE AS TAKING THE LAST OBJECT OR"
    print("DON'T USE ZERO, HOWEVER, IN PLAYING THE GAME."
    print("ENTER A NEGATIVE NUMBER FOR NEW PILE SIZE TO STOP PLAYING."
    print("")
    return

def vspace():
    for i in range(10):
        print("")

def pile_size():
    while True:
        try:
            raw_pile_size = input("ENTER PILE SIZE: ")
            pile_size = int(raw_pile_size)
        except TypeError:
            pile_size = 0
        if pile_size >= 1:
            return pile_size
        vspace()

def win_option():
    while True:
        try:
            raw_win_opt = input("ENTER WIN OPTION - 1 TO TAKE LAST, 2 TO AVOID LAST: ")
            win_opt = int(raw_win_opt)
        except TypeError:
            win_opt = 0
        if win_opt in (1, 2):
            return win_opt

def min_max():
    while True:
        try:
            raw_min, raw_max = input("ENTER MIN AND MAX ").split(",")
            min = int(raw_min)
            max = int(raw_max)
        except TypeError:
            min = 0
            max = 0
        if min <= max and min >=1:
            return min, max

def start_option():
    while True:
        try:
            raw_start_opt = input("ENTER START OPTION - 1 COMPUTER FIRST, 2 YOU FIRST ")
            start_opt = int(raw_win_opt)
            print("")
            print("")
        except TypeError:
            start_opt = 0
        if start_opt in (1, 2):
            return start_opt

while True:
    n = pile_size()
    m = win_option()
    a, b = min_max()
    s = start_option()
    c = a + b
    530 C=A+B
    540 IF S=2 THEN 570
    
    # computer move
    550 GOSUB 600
    560 IF W=1 THEN vspace(): continue

    # human move
    570 GOSUB 810
    580 IF W=1 THEN vspace(): continue
    590 GOTO 550

600 Q=N
610 IF M=1 THEN 630
620 Q=Q-1
630 IF M=1 THEN 680
640 IF N>MIN THEN 720
650 W=1
660 print("COMPUTER TAKES";N;"AND LOSES."
670 RETURN


680 IF N>MAX THEN 720
690 W=1
700 print("COMPUTER TAKES";N;"AND WINS."
710 RETURN


720 P=Q-C*INT(Q/C)
730 IF P>=MIN THEN 750
740 P=MIN
750 IF P<=MAX THEN 770
760 P=MAX
770 N=N-P
780 print("COMPUTER TAKES";P;"AND LEAVES";N
790 W=0
800 RETURN


810 print(""):print("YOUR MOVE ";
820 INPUT P
830 IF P<>0 THEN 870
840 print("I TOLD YOU NOT TO USE ZERO! COMPUTER WINS BY FORFEIT."
850 W=1
860 RETURN


870 IF P<>INT(P) THEN 920
880 IF P>=MIN THEN 910
890 IF P=N THEN 960
900 GOTO 920

910 IF P<=B THEN 940
920 print("ILLEGAL MOVE, REENTER IT ";
930 GOTO 820

940 N=N-P
950 IF N<>0 THEN 1030


960 IF M=1 THEN 1000
970 print("TOUGH LUCK, YOU LOSE."
980 W=1
990 RETURN


1000 print("CONGRATULATIONS, YOU WIN.")
1010 W=1
1020 RETURN


1030 IF N>=0 THEN W=0: RETURN
1040 N=N+P
1050 GOTO 920
