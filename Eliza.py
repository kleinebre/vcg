#!/usr/bin/env python
import re

print(16 * " " + "**************************")
print(26 * " " + "ELIZA")
print(20 * " " + "CREATIVE COMPUTING")
print(18 * " " + "MORRISTOWN, NEW JERSEY")
print("")
print(19 * " " + "ADAPTED FOR IBM PC BY")
print(14 * " " + "PATRICIA DANIELSON AND PAUL HASHFIELD")
print(12 * " " + "PYTHON VERSION BY MARC BREVOORT")
print(16 * " " + "**************************")
print("")
print("")
print("")
words_in_out = [
    ("ARE", "AM"),
    ("WERE", "WAS"),
    ("YOU", "I"),
    ("YOUR ", "MY"),
    ("ME", "YOU"),
]

replies = {
    "CAN YOU": [
        "DON'T YOU BELIEVE THAT I CAN*?",
        "PERHAPS YOU WOULD LIKE TO BE LIKE ME*?",
        "YOU WANT ME TO BE ABLE TO*?",
    ],
    "CAN I": ["PERHAPS YOU DON'T WANT TO*?", "DO YOU WANT TO BE ABLE TO*?"],
    ("YOU ARE", "YOURE"): [
        "WHAT MAKES YOU THINK I AM*?",
        "DOES IT PLEASE YOU TO BELIEVE I AM*?",
        "PERHAPS YOU WOULD LIKE TO BE*?",
        "DO YOU SOMETIMES WISH YOU WERE*?",
    ],
    ("I DONT"): [
        "DON'T YOU REALLY*?",
        "WHY DON'T YOU*?",
        "DO YOU WISH TO BE ABLE TO*?",
        "DOES THAT TROUBLE YOU*?",
    ],
    "I FEEL": ["DO YOU OFTEN FEEL*?", "DO YOU ENJOY FEELING*"],
    "WHY DONT YOU": [
        "DO YOU REALLY BELIEVE I DON'T*?",
        "PERHAPS IN GOOD TIME I WILL*.",
        "DO YOU WANT ME TO*?",
    ],
    "WHY CANT I": ["DO YOU THINK YOU SHOULD BE ABLE TO*?", "WHY CAN'T YOU*?"],
    "ARE YOU": [
        "WHY ARE YOU INTERESTED IN WHETHER OR NOT I AM*?",
        "WOULD YOU PREFER IF I WERE NOT*?",
        "PERHAPS IN YOUR FANTASIES I AM*?",
    ],
    "I CANT": [
        "HOW DO YOU KNOW YOU CAN'T*?",
        "HAVE YOU TRIED?",
        "PERHAPS YOU CAN NOW*?",
    ],
    ("I AM", "IM"): [
        "DID YOU COME TO ME BECAUSE YOU ARE*?",
        "HOW LONG HAVE YOU BEEN*?",
        "DO YOU BELIEVE IT IS NORMAL TO BE*?",
        "DO YOU ENJOY BEING*?",
    ],
    "YOU": [
        "WE WERE DISCUSSING YOU--NOT ME.",
        "OH, I*?",
        "YOU'RE NOT REALLY TALKING ABOUT ME, ARE YOU?",
    ],
    "I WANT": [
        "WHAT WOULD IT MEAN TO YOU IF YOU GOT*?",
        "WHY DO YOU WANT*?",
        "SUPPOSE YOU SOON GOT*?",
        "WHAT IF YOU NEVER GOT*?",
        "I SOMETIMES ALSO WANT*.",
    ],
    ("WHAT", "HOW", "WHO", "WHERE", "WHEN", "WHY"): [
        "WHY DO YOU ASK?",
        "DOES THAT QUESTION INTEREST YOU?",
        "WHAT ANSWER WOULD PLEASE YOU THE MOST?",
        "WHAT DO YOU THINK?",
        "ARE SUCH QUESTIONS ON YOUR MIND OFTEN?",
        "WHAT IS IT THAT YOU REALLY WANT TO KNOW?",
        "HAVE YOU ASKED ANYONE ELSE?",
        "HAVE YOU ASKED SUCH QUESTIONS BEFORE?",
        "WHAT ELSE COMES TO MIND WHEN YOU ASK THAT?",
    ],
    "NAME": ["NAMES DON'T INTEREST ME.", "I DON'T CARE ABOUT NAMES --PLEASE GO ON."],
    ("CAUSE", "BECAUSE"): [
        "IS THAT THE REAL REASON?",
        "DON'T ANY OTHER REASONS COME TO MIND?",
        "DOES THAT REASON EXPLAIN ANYTHING ELSE?",
        "WHAT OTHER REASONS MIGHT THERE BE?",
    ],
    "SORRY": [
        "PLEASE DON'T APOLOGIZE!",
        "APOLOGIES ARE NOT NECESSARY.",
        "WHAT FEELINGS DO YOU HAVE WHEN YOU APOLOGIZE?",
        "DON'T BE SO DEFENSIVE!",
    ],
    "DREAM": [
        "WHAT DOES THAT DREAM SUGGEST TO YOU?",
        "DO YOU DREAM OFTEN?",
        "WHAT PERSONS APPEAR IN YOUR DREAMS?",
        "ARE YOU DISTURBED BY YOUR DREAMS?",
    ],
    ("HELLO", "HI"): ["HOW DO YOU DO ...PLEASE STATE YOUR PROBLEM."],
    "MAYBE": [
        "YOU DON'T SEEM QUITE CERTAIN.",
        "WHY THE UNCERTAIN TONE?",
        "CAN'T YOU BE MORE POSITIVE?",
        "YOU AREN'T SURE?",
        "DON'T YOU KNOW?",
    ],
    ("NO", "NOPE"): [
        "ARE YOU SAYING NO JUST TO BE NEGATIVE?",
        "YOU ARE BEING A BIT NEGATIVE.",
        "WHY NOT?",
        "ARE YOU SURE?",
        "WHY NO?",
    ],
    "YOUR": ["WHY ARE YOU CONCERNED ABOUT MY*", "WHAT ABOUT YOUR OWN*"],
    "ALWAYS": [
        "CAN YOU THINK OF A SPECIFIC EXAMPLE?",
        "WHEN?",
        "WHAT ARE YOU THINKING OF?",
        "REALLY, ALWAYS?",
    ],
    "THINK": [
        "DO YOU REALLY THINK SO?",
        "BUT YOU ARE NOT SURE YOU*?",
        "DO YOU DOUBT YOU*?",
    ],
    "ALIKE": [
        "IN WHAT WAY?",
        "WHAT RESEMBLANCE DO YOU SEE?",
        "WHAT DOES THE SIMILARITY SUGGEST TO YOU?",
        "WHAT OTHER CONNECTIONS DO YOU SEE?",
        "COULD THERE REALLY BE SOME CONNECTION?",
        "HOW?",
    ],
    "YES": ["YOU SEEM QUITE POSITIVE.", "ARE YOU SURE?", "I SEE.", "I UNDERSTAND."],
    "FRIEND": [
        "WHY DO YOU BRING UP THE TOPIC OF FRIENDS?",
        "DO YOUR FRIENDS WORRY YOU?",
        "DO YOUR FRIENDS PICK ON YOU?",
        "ARE YOU SURE YOU HAVE ANY FRIENDS?",
        "DO YOU IMPOSE ON YOUR FRIENDS?",
        "PERHAPS YOUR LOVE FOR FRIENDS WORRIES YOU.",
    ],
    "COMPUTER": [
        "DO COMPUTERS WORRY YOU?",
        "ARE YOU TALKING ABOUT ME IN PARTICULAR?",
        "ARE YOU FRIGHTENED BY MACHINES?",
        "WHY DO YOU MENTION COMPUTERS?",
        "WHAT DO YOU THINK MACHINES HAVE TO DO WITH YOUR PROBLEM?",
        "DON'T YOU THINK COMPUTERS CAN HELP PEOPLE?",
        "WHAT IS IT ABOUT MACHINES THAT WORRIES YOU?",
    ],
    None: [
        "SAY, DO YOU HAVE ANY PSYCHOLOGICAL PROBLEMS?",
        "WHAT DOES THAT SUGGEST TO YOU?",
        "I SEE.",
        "I'M NOT SURE I UNDERSTAND YOU FULLY.",
        "COME COME ELUCIDATE YOUR THOUGHTS.",
        "CAN YOU ELABORATE ON THAT?",
        "THAT IS QUITE INTERESTING.",
    ],
}

