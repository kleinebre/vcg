	PRINT TAB(31);"BASKETBALL"
	PRINT TAB(15);"CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY"
	PRINT:PRINT:PRINT
	PRINT "THIS IS DARTMOUTH COLLEGE BASKETBALL.  YOU WILL BE DARTMOUTH"
	PRINT " CAPTAIN AND PLAYMAKER.  CALL SHOTS AS FOLLOWS:  1. LONG"
	PRINT " (30 FT.) JUMP SHOT; 2. SHORT (15 FT.) JUMP SHOT; 3. LAY"
	PRINT " UP; 4. SET SHOT."
	PRINT "BOTH TEAMS WILL USE THE SAME DEFENSE.  CALL DEFENSE AS"
	PRINT "FOLLOWS:  6. PRESS; 6.5 MAN-TO MAN; 7. ZONE; 7.5 NONE."
	PRINT "TO CHANGE DEFENSE, JUST TYPE 0 AS YOUR NEXT SHOT."
	INPUT "YOUR STARTING DEFENSE WILL BE";D:IF D<6 THEN GOSUB 2010:PRINT: GOTO yourshot
	PRINT
	INPUT "CHOOSE YOUR OPPONENT";O$
###### MAIN LOOP
center_jump:
    IF YS=1 then YS=0: GOTO yourshot
    PRINT "CENTER JUMP"
	IF RND(1)> 3/5 THEN 420
	PRINT O$;" CONTROLS THE TAP."
	GOSUB 3000: GOTO center_jump
420 PRINT "DARTMOUTH CONTROLS THE TAP."
	PRINT
yourshot:
    INPUT "YOUR SHOT";Z
	P=0
	IF Z<>INT(Z) THEN PRINT "INCORRECT ANSWER.  RETYPE IT. ";:GOTO yourshot
	IF Z<0 OR Z>4 THEN PRINT "INCORRECT ANSWER.  RETYPE IT. ";:GOTO yourshot
	IF RND(1)<.5 THEN 1000
	IF T<100 THEN 1000
	PRINT
	IF S(1)<>S(0) THEN PRINT "   ***** END OF GAME *****":PRINT "FINAL SCORE: DARTMOUTH:";S(1);"  ";O$;":";S(0):STOP

	PRINT:PRINT "   ***** END OF SECOND HALF *****":PRINT
	PRINT "SCORE AT END OF REGULATION TIME:"
	PRINT "        DARTMOUTH:";S(1);"  ";O$;":";S(0)
	PRINT
	PRINT "BEGIN TWO MINUTE OVERTIME PERIOD"
	T=93
	GOTO center_jump
###### END OF MAIN LOOP
two_minutes_left:
    PRINT
	PRINT "   *** TWO MINUTES LEFT IN THE GAME ***"
	PRINT
	RETURN
1000 ON Z GOTO 1040,1040
	GOTO 1300
1040 T=T+1
	IF T=50 THEN GOSUB 8000: GOTO center_jump
	IF T=92 THEN 1046
	GOTO 1050
1046 GOSUB two_minutes_left
1050 PRINT "JUMP SHOT"
	IF RND(1)>.341*D/8 THEN 1090
	PRINT "SHOT IS GOOD."
	GOSUB 7000
	GOSUB 3000: GOTO center_jump
1090 IF RND(1)>.682*D/8 THEN 1200
	PRINT "SHOT IS OFF TARGET."
	IF D/6*RND(1)>.45 THEN 1130
	PRINT "DARTMOUTH CONTROLS THE REBOUND."
	GOTO 1145
1130 PRINT "REBOUND TO ";O$
	GOSUB 3000: GOTO center_jump
1145 IF RND(1)<=.4 THEN 1300
	IF D<>6 THEN 1160
	IF RND(1)>.6 THEN PRINT "PASS STOLEN BY ";O$;" EASY LAYUP.":GOSUB 6000:PRINT: GOTO yourshot
1160 PRINT "BALL PASSED BACK TO YOU. ";
	YS=1: GOTO center_jump
	PRINT "BALL STOLEN. ";O$;"'S BALL."
	GOSUB 3000: GOTO center_jump
1200 IF RND(1)>.782*D/8 THEN 1250
	PRINT "SHOT IS BLOCKED.  BALL CONTROLLED BY ";
	IF RND(1)>.5 THEN 1242
	PRINT "DARTMOUTH."
	YS=1: GOTO center_jump
1242 PRINT O$;"."
	GOSUB 3000: GOTO center_jump
1250 IF RND(1)>.843*D/8 THEN 1270
	PRINT "SHOOTER IS FOULED.  TWO SHOTS."
	GOSUB 4000
	GOSUB 3000: GOTO center_jump
1270 PRINT "CHARGING FOUL.  DARTMOUTH LOSES BALL."
	GOSUB 3000: GOTO center_jump
1300 T=T+1
	IF T=50 THEN GOSUB 8000: GOTO center_jump
	IF T=92 THEN 1304
	GOTO 1305
1304 GOSUB two_minutes_left
1305 IF Z=0 THEN GOSUB 2010:PRINT: GOTO yourshot
	IF Z>3 THEN PRINT "SET SHOT." ELSE PRINT "LAY UP."
	IF 7/D*RND(1)<=.4 THEN PRINT "SHOT IS GOOD.  TWO POINTS.":GOSUB 7000:GOSUB 3000: GOTO center_jump
	IF 7/D*RND(1)>.7 THEN 1500
	PRINT "SHOT IS OFF THE RIM."
	IF RND(1)<=2/3 THEN PRINT O$;" CONTROLS THE REBOUND.":GOSUB 3000: GOTO center_jump
	PRINT "DARTMOUTH CONTROLS THE REBOUND."
	IF RND(1)<=.4 THEN 1300
	PRINT "BALL PASSED BACK TO YOU.";
	YS=1: GOTO center_jump
1500 IF 7/D*RND(1)<=.875 THEN PRINT "SHOOTER FOULED.  TWO SHOTS.":GOSUB 4000:GOSUB 3000: GOTO center_jump
	IF 7/D*RND(1)<=.925 THEN PRINT "SHOT BLOCKED. ";O$;"'S BALL.":GOSUB 3000: GOTO center_jump
	PRINT "CHARGING FOUL.  DARTMOUTH LOSES THE BALL."
	GOSUB 3000: GOTO center_jump
2010 INPUT "YOUR NEW DEFENSIVE ALLIGNMENT IS";D
	IF D<6 THEN 2010
	RETURN

3000 P=1
	T=T+1
	IF T=50 THEN GOSUB 8000: GOTO center_jump
	PRINT
	Z1=10/4*RND(1)+1
	IF Z1>2 THEN 3500
	PRINT "JUMP SHOT."
	IF 8/D*RND(1)<=.35 THEN PRINT "SHOT IS GOOD.":GOSUB 6000:PRINT: YS=1: GOTO center_jump
	IF 8/D*RND(1)>.75 THEN 3200
	PRINT "SHOT IS OFF RIM."
3110 IF D/6*RND(1)<=.5 THEN PRINT "DARTMOUTH CONTROLS THE REBOUND.":PRINT: YS=1: GOTO center_jump
	PRINT O$;" CONTROLS THE REBOUND."
	IF D<>6 THEN 3165
    IF RND(1)<=.75 THEN PRINT "BALL STOLEN.  EASY LAY UP FOR DARTMOUTH.":GOSUB 7000: GOTO 3000
3165 IF RND(1)<=.5 THEN PRINT "PASS BACK TO ";O$;" GUARD.":GOTO 3000
	GOTO 3500
3200 IF 8/D*RND(1)<=.9 THEN PRINT "PLAYER FOULED.  TWO SHOTS.":GOSUB 4000:PRINT: YS=1: GOTO center_jump
	PRINT "OFFENSIVE FOUL.  DARTMOUTH'S BALL."
	PRINT: YS=1: GOTO center_jump
3500 IF Z1>3 THEN PRINT "SET SHOT." ELSE PRINT "LAY UP."
	IF 7/D*RND(1)>.413 THEN PRINT "SHOT IS MISSED.":GOTO 3110
	PRINT "SHOT IS GOOD."
	GOSUB 6000
	PRINT: YS=1: GOTO center_jump

4000 REM FOUL SHOOTING
	IF RND(1)<=.49 THEN PRINT "SHOOTER MAKES BOTH SHOTS.":S(1-P)=S(1-P)+2:GOSUB 7500:RETURN
	IF RND(1)<=.75 THEN PRINT "BOTH SHOTS MISSED.": RETURN
	PRINT "SHOOTER MAKES ONE SHOT AND MISSES ONE.":S(1-P)=S(1-P)+1:GOSUB 7500: RETURN


6000 S(0)=S(0)+2
	GOSUB 7500
	RETURN
7000 S(1)=S(1)+2
	GOSUB 7500
	RETURN
7500 PRINT "SCORE: ";S(1);"TO";S(0)
	RETURN
8000 PRINT:PRINT "   ***** END OF FIRST HALF *****":PRINT
	PRINT "SCORE: DARTMOUTH:";S(1);"  ";O$;":";S(0)
	PRINT
	PRINT
	RETURN
