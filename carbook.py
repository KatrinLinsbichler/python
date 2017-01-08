class Carbookeintrag(object):
    def __init__(self, brand, model, kilometersdonesofar, generalservicedate):
        self.brand = brand
        self.model = model
        self.kilometers = kilometersdonesofar
        self.service = generalservicedate

    def __str__(self):
        return "Brand: " + self.brand + " Model: " + self.model + " Kilometers so far: " +self.kilometers + " Last service: " + self.service

def seeallcars(carbook):
    for index, car in enumerate(carbook):
        print str(index) + ") " + str(car)
    print ""

def addnewcar(carbook):
    carbook_temp = []

    while True:
        brand = raw_input("Please enter the new car. Start with the brand: ")
        model = raw_input("Model: ")
        kilometersdonesofar = raw_input("How many kilometers have you done so far: ")
        generalservicedate = raw_input("When was the last general service: ")
        print ""

        car = Carbookeintrag(brand = brand, model = model, kilometersdonesofar = kilometersdonesofar, generalservicedate = generalservicedate)

        carbook_temp.append(car)

        print "This car has been added to your list: " + " " + str(brand) + " " + str(model)
        print ""

        anotherentry = raw_input("do you want to enter another car? Please press y or n: ")
        print ""

        if anotherentry == "n":
            break

    print "Overview of added cars:"
    for car in carbook_temp:
        print str(car)
        carbook.append(car)
    print ""

def deletecar(carbook):
    print "Which car do you want to delete?"
    seeallcars(carbook)
    print ""
    deletedcar = int(raw_input("Please enter the index number of your car? "))
    print ""

    if deletedcar >= 0 and deletedcar < len(carbook):
        del carbook[deletedcar]
        print "Entry successfully deleted."
    else:
        print "Index not valid"

def editkilometers(carbook):
    print "Which kilometers do you want to edit?"
    seeallcars(carbook)
    print ""
    index_car = int(raw_input("Please enter the index number of your car? "))
    newkilometer = raw_input("new value: ")
    carbook[index_car].kilometers = newkilometer
    print ""
    print carbook[index_car]

def editdateservice(carbook):
    print "Which service date do you want to edit?"
    seeallcars(carbook)
    print ""
    index_car = int(raw_input("Please enter the index number of your car? "))
    newdate = raw_input("new date: ")
    carbook[index_car].service = newdate
    print ""
    print carbook[index_car]

def main():
    audi = Carbookeintrag(brand = "Audi", model = "A4", kilometersdonesofar = "60.000", generalservicedate = "29. Juli 2016")
    bmw = Carbookeintrag(brand = "BMW", model = "X5", kilometersdonesofar = "100.000", generalservicedate = "30. Dezember 2016")
    carbook = [audi, bmw]

    print "Welcome to your car book! Please choose what you want to do: "


    while True:
        print "a) see a list of vehicles the company has "
        print "b) edit kilometers "
        print "c) edit general service date "
        print "d) add new vehicle(s) "
        print "e) delete a vehicle"
        print ""

        userauswahl = raw_input("Please enter which option you want to choose (a, b, c, d, e): ")

        if userauswahl == "a":
            seeallcars(carbook)

        if userauswahl == "b":
            editkilometers(carbook)

        if userauswahl == "c":
            editdateservice(carbook)

        if userauswahl == "d":
            addnewcar(carbook)

        if userauswahl == "e":
            deletecar(carbook)

        weitereoption = raw_input("Do you want to do another thing? Press y for yes or any other letter for no: ")
        if weitereoption == "y":
            print "Please choose what you want to do: "
            print ""

        else:
            print "Good Bye"
            break

if __name__ == "__main__":
    main()