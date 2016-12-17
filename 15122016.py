meile = 1.60934
km = 0.621371

while True:
    Beginn = (raw_input("Was moechten Sie umwandeln - geben Sie km oder m ein: "))

    if Beginn == "q":
        break

    elif Beginn != "km" and Beginn != "m":
        print "bitte waehlen Sie zuerst Kilometer oder Meter"

    else:

        Zahl = int(raw_input("Bitte geben Sie Ihre Zahl ein: "))

        if Beginn == "km":
            print "Ihre eingegebenen Kilometer sind " + str(Zahl * km) + " Meilen"

        elif Beginn == "m":
            print "Ihre eingegebenen Meilen sind " + str(Zahl * km) + " Kilometer"
