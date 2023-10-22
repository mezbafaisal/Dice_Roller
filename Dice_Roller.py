import random

# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),

    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│       ● │",
       "└─────────┘"),

    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│       ● │",
       "└─────────┘"),

    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),

    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),

    6:("┌─────────┐",
       "│ ●     ● │",
       "│ ●     ● │",
       "│ ●     ● │",
       "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?:"))

for die in range(num_of_dice):
     dice.append(random.randint(1, 6))

#Vertical Approch:
#for die in range(num_of_dice):
 #   for line in dice_art.get(dice[die]):
   #     print(line)

#Horizontal Approach:
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()


for die in dice:
    total += die
    print(f"Total: {total}")