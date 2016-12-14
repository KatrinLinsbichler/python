secret = 1987
guess = int(raw_input("Bitte erraten Sie die geheime Zahl: "))

if guess == secret:
    print "Congratulations!! You won. :-) :-) "

else:
    print "Sorry, the number is not correct. Please try it again."