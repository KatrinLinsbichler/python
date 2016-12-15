secret = 15

for i in range(3):
    guess = int(raw_input("Bitte erraten Sie die geheime zweistellige Zahl: "))
    if guess == secret:
        print "Congratulations!! You won. :-) :-)"
        break
    else:
        if i == 3:
            print "your chance is over."
        elif guess > secret:
            print "Du bist zu hoch. Du hast noch " + str(2 - i) + " Versuch(e)"
        elif guess < secret:
            print "das ist zu niedrig. Du hast noch so viele versuche"
            print 2 - i