# postprocess multi-keyword reply blocks into single-keyword reply blocks
postprocessed_replies = {}
replies_used = {}
for key in replies:
    if not isinstance(key, tuple):
        keywords = [key]
    else:
        keywords = list(key)
    for keyword in keywords:
        postprocessed_replies[keyword] = replies[key]
        replies_used[keyword] = 0

replies = postprocessed_replies

# Greeting
print("HI! I'M ELIZA. WHAT'S YOUR PROBLEM?")
previous = ""
while True:
    request = "  {}  ".format(input("> "))
    request = request.upper()
    request = request.replace("'", "")
    if " SHUT " in request and " UP" in request:
        print("O.K. IF YOU FEEL THAT WAY I'LL SHUT UP....")
        break

    if request == previous:
        print("PLEASE DON'T REPEAT YOURSELF!")
        continue

    # find keywords in input
    found_keyword = None
    for keyword in replies:
        if keyword is None:
            continue

        if (keyword + " ") in request:
            found_keyword = keyword

    reply_words = ""
    if found_keyword:
        request = re.sub(".*?" + found_keyword, "", request)
        words = request.split(" ")
        changed_words = []
        for word in words:
            for swapwords in words_in_out:
                if word == swapwords[0]:
                    word = swapwords[1]
                elif word == swapwords[1]:
                    word = swapwords[0]
            changed_words.append(word)
        reply_words = " ".join(changed_words)

    possible_replies = replies[found_keyword]
    amount_of_replies = len(possible_replies)
    reply = possible_replies[replies_used[found_keyword] % amount_of_replies]
    replies_used[found_keyword] += 1
    reply = reply.replace("*", reply_words)
    print(reply)
