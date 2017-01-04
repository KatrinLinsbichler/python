import random

anzahlziffern = int(raw_input("Wie viele Ziffern zwischen 0 und 99 soll das Programm ausgeben (1-9 moeglich)? "))

lottozahlen = []

for i in range(anzahlziffern):
    secret_num = random.randint(0, 99)
    lottozahlen.append(secret_num)

print "Ihre Zahlen sind: " + str(lottozahlen)


#ohne doppelte Ziffern

anzahlziffern = int(raw_input("Wie viele Ziffern zwischen 0 und 99 soll das Programm ausgeben (1-9 moeglich)? "))

while anzahlziffern >=10:
    print "Bitte geben Sie ein Zahl zwischen 1 und 9 ein."
    anzahlziffern = int(raw_input("Wie viele Ziffern zwischen 0 und 99 soll das Programm ausgeben (1-9 moeglich)? "))

lottozahlen = []

for i in range(anzahlziffern):
    secret_num = random.randint(0, 9)
    while secret_num in lottozahlen:
        secret_num = random.randint(0, 9)
    lottozahlen.append(secret_num)

print "Ihre Zahlen sind: " + str(lottozahlen)

