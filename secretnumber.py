secret = 1987
guess = int(raw_input("Bitte erraten Sie die gemeine Zahl: "))

while guess != secret:
    print "Sorry  do it again"
    guess = int(raw_input("Bitte erraten Sie die gemeine Zahl: "))

if guess == secret:
    print "Congratulations!! You won. :-) :-)"