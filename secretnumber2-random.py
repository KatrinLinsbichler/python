import random

secret_num = random.randint(0, 9)

def main():
    for i in range(3):
        guess = int(raw_input("Bitte erraten Sie die geheime einstellige Zahl: "))
        if guess == secret_num:
            print "Congratulations!! You won. :-) :-)"
            break
        else:
            if i == 3:
                print "your chance is over."
            elif guess > secret_num:
                print "Du bist zu hoch. Du hast noch " + str(2 - i) + " Versuch(e)"
            elif guess < secret_num:
                print "das ist zu niedrig. Du hast noch so viele versuche"
                print 2 - i

if __name__ == "__main__":
    main()



